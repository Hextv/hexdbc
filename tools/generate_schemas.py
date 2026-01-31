import xml.etree.ElementTree as ET
from pathlib import Path

# Localized string takes 17 fields (16 locales + flags)
LOC_FIELDS = 17

def parse_xml_definitions(xml_path: Path) -> dict:
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    schemas = {}
    
    for table in root.findall('Table'):
        name = table.get('Name')
        fields = []
        field_idx = 0
        
        for field in table.findall('Field'):
            fname = field.get('Name')
            ftype = field.get('Type', 'int')
            array_size = int(field.get('ArraySize', '1'))
            
            # Map XML types to our FieldType
            if ftype == 'loc':
                # Localized strings expand to 17 fields
                py_type = 'LOCSTRING'
                for i in range(LOC_FIELDS):
                    if i < 16:
                        suffix = f'_{["enUS","koKR","frFR","deDE","enCN","enTW","esES","esMX","ruRU","jaJP","ptPT","itIT","Unk12","Unk13","Unk14","Unk15"][i]}'
                    else:
                        suffix = '_Flags'
                    fields.append({
                        'idx': field_idx,
                        'name': f'{fname}{suffix}',
                        'type': 'STRING' if i < 16 else 'UINT'
                    })
                    field_idx += 1
            elif ftype == 'string':
                for i in range(array_size):
                    suffix = f'_{i}' if array_size > 1 else ''
                    fields.append({
                        'idx': field_idx,
                        'name': f'{fname}{suffix}',
                        'type': 'STRING'
                    })
                    field_idx += 1
            elif ftype == 'float':
                for i in range(array_size):
                    suffix = f'_{i}' if array_size > 1 else ''
                    fields.append({
                        'idx': field_idx,
                        'name': f'{fname}{suffix}',
                        'type': 'FLOAT'
                    })
                    field_idx += 1
            elif ftype in ('uint', 'ulong'):
                for i in range(array_size):
                    suffix = f'_{i}' if array_size > 1 else ''
                    fields.append({
                        'idx': field_idx,
                        'name': f'{fname}{suffix}',
                        'type': 'UINT'
                    })
                    field_idx += 1
            elif ftype in ('byte', 'bool'):
                for i in range(array_size):
                    suffix = f'_{i}' if array_size > 1 else ''
                    fields.append({
                        'idx': field_idx,
                        'name': f'{fname}{suffix}',
                        'type': 'UINT'
                    })
                    field_idx += 1
            else:  # int or default
                for i in range(array_size):
                    suffix = f'_{i}' if array_size > 1 else ''
                    fields.append({
                        'idx': field_idx,
                        'name': f'{fname}{suffix}',
                        'type': 'INT'
                    })
                    field_idx += 1
        
        schemas[name] = {
            'name': name,
            'fields': fields,
            'field_count': field_idx
        }
    
    return schemas


