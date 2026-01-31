from pathlib import Path
from typing import Dict, List, Optional, Any

from hexdbc.core.parser import DBCParser, DBCFile
from hexdbc.core.schema import SchemaManager
from hexdbc.core.hexdbc_format import HexDBCGenerator


class DBCCache:
    def __init__(self, parser: DBCParser, schema_manager: SchemaManager):
        self.parser = parser
        self.schema_manager = schema_manager
        self.generator = HexDBCGenerator(schema_manager)
        self.folder: Optional[Path] = None
        self._cache: Dict[str, DBCFile] = {}
        self._available_dbcs: set[str] = set()
        self._indices: Dict[str, Dict[int, List[int]]] = {}

    def set_folder(self, folder: Path) -> None:
        self.folder = folder
        self._cache.clear()
        self._available_dbcs.clear()
        self._indices.clear()

        if folder and folder.is_dir():
            # Scan once so we know what's available
            for f in folder.glob("*.dbc"):
                self._available_dbcs.add(f.stem)

    def clear(self) -> None:
        self._cache.clear()
        self._available_dbcs.clear()
        self._indices.clear()
        self.folder = None

    def is_available(self, dbc_name: str) -> bool:
        return dbc_name in self._available_dbcs

    def get_dbc(self, dbc_name: str) -> Optional[DBCFile]:

        if dbc_name in self._cache:
            return self._cache[dbc_name]

        if not self.folder or dbc_name not in self._available_dbcs:
            return None

        # Try to load from disk
        try:
            file_path = self.folder / f"{dbc_name}.dbc"
            if not file_path.is_file():
                return None

            dbc_file = self.parser.parse(file_path)
            self._cache[dbc_name] = dbc_file

            # Drop any existing index so it rebuilds next time
            if dbc_name in self._indices:
                del self._indices[dbc_name]

            return dbc_file

        except Exception as e:
            print(f"Failed to load {dbc_name}.dbc: {e}")

        return None

    def add_open_dbc(self, dbc_name: str, dbc_file: DBCFile) -> None:
        self._cache[dbc_name] = dbc_file
        self._available_dbcs.add(dbc_name)

        # Force index rebuild
        if dbc_name in self._indices:
            del self._indices[dbc_name]

    def _ensure_index(self, dbc_name: str, dbc_file: DBCFile) -> None:

        if dbc_name in self._indices:
            return

        index: Dict[int, List[int]] = {}

        for record in dbc_file.records:
            if not record:
                continue

            # First field is ID
            entry_id = record[0]
            index[entry_id] = record

        self._indices[dbc_name] = index

    def lookup_entry(self, dbc_name: str, entry_id: int) -> Optional[Dict[str, Any]]:

        dbc_file = self.get_dbc(dbc_name)
        if not dbc_file:
            return None

        self._ensure_index(dbc_name, dbc_file)

        record = self._indices[dbc_name].get(entry_id)
        if not record:
            return None

        schema = self.schema_manager.get_schema(dbc_name)

        # Convert record list into a dict using schema info
        result: Dict[str, Any] = {}

        for i, value in enumerate(record):
            if schema and i < len(schema.fields):
                field_def = schema.fields[i]
                result[field_def.name] = value
            else:
                # Fallback if schema is missing or shorter than record
                result[f"Field{i}"] = value

        return result

    def get_entry_preview(
        self,
        dbc_name: str,
        entry_id: int,
        max_fields: int = 6,
    ) -> Optional[str]:
        entry = self.lookup_entry(dbc_name, entry_id)
        if not entry:
            return None

        lines = [f"[{dbc_name}] ID: {entry_id}"]

        shown = 0
        for name, value in entry.items():
            if name.startswith("_") or name == "ID":
                continue

            str_val = str(value)

            # Truncate long values so tooltips don't get insane
            if len(str_val) > 50:
                str_val = str_val[:47] + "..."

            # Skip empty-ish values
            if str_val == "" or str_val == "0":
                continue

            lines.append(f"  {name}: {str_val}")
            shown += 1

            if shown >= max_fields:
                lines.append("  ...")
                break

        return "\n".join(lines)

    def get_available_dbcs(self) -> List[str]:
        return sorted(self._available_dbcs)