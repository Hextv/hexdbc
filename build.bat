@echo off
echo Installing requirements...
pip install pyinstaller

echo.
echo Building HexDBC...
pyinstaller --noconfirm --onefile --windowed --name "HexDBC" --icon "icon/hexdbc.ico" --paths "src" start.py

echo.
echo Build complete! The executable is in the 'dist' folder.
pause
