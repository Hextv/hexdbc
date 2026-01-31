"""
HexDBC UI Module - User interface components.
"""

from hexdbc.ui.main_window import HexDBCWindow, run
from hexdbc.ui.editor import CodeEditor
from hexdbc.ui.dialogs import AdvancedSearchDialog, AddEntryDialog
from hexdbc.ui.theme import COLORS, get_stylesheet, get_editor_colors

__all__ = [
    "HexDBCWindow",
    "run",
    "CodeEditor",
    "AdvancedSearchDialog",
    "AddEntryDialog",
    "COLORS",
    "get_stylesheet",
    "get_editor_colors",
]
