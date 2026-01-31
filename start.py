import sys
import os

# Ensure we're running from the correct directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Add src to path so the package can be found
sys.path.insert(0, os.path.join(script_dir, 'src'))

# Create QApplication FIRST - before any other Qt imports
from PySide6.QtWidgets import QApplication
import hexdbc

app = QApplication(sys.argv)
app.setApplicationName("HexDBC")
app.setApplicationVersion(hexdbc.__version__)

# NOW it's safe to import the main window (which imports QScintilla)
from hexdbc.ui.main_window import HexDBCWindow

window = HexDBCWindow()
window.show()

sys.exit(app.exec())
