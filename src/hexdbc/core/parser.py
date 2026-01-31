import struct
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional


@dataclass
class DBCHeader:
    magic: bytes
    record_count: int
    field_count: int
    record_size: int
    string_block_size: int
    
    @property
    def is_valid(self) -> bool:
        return self.magic == b'WDBC'


@dataclass
class DBCRecord:
    fields: List[int]
    
    def __getitem__(self, index: int) -> int:
        return self.fields[index]
    
    def __len__(self) -> int:
        return len(self.fields)


@dataclass
class DBCFile:
    header: DBCHeader
    records: List[List[int]]  # Each record is a list of uint32 values
    string_block: bytes
    source_path: Optional[Path] = None
    
    def get_string(self, offset: int) -> str:
        if offset == 0 or offset >= len(self.string_block):
            return ""
        
        end = self.string_block.find(b'\x00', offset)
        if end == -1:
            end = len(self.string_block)
        
        try:
            return self.string_block[offset:end].decode('utf-8', errors='replace')
        except:
            return ""
    
    def get_field_as_int(self, record_idx: int, field_idx: int) -> int:
        if record_idx < 0 or record_idx >= len(self.records):
            return 0
        if field_idx < 0 or field_idx >= len(self.records[record_idx]):
            return 0
        return self.records[record_idx][field_idx]
    
    def get_field_as_signed(self, record_idx: int, field_idx: int) -> int:
        value = self.get_field_as_int(record_idx, field_idx)
        if value >= 0x80000000:
            return value - 0x100000000
        return value
    
    def get_field_as_float(self, record_idx: int, field_idx: int) -> float:
        value = self.get_field_as_int(record_idx, field_idx)
        return struct.unpack('<f', struct.pack('<I', value))[0]
    
    def get_field_as_string(self, record_idx: int, field_idx: int) -> str:
        offset = self.get_field_as_int(record_idx, field_idx)
        return self.get_string(offset)


class DBCParser:
    HEADER_SIZE = 20
    HEADER_FORMAT = '<4sIIII'
    
    def parse(self, file_path: Path) -> DBCFile:
        with open(file_path, 'rb') as f:
            data = f.read()
        
        return self.parse_bytes(data, file_path)
    
    def parse_bytes(self, data: bytes, source_path: Optional[Path] = None) -> DBCFile:
        if len(data) < self.HEADER_SIZE:
            raise ValueError("File too small to be a valid DBC file")
        
        # Parse header
        header_data = struct.unpack(self.HEADER_FORMAT, data[:self.HEADER_SIZE])
        header = DBCHeader(
            magic=header_data[0],
            record_count=header_data[1],
            field_count=header_data[2],
            record_size=header_data[3],
            string_block_size=header_data[4]
        )
        
        if not header.is_valid:
            raise ValueError(f"Invalid DBC magic: {header.magic}")
        
        # Calculate expected sizes
        records_size = header.record_count * header.record_size
        expected_size = self.HEADER_SIZE + records_size + header.string_block_size
        
        if len(data) < expected_size:
            raise ValueError(f"File size mismatch: expected {expected_size}, got {len(data)}")
        
        # Parse records
        records = []
        fields_per_record = header.record_size // 4
        
        for i in range(header.record_count):
            offset = self.HEADER_SIZE + (i * header.record_size)
            record_data = data[offset:offset + header.record_size]
            
            # Parse each field as uint32
            fields = []
            for j in range(fields_per_record):
                field_offset = j * 4
                if field_offset + 4 <= len(record_data):
                    value = struct.unpack('<I', record_data[field_offset:field_offset + 4])[0]
                    fields.append(value)
            
            records.append(fields)
        
        # Extract string block
        string_block_offset = self.HEADER_SIZE + records_size
        string_block = data[string_block_offset:string_block_offset + header.string_block_size]
        
        return DBCFile(
            header=header,
            records=records,
            string_block=string_block,
            source_path=source_path
        )


class DBCWriter:

    HEADER_FORMAT = '<4sIIII'
    
    def write(self, dbc: DBCFile, file_path: Path) -> None:
        data = self.to_bytes(dbc)
        with open(file_path, 'wb') as f:
            f.write(data)
    
    def to_bytes(self, dbc: DBCFile) -> bytes:
        # Build records data
        records_data = bytearray()
        for record in dbc.records:
            for field in record:
                records_data.extend(struct.pack('<I', field & 0xFFFFFFFF))
        
        # Build header
        header_data = struct.pack(
            self.HEADER_FORMAT,
            b'WDBC',
            len(dbc.records),
            dbc.header.field_count,
            dbc.header.record_size,
            len(dbc.string_block)
        )
        
        return header_data + bytes(records_data) + dbc.string_block
