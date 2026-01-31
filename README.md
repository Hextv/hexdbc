# HexDBC

A modern, code-based DBC editor for World of Warcraft 3.3.5a (WotLK) modding.

HexDBC reimagines DBC editing by treating data as code. Instead of working with cumbersome spreadsheets, you edit DBC files using a clean, readable text format (`.hexdbc`) with full syntax highlighting and validation.
## Getting Started

### Prerequisites

- Python 3.9 or higher
- `pip` package manager

### Installation

   1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hexdbc.git
   cd hexdbc
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To start HexDBC in development mode:

```bash
python start.py
```

## Building from Source

To create a standalone executable (`.exe`), simply run the build script:

```bash
build.bat
```

The executable will be created in the `dist/` directory.

## Project Structure

- **`src/hexdbc`**: Main source code.
    - **`core/`**: Core logic for parsing, schema validation, and formatting.
    - **`ui/`**: Qt-based user interface components.
    - **`resources/`**: Static resources and assets.
- **`tools/`**: Utility scripts, including schema generators.
- **`pyproject.toml`**: Project metadata and dependency configuration.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Authors

- **Hex**
  
NOTE: If you contribute to the project your name will be added here

---
