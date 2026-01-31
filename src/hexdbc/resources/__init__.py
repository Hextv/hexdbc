from pathlib import Path

RESOURCES_DIR = Path(__file__).parent
SCHEMAS_DIR = RESOURCES_DIR / "schemas"


def get_schema_path(schema_name: str) -> Path:
    return SCHEMAS_DIR / f"{schema_name}.xml"


def list_schemas() -> list:
    if SCHEMAS_DIR.exists():
        return [f.stem for f in SCHEMAS_DIR.glob("*.xml")]
    return []