def generate_schema_code(schemas: dict) -> str:
    lines = []
    lines.append('"""')
    lines.append('DBC Schema definitions for WoW 3.3.5a (build 12340).')
    lines.append('Auto-generated from WDBX definitions.')
    lines.append('"""')
    lines.append('')
    lines.append('from dataclasses import dataclass, field')
    lines.append('from enum import Enum, auto')
    lines.append('from typing import Dict, List, Optional')
    lines.append('')
    lines.append('')
    lines.append('class FieldType(Enum):')
    lines.append('    """Field data types."""')
    lines.append('    UINT = auto()')
    lines.append('    INT = auto()')
    lines.append('    FLOAT = auto()')
    lines.append('    STRING = auto()')
    lines.append('    LOCSTRING = auto()')
    lines.append('    FLAGS = auto()')
    lines.append('    ENUM = auto()')
    lines.append('')
    lines.append('')
    lines.append('@dataclass')
    lines.append('class FieldDef:')
    lines.append('    """Field definition."""')
    lines.append('    name: str')
    lines.append('    type: FieldType = FieldType.UINT')
    lines.append('    description: str = ""')
    lines.append('    enum_name: Optional[str] = None')
    lines.append('')
    lines.append('')
    lines.append('@dataclass')
    lines.append('class SchemaDef:')
    lines.append('    """Schema definition for a DBC file."""')
    lines.append('    name: str')
    lines.append('    fields: List[FieldDef] = field(default_factory=list)')
    lines.append('    enums: Dict[str, Dict[int, str]] = field(default_factory=dict)')
    lines.append('')
    lines.append('    def get_field(self, index: int) -> Optional[FieldDef]:')
    lines.append('        """Get field definition by index."""')
    lines.append('        if 0 <= index < len(self.fields):')
    lines.append('            return self.fields[index]')
    lines.append('        return None')
    lines.append('')
    lines.append('')
    lines.append('# Built-in schemas for WoW 3.3.5a DBCs')
    lines.append('BUILTIN_SCHEMAS: Dict[str, SchemaDef] = {}')
    lines.append('')
    
    # Generate schema for each table
    for name, schema in sorted(schemas.items()):
        lines.append('')
        lines.append(f'# {name} - {schema["field_count"]} fields')
        lines.append(f'BUILTIN_SCHEMAS["{name}"] = SchemaDef(')
        lines.append(f'    name="{name}",')
        lines.append('    fields=[')
        
        for f in schema['fields']:
            ftype = f['type']
            fname = f['name'].replace('"', '\\"')
            lines.append(f'        FieldDef("{fname}", FieldType.{ftype}),')
        
        lines.append('    ]')
        lines.append(')')
    
    lines.append('')
    lines.append('')
    lines.append('class SchemaManager:')
    lines.append('    """Manages DBC schemas."""')
    lines.append('')
    lines.append('    def __init__(self):')
    lines.append('        self.schemas = dict(BUILTIN_SCHEMAS)')
    lines.append('')
    lines.append('    def get_schema(self, dbc_name: str) -> Optional[SchemaDef]:')
    lines.append('        """Get schema for a DBC file."""')
    lines.append('        # Try exact match first')
    lines.append('        if dbc_name in self.schemas:')
    lines.append('            return self.schemas[dbc_name]')
    lines.append('        # Try case-insensitive')
    lines.append('        for name, schema in self.schemas.items():')
    lines.append('            if name.lower() == dbc_name.lower():')
    lines.append('                return schema')
    lines.append('        return None')
    lines.append('')
    lines.append('    def generate_fallback_schema(self, field_count: int, name: str = "Unknown") -> SchemaDef:')
    lines.append('        """Generate a fallback schema with generic field names."""')
    lines.append('        fields = [FieldDef(f"field_{i}", FieldType.UINT) for i in range(field_count)]')
    lines.append('        return SchemaDef(name=name, fields=fields)')
    lines.append('')
    
    return '\n'.join(lines)


if __name__ == '__main__':
    # Parse full definitions
    script_dir = Path(__file__).parent
    xml_path = script_dir / 'resources' / 'WotLK 3.3.5 (12340).xml'
    
    if not xml_path.exists():
        print(f"Full definitions not found at {xml_path}")
        print("Using subset definitions...")
        xml_path = script_dir / 'resources' / 'dbc_definitions.xml'
    
    schemas = parse_xml_definitions(xml_path)
    print(f"Parsed {len(schemas)} schemas")
    
    # Show field count for a few
    for name in ['Achievement', 'Spell', 'Item', 'Map', 'ChrRaces']:
        if name in schemas:
            print(f"  {name}: {schemas[name]['field_count']} fields")
    
    code = generate_schema_code(schemas)
    
    # Output to src/hexdbc/core/schema.py (relative to tools/)
    output_path = script_dir.parent / 'src' / 'hexdbc' / 'core' / 'schema.py'
    output_path.write_text(code, encoding='utf-8')
    print(f"Generated {output_path}")
