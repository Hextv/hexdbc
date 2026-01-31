"""
Main window for HexDBC editor with multi-tab support.
"""

import os
import re
import webbrowser
from pathlib import Path
from typing import Optional, Dict, List
from dataclasses import dataclass, field
from datetime import datetime

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon, QKeySequence, QFont, QFontDatabase
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QFileDialog, QMessageBox, QToolBar, QStatusBar, QSplitter,
    QTreeWidget, QTreeWidgetItem, QFrame, QApplication, QTabWidget,
    QTabBar, QPushButton
)

from hexdbc.ui.editor import CodeEditor
from hexdbc.core.parser import DBCParser, DBCWriter, DBCFile
from hexdbc.core.hexdbc_format import HexDBCGenerator, HexDBCParser
from hexdbc.core.schema import SchemaManager
from hexdbc.core.dbc_cache import DBCCache
from hexdbc.core.dbc_relations import get_reference
from hexdbc.ui.theme import get_stylesheet, COLORS
from hexdbc.ui.dialogs import (
    AdvancedSearchDialog, AddEntryDialog,
    CommandPaletteDialog, FileComparisonDialog
)
from hexdbc.ui.reference_tooltip import ReferenceTooltip


@dataclass
class TabState:
    """State data for each editor tab."""
    file_path: Optional[Path] = None
    dbc_file: Optional[DBCFile] = None
    original_dbc_path: Optional[Path] = None
    is_modified: bool = False
    change_history: List[Dict] = field(default_factory=list)  # Track changes


class ClosableTabBar(QTabBar):
    """Custom tab bar with styled close buttons."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTabsClosable(True)
        self.setMovable(True)
        self.setExpanding(False)
        self.setDocumentMode(True)


class HexDBCWindow(QMainWindow):
    """Main application window with multi-tab editor."""
    
    def __init__(self):
        super().__init__()
        
        # Per-tab state tracking: tab_index -> TabState
        self.tab_states: Dict[int, TabState] = {}
        
        # Core components
        self.parser = DBCParser()
        self.writer = DBCWriter()
        self.schema_manager = SchemaManager()
        self.generator = HexDBCGenerator(self.schema_manager)
        self.hexdbc_parser = HexDBCParser(self.schema_manager)
        
        # DBC cache for cross-references (lazy loads DBCs from folder)
        self.dbc_cache = DBCCache(self.parser, self.schema_manager)
        
        # Current folder path
        self.current_folder: Optional[Path] = None
        
        self._init_ui()
        
        # Reference tooltip (created after UI init)
        self.reference_tooltip = ReferenceTooltip(self)
        self.reference_tooltip.navigate_requested.connect(self._on_reference_navigate)
        self._create_actions()
        self._create_menus()
        self._create_toolbar()
        self._create_statusbar()
        
        self._update_title()
    
    def _init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle("HexDBC")
        self.setMinimumSize(1200, 800)
        self.resize(1400, 900)
        
        # Apply theme
        self.setStyleSheet(get_stylesheet())
        
        # Central widget
        central = QWidget()
        self.setCentralWidget(central)
        
        # Main layout with splitter
        layout = QHBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        splitter = QSplitter(Qt.Orientation.Horizontal)
        layout.addWidget(splitter)
        
        # Left panel - File browser
        self.file_panel = self._create_file_panel()
        splitter.addWidget(self.file_panel)
        
        # Right panel - Tabbed Editor
        editor_container = self._create_editor_panel()
        splitter.addWidget(editor_container)
        
        # Set splitter sizes (20% / 80%)
        splitter.setSizes([280, 1120])
        splitter.setStretchFactor(0, 0)
        splitter.setStretchFactor(1, 1)
    
    def _create_file_panel(self) -> QWidget:
        """Create the left file browser panel."""
        panel = QFrame()
        panel.setStyleSheet(f"""
            QFrame {{
                background-color: {COLORS['bg_secondary']};
                border-right: 1px solid {COLORS['border_primary']};
            }}
        """)
        
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Header
        header = QLabel("  DBC Files")
        header.setStyleSheet(f"""
            QLabel {{
                background-color: {COLORS['bg_tertiary']};
                color: {COLORS['text_primary']};
                padding: 12px 8px;
                font-size: 13px;
                font-weight: 600;
                border-bottom: 1px solid {COLORS['border_primary']};
            }}
        """)
        layout.addWidget(header)
        
        # File tree
        self.file_tree = QTreeWidget()
        self.file_tree.setHeaderHidden(True)
        self.file_tree.setRootIsDecorated(False)
        self.file_tree.setStyleSheet(f"""
            QTreeWidget {{
                background-color: {COLORS['bg_secondary']};
                border: none;
                outline: none;
            }}
            QTreeWidget::item {{
                padding: 8px 12px;
            }}
            QTreeWidget::item:hover {{
                background-color: {COLORS['bg_tertiary']};
            }}
            QTreeWidget::item:selected {{
                background-color: {COLORS['accent_blue']};
            }}
        """)
        self.file_tree.itemDoubleClicked.connect(self._on_file_double_clicked)
        layout.addWidget(self.file_tree)
        
        return panel
    
    def _create_editor_panel(self) -> QWidget:
        """Create the main tabbed editor panel."""
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Tab widget for multiple files
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(False)  # We'll add custom close buttons
        self.tab_widget.setMovable(True)
        self.tab_widget.setDocumentMode(True)
        
        # Style the tab widget
        self.tab_widget.setStyleSheet(f"""
            QTabWidget::pane {{
                border: none;
                background-color: {COLORS['bg_primary']};
            }}
            QTabBar {{
                background-color: {COLORS['bg_secondary']};
            }}
            QTabBar::tab {{
                background-color: {COLORS['bg_secondary']};
                color: {COLORS['text_secondary']};
                padding: 10px 16px;
                padding-right: 8px;
                border: none;
                border-right: 1px solid {COLORS['border_secondary']};
                min-width: 80px;
            }}
            QTabBar::tab:selected {{
                background-color: {COLORS['bg_primary']};
                color: {COLORS['text_primary']};
                border-bottom: 2px solid {COLORS['accent_blue']};
            }}
            QTabBar::tab:hover:!selected {{
                background-color: {COLORS['bg_tertiary']};
            }}
        """)
        
        # Connect signals
        self.tab_widget.currentChanged.connect(self._on_tab_changed)
        
        layout.addWidget(self.tab_widget)
        
        # Create welcome/empty state
        self._create_welcome_tab()
        
        return container
    
    def _create_welcome_tab(self):
        """Create a welcome tab when no files are open."""
        welcome = QWidget()
        layout = QVBoxLayout(welcome)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        label = QLabel("Open a DBC file to start editing\n\nCtrl+O - Open File\nCtrl+Shift+O - Open Folder")
        label.setStyleSheet(f"""
            color: {COLORS['text_disabled']};
            font-size: 16px;
            padding: 40px;
        """)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        
        self.welcome_widget = welcome
    
    def _get_current_editor(self) -> Optional[CodeEditor]:
        """Get the currently active editor."""
        current_widget = self.tab_widget.currentWidget()
        if isinstance(current_widget, CodeEditor):
            return current_widget
        return None
    
    def _get_current_state(self) -> Optional[TabState]:
        """Get the state for the current tab."""
        idx = self.tab_widget.currentIndex()
        return self.tab_states.get(idx)
    
    def _create_new_tab(self, file_path: Path, code: str, dbc_file: Optional[DBCFile] = None) -> int:
        """Create a new editor tab and return its index."""
        # Check if file is already open
        for idx, state in self.tab_states.items():
            if state.file_path and state.file_path == file_path:
                self.tab_widget.setCurrentIndex(idx)
                return idx
        
        # Create new editor
        editor = CodeEditor()
        editor.set_text(code)
        
        # Set DBC name for FK lookups
        if file_path:
            dbc_name = file_path.stem
            if hasattr(editor, 'set_dbc_name'):
                editor.set_dbc_name(dbc_name)
        
        # Connect text changed signal
        if hasattr(editor, 'textChanged'):
            editor.textChanged.connect(lambda: self._on_editor_text_changed(editor))
        
        # Connect FK hover signals
        if hasattr(editor, 'reference_hovered'):
            editor.reference_hovered.connect(
                lambda field, val_str, val_int, pos, e=editor: self._on_reference_hover(e, field, val_str, val_int, pos)
            )
        if hasattr(editor, 'reference_left'):
            editor.reference_left.connect(self._on_reference_leave)
        
        # Add tab
        tab_name = file_path.name if file_path else "Untitled"
        idx = self.tab_widget.addTab(editor, tab_name)
        
        # Create custom close button with visible X
        close_btn = QPushButton("✕")
        close_btn.setFixedSize(20, 20)
        close_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: transparent;
                border: none;
                border-radius: 3px;
                font-size: 14px;
                font-weight: bold;
                color: {COLORS['text_disabled']};
                padding: 0px;
                margin: 0px;
            }}
            QPushButton:hover {{
                background-color: {COLORS['accent_red']};
                color: white;
            }}
        """)
        close_btn.setToolTip("Close tab")
        close_btn.clicked.connect(lambda checked, i=idx: self._close_tab(i))
        
        # Add the close button to the tab
        self.tab_widget.tabBar().setTabButton(idx, QTabBar.ButtonPosition.RightSide, close_btn)
        
        # Store state
        self.tab_states[idx] = TabState(
            file_path=file_path,
            dbc_file=dbc_file,
            original_dbc_path=file_path if file_path and file_path.suffix.lower() == '.dbc' else None,
            is_modified=False
        )
        
        # Switch to the new tab
        self.tab_widget.setCurrentIndex(idx)
        
        return idx
    
    def _close_tab(self, index: int):
        """Close a tab, prompting to save if modified."""
        state = self.tab_states.get(index)
        
        if state and state.is_modified:
            file_name = state.file_path.name if state.file_path else "Untitled"
            reply = QMessageBox.question(
                self, "Unsaved Changes",
                f"{file_name} has unsaved changes. Save before closing?",
                QMessageBox.StandardButton.Save | 
                QMessageBox.StandardButton.Discard | 
                QMessageBox.StandardButton.Cancel
            )
            
            if reply == QMessageBox.StandardButton.Cancel:
                return
            elif reply == QMessageBox.StandardButton.Save:
                self.tab_widget.setCurrentIndex(index)
                self.save_file()
        
        # Remove the tab
        self.tab_widget.removeTab(index)
        
        # Update tab states (indices shift after removal)
        new_states = {}
        for idx, s in self.tab_states.items():
            if idx < index:
                new_states[idx] = s
            elif idx > index:
                new_states[idx - 1] = s
        self.tab_states = new_states
        
        # Update close button connections (indices have shifted)
        self._update_close_button_connections()
        
        # Update UI
        self._on_tab_changed(self.tab_widget.currentIndex())
    
    def _update_close_button_connections(self):
        """Update all close button connections after tab index changes."""
        for idx in range(self.tab_widget.count()):
            close_btn = self.tab_widget.tabBar().tabButton(idx, QTabBar.ButtonPosition.RightSide)
            if close_btn and isinstance(close_btn, QPushButton):
                # Disconnect all and reconnect with correct index
                try:
                    close_btn.clicked.disconnect()
                except:
                    pass
                close_btn.clicked.connect(lambda checked, i=idx: self._close_tab(i))
    
    def _on_tab_changed(self, index: int):
        """Handle tab change - update status bar and title."""
        state = self.tab_states.get(index)
        
        if state and state.file_path:
            self.status_file.setText(f"Editing: {state.file_path.name}")
            if state.dbc_file:
                self.status_stats.setText(
                    f"{state.dbc_file.header.record_count} records | "
                    f"{state.dbc_file.header.field_count} fields"
                )
            else:
                self.status_stats.setText("")
        else:
            self.status_file.setText("Ready")
            self.status_stats.setText("")
        
        self._update_title()
    
    def _on_editor_text_changed(self, editor: CodeEditor):
        """Handle text changes in an editor."""
        # Find which tab this editor belongs to
        for idx in range(self.tab_widget.count()):
            if self.tab_widget.widget(idx) is editor:
                state = self.tab_states.get(idx)
                if state and not state.is_modified:
                    state.is_modified = True
                    # Update tab title to show modified indicator
                    current_title = self.tab_widget.tabText(idx)
                    if not current_title.endswith(" •"):
                        self.tab_widget.setTabText(idx, current_title + " •")
                    self._update_title()
                break
    
    def _create_actions(self):
        """Create menu/toolbar actions."""
        # File actions
        self.action_open = QAction("Open DBC...", self)
        self.action_open.setShortcut(QKeySequence.StandardKey.Open)
        self.action_open.triggered.connect(self.open_file)
        
        self.action_open_folder = QAction("Open Folder...", self)
        self.action_open_folder.setShortcut("Ctrl+Shift+O")
        self.action_open_folder.triggered.connect(self.open_folder)
        
        self.action_close_tab = QAction("Close Tab", self)
        self.action_close_tab.setShortcut("Ctrl+W")
        self.action_close_tab.triggered.connect(self._close_current_tab)
        
        self.action_save = QAction("Save", self)
        self.action_save.setShortcut(QKeySequence.StandardKey.Save)
        self.action_save.triggered.connect(self.save_file)
        
        self.action_save_as = QAction("Save As...", self)
        self.action_save_as.setShortcut(QKeySequence.StandardKey.SaveAs)
        self.action_save_as.triggered.connect(self.save_file_as)
        
        self.action_export_dbc = QAction("Export to DBC...", self)
        self.action_export_dbc.setShortcut("Ctrl+E")
        self.action_export_dbc.triggered.connect(self.export_dbc)
        
        self.action_export_hexdbc = QAction("Export to HexDBC...", self)
        self.action_export_hexdbc.setShortcut("Ctrl+Shift+E")
        self.action_export_hexdbc.triggered.connect(self.export_hexdbc)
        
        self.action_exit = QAction("Exit", self)
        self.action_exit.setShortcut("Alt+F4")
        self.action_exit.triggered.connect(self.close)
        
        # Edit actions
        self.action_undo = QAction("Undo", self)
        self.action_undo.setShortcut(QKeySequence.StandardKey.Undo)
        self.action_undo.triggered.connect(lambda: self._get_current_editor().undo() if self._get_current_editor() and hasattr(self._get_current_editor(), 'undo') else None)
        
        self.action_redo = QAction("Redo", self)
        self.action_redo.setShortcut(QKeySequence.StandardKey.Redo)
        self.action_redo.triggered.connect(lambda: self._get_current_editor().redo() if self._get_current_editor() and hasattr(self._get_current_editor(), 'redo') else None)
        
        self.action_cut = QAction("Cut", self)
        self.action_cut.setShortcut(QKeySequence.StandardKey.Cut)
        self.action_cut.triggered.connect(lambda: self._get_current_editor().cut() if self._get_current_editor() and hasattr(self._get_current_editor(), 'cut') else None)
        
        self.action_copy = QAction("Copy", self)
        self.action_copy.setShortcut(QKeySequence.StandardKey.Copy)
        self.action_copy.triggered.connect(lambda: self._get_current_editor().copy() if self._get_current_editor() and hasattr(self._get_current_editor(), 'copy') else None)
        
        self.action_paste = QAction("Paste", self)
        self.action_paste.setShortcut(QKeySequence.StandardKey.Paste)
        self.action_paste.triggered.connect(lambda: self._get_current_editor().paste() if self._get_current_editor() and hasattr(self._get_current_editor(), 'paste') else None)
        
        self.action_advanced_search = QAction("Search...", self)
        self.action_advanced_search.setShortcut(QKeySequence.StandardKey.Find)
        self.action_advanced_search.triggered.connect(self._show_advanced_search)
        
        self.action_add_entry = QAction("Add New Entry...", self)
        self.action_add_entry.setShortcut("Ctrl+N")
        self.action_add_entry.triggered.connect(self._show_add_entry)
        
        # New navigation actions
        self.action_command_palette = QAction("Command Palette...", self)
        self.action_command_palette.setShortcut("Ctrl+Shift+P")
        self.action_command_palette.triggered.connect(self._show_command_palette)
        
        self.action_file_comparison = QAction("Compare Files...", self)
        self.action_file_comparison.setShortcut("Ctrl+D")
        self.action_file_comparison.triggered.connect(self._show_file_comparison)
        
        # View actions
        self.action_zoom_in = QAction("Zoom In", self)
        self.action_zoom_in.setShortcut(QKeySequence.StandardKey.ZoomIn)
        self.action_zoom_in.triggered.connect(lambda: self._get_current_editor().zoomIn() if self._get_current_editor() and hasattr(self._get_current_editor(), 'zoomIn') else None)
        
        self.action_zoom_out = QAction("Zoom Out", self)
        self.action_zoom_out.setShortcut(QKeySequence.StandardKey.ZoomOut)
        self.action_zoom_out.triggered.connect(lambda: self._get_current_editor().zoomOut() if self._get_current_editor() and hasattr(self._get_current_editor(), 'zoomOut') else None)
        
        # Help actions
        self.action_about = QAction("About HexDBC", self)
        self.action_about.triggered.connect(self._show_about)
    
    def _create_menus(self):
        """Create the menu bar with navigation arrows."""
        menubar = self.menuBar()
        
        # Add undo/redo arrows as menu bar actions with proper icons
        style = self.style()
        
        undo_action = menubar.addAction("")
        undo_action.setIcon(style.standardIcon(style.StandardPixmap.SP_ArrowLeft))
        undo_action.setToolTip("Undo (Ctrl+Z)")
        undo_action.triggered.connect(self.action_undo.trigger)
        
        redo_action = menubar.addAction("")
        redo_action.setIcon(style.standardIcon(style.StandardPixmap.SP_ArrowRight))
        redo_action.setToolTip("Redo (Ctrl+Y)")
        redo_action.triggered.connect(self.action_redo.trigger)
        
        # File menu
        file_menu = menubar.addMenu("File")
        file_menu.addAction(self.action_open)
        file_menu.addAction(self.action_open_folder)
        file_menu.addSeparator()
        file_menu.addAction(self.action_close_tab)
        file_menu.addSeparator()
        file_menu.addAction(self.action_save)
        file_menu.addAction(self.action_save_as)
        file_menu.addAction(self.action_export_dbc)
        file_menu.addAction(self.action_export_hexdbc)
        file_menu.addSeparator()
        file_menu.addAction(self.action_exit)
        
        # Edit menu
        edit_menu = menubar.addMenu("Edit")
        edit_menu.addAction(self.action_undo)
        edit_menu.addAction(self.action_redo)
        edit_menu.addSeparator()
        edit_menu.addAction(self.action_cut)
        edit_menu.addAction(self.action_copy)
        edit_menu.addAction(self.action_paste)
        edit_menu.addSeparator()
        edit_menu.addAction(self.action_advanced_search)
        edit_menu.addSeparator()
        edit_menu.addAction(self.action_add_entry)
        
        # View menu
        view_menu = menubar.addMenu("View")
        view_menu.addAction(self.action_zoom_in)
        view_menu.addAction(self.action_zoom_out)
        view_menu.addSeparator()
        view_menu.addAction(self.action_command_palette)
        view_menu.addAction(self.action_file_comparison)
        
        # Help menu
        help_menu = menubar.addMenu("Help")
        help_menu.addAction(self.action_about)
    
    def _create_toolbar(self):
        """Create the main toolbar."""
        toolbar = QToolBar("Main Toolbar")
        toolbar.setMovable(False)
        toolbar.setIconSize(QSize(20, 20))
        self.addToolBar(toolbar)
        
        # Styled buttons
        def make_button(text, action):
            btn = toolbar.addAction(text)
            btn.triggered.connect(action.trigger)
            return btn
        
        make_button("Open", self.action_open)
        make_button("Folder", self.action_open_folder)
        toolbar.addSeparator()
        make_button("Save", self.action_save)
        make_button("Export DBC", self.action_export_dbc)
        make_button("Export HexDBC", self.action_export_hexdbc)
        toolbar.addSeparator()
        make_button("Search", self.action_advanced_search)
        make_button("Add Entry", self.action_add_entry)
        
        # Add spacer to push Ko-fi button to the right
        spacer = QWidget()
        spacer.setSizePolicy(spacer.sizePolicy().horizontalPolicy(), spacer.sizePolicy().verticalPolicy())
        from PySide6.QtWidgets import QSizePolicy
        spacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        toolbar.addWidget(spacer)
        
        # Ko-fi support button - Premium red design
        kofi_btn = QPushButton("❤  Support Me")
        kofi_btn.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #FF6B6B, stop:1 #EE5A5A);
                color: white;
                border: 1px solid #D94444;
                border-radius: 8px;
                padding: 8px 18px;
                font-size: 13px;
                font-weight: bold;
                font-family: 'Segoe UI', sans-serif;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #FF5252, stop:1 #E53935);
                border-color: #C62828;
            }
            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #D32F2F, stop:1 #C62828);
            }
        """)
        kofi_btn.setToolTip("Support HexDBC on Ko-fi")
        kofi_btn.clicked.connect(lambda: webbrowser.open("https://ko-fi.com/hex23"))
        toolbar.addWidget(kofi_btn)
    
    def _create_statusbar(self):
        """Create the status bar."""
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        
        # File info label
        self.status_file = QLabel("Ready")
        self.statusbar.addWidget(self.status_file, 1)
        
        # Stats label
        self.status_stats = QLabel("")
        self.statusbar.addPermanentWidget(self.status_stats)
        
        # Position label
        self.status_pos = QLabel("Ln 1, Col 1")
        self.statusbar.addPermanentWidget(self.status_pos)
    
    def _update_title(self):
        """Update window title based on current tab."""
        state = self._get_current_state()
        if state and state.file_path:
            modified = " •" if state.is_modified else ""
            self.setWindowTitle(f"HexDBC - {state.file_path.name}{modified}")
        else:
            self.setWindowTitle("HexDBC")
    
    def _close_current_tab(self):
        """Close the currently active tab."""
        idx = self.tab_widget.currentIndex()
        if idx >= 0:
            self._close_tab(idx)
    
    def _on_file_double_clicked(self, item: QTreeWidgetItem, column: int):
        """Handle file tree double click."""
        file_path = item.data(0, Qt.ItemDataRole.UserRole)
        if file_path and Path(file_path).is_file():
            self._load_dbc(Path(file_path))
    
    def open_file(self):
        """Open a DBC file (or multiple files)."""
        file_paths, _ = QFileDialog.getOpenFileNames(
            self, "Open DBC File(s)", "",
            "DBC Files (*.dbc);;HexDBC Files (*.hexdbc);;All Files (*.*)"
        )
        
        for file_path in file_paths:
            path = Path(file_path)
            if path.suffix.lower() == '.hexdbc':
                self._load_hexdbc(path)
            else:
                self._load_dbc(path)
    
    def open_folder(self):
        """Open a folder containing DBC files."""
        folder = QFileDialog.getExistingDirectory(
            self, "Open Folder with DBC Files"
        )
        
        if folder:
            self._populate_file_tree(Path(folder))
    
    def _populate_file_tree(self, folder: Path):
        """Populate the file tree with DBC files from a folder."""
        self.file_tree.clear()
        
        # Set folder for DBC cache (enables FK resolution)
        self.current_folder = folder
        self.dbc_cache.set_folder(folder)
        
        dbc_files = sorted(folder.glob("*.dbc"), key=lambda p: p.name.lower())
        
        for dbc_file in dbc_files:
            item = QTreeWidgetItem([dbc_file.stem])
            item.setData(0, Qt.ItemDataRole.UserRole, str(dbc_file))
            self.file_tree.addTopLevelItem(item)
        
        self.status_file.setText(f"Found {len(dbc_files)} DBC files in {folder.name}")
    
    def _load_dbc(self, file_path: Path):
        """Load and convert a DBC file to hexdbc code in a new tab."""
        try:
            dbc_file = self.parser.parse(file_path)
            
            # Generate hexdbc code
            code = self.generator.generate(dbc_file, file_path.stem)
            
            # Create new tab
            self._create_new_tab(file_path, code, dbc_file)
            
            # Update status
            self.status_file.setText(f"Loaded: {file_path.name}")
            self.status_stats.setText(f"{dbc_file.header.record_count} records | {dbc_file.header.field_count} fields")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load DBC file:\n{e}")
    
    def _load_hexdbc(self, file_path: Path):
        """Load a .hexdbc file into a new tab."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()
            
            # Create new tab
            self._create_new_tab(file_path, code, None)
            
            self.status_file.setText(f"Loaded: {file_path.name}")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load file:\n{e}")
    
    def save_file(self):
        """Save - always prompts for location and format."""
        self.save_file_as()
    
    def save_file_as(self):
        """Save the current file - prompts for location and format (DBC or hexdbc)."""
        editor = self._get_current_editor()
        state = self._get_current_state()
        
        if not editor or editor.get_text().strip() == "":
            QMessageBox.warning(self, "Warning", "No content to save.")
            return
        
        # Suggest original name with .dbc extension
        suggested = ""
        if state and state.file_path:
            suggested = str(state.file_path.with_suffix('.dbc'))
        
        file_path, selected_filter = QFileDialog.getSaveFileName(
            self, "Save As", suggested,
            "DBC Files (*.dbc);;HexDBC Code Files (*.hexdbc);;All Files (*.*)"
        )
        
        if file_path:
            path = Path(file_path)
            # Determine format based on extension or selected filter
            if path.suffix.lower() == '.hexdbc' or ('hexdbc' in selected_filter.lower() and path.suffix.lower() != '.dbc'):
                if not path.suffix:
                    path = path.with_suffix('.hexdbc')
                self._save_hexdbc(path)
            else:
                if not path.suffix:
                    path = path.with_suffix('.dbc')
                self._save_to_dbc(path)
    
    def _save_hexdbc(self, file_path: Path):
        """Save content as .hexdbc file."""
        try:
            editor = self._get_current_editor()
            state = self._get_current_state()
            
            if not editor:
                return
            
            code = editor.get_text()
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(code)
            
            if state:
                state.file_path = file_path
                state.is_modified = False
            
            # Update tab title
            idx = self.tab_widget.currentIndex()
            self.tab_widget.setTabText(idx, file_path.name)
            
            self._update_title()
            self.status_file.setText(f"Saved: {file_path.name}")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save file:\n{e}")
    
    def _save_to_dbc(self, file_path: Path):
        """Save content directly to DBC format."""
        try:
            editor = self._get_current_editor()
            state = self._get_current_state()
            
            if not editor:
                return
            
            code = editor.get_text()
            dbc = self.hexdbc_parser.parse(code, state.dbc_file if state else None)
            
            if self.hexdbc_parser.errors:
                errors = "\n".join(self.hexdbc_parser.errors[:5])
                result = QMessageBox.warning(
                    self, "Parse Warnings",
                    f"The following issues were found:\n\n{errors}\n\nSave anyway?",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                )
                if result != QMessageBox.StandardButton.Yes:
                    return
            
            self.writer.write(dbc, file_path)
            
            if state:
                state.file_path = file_path
                state.original_dbc_path = file_path
                state.dbc_file = dbc
                state.is_modified = False
            
            # Update tab title
            idx = self.tab_widget.currentIndex()
            self.tab_widget.setTabText(idx, file_path.name)
            
            self._update_title()
            self.status_file.setText(f"Saved DBC: {file_path.name}")
            self.status_stats.setText(f"{dbc.header.record_count} records | {dbc.header.field_count} fields")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save DBC:\n{e}")
    
    def export_dbc(self):
        """Export the current hexdbc code to a DBC file."""
        state = self._get_current_state()
        
        if not state or not state.file_path:
            QMessageBox.warning(self, "Warning", "No file open to export.")
            return
        
        # Suggest original .dbc name if available
        suggested_name = ""
        if state.file_path.suffix.lower() == '.dbc':
            suggested_name = str(state.file_path)
        elif state.file_path.suffix.lower() == '.hexdbc':
            suggested_name = str(state.file_path.with_suffix('.dbc'))
        
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Export to DBC", suggested_name,
            "DBC Files (*.dbc);;All Files (*.*)"
        )
        
        if file_path:
            self._export_to_dbc(Path(file_path))
    
    def _export_to_dbc(self, file_path: Path):
        """Export hexdbc code to DBC format."""
        try:
            editor = self._get_current_editor()
            state = self._get_current_state()
            
            if not editor:
                return
            
            code = editor.get_text()
            dbc = self.hexdbc_parser.parse(code, state.dbc_file if state else None)
            
            if self.hexdbc_parser.errors:
                errors = "\n".join(self.hexdbc_parser.errors[:10])
                QMessageBox.warning(
                    self, "Parse Warnings",
                    f"The following issues were found:\n\n{errors}"
                )
            
            self.writer.write(dbc, file_path)
            self.status_file.setText(f"Exported to: {file_path.name}")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to export DBC:\n{e}")
    
    def export_hexdbc(self):
        """Export the current code visualization to a HexDBC file."""
        editor = self._get_current_editor()
        state = self._get_current_state()
        
        if not editor or editor.get_text().strip() == "":
            QMessageBox.warning(self, "Warning", "No content to export.")
            return
        
        # Suggest name based on current file
        suggested_name = ""
        if state and state.file_path:
            if state.file_path.suffix.lower() == '.dbc':
                suggested_name = str(state.file_path.with_suffix('.hexdbc'))
            elif state.file_path.suffix.lower() == '.hexdbc':
                suggested_name = str(state.file_path)
            else:
                suggested_name = str(state.file_path.with_suffix('.hexdbc'))
        
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Export to HexDBC", suggested_name,
            "HexDBC Code Files (*.hexdbc);;All Files (*.*)"
        )
        
        if file_path:
            path = Path(file_path)
            if not path.suffix:
                path = path.with_suffix('.hexdbc')
            
            try:
                code = editor.get_text()
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(code)
                
                self.status_file.setText(f"Exported to: {path.name}")
                
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to export HexDBC:\n{e}")
    
    def _show_advanced_search(self):
        """Show search dialog. Triggered by Ctrl+F."""
        editor = self._get_current_editor()
        if editor:
            dialog = AdvancedSearchDialog(self, editor)
            dialog.show()  # Non-modal so user can interact with editor
    
    def _show_add_entry(self):
        """Show add entry dialog."""
        editor = self._get_current_editor()
        state = self._get_current_state()
        
        if not editor:
            QMessageBox.warning(self, "Warning", "No file open.")
            return
        
        # Get current schema and max ID
        schema = None
        dbc_name = ""
        max_id = 0
        
        if state and state.file_path:
            dbc_name = state.file_path.stem
            schema = self.schema_manager.get_schema(dbc_name)
        
        # Parse editor content to find max ID and existing IDs
        content = editor.get_text()
        id_matches = re.findall(r'\w+\((\d+)\)\s*\{', content)
        existing_ids = set(int(m) for m in id_matches)
        if existing_ids:
            max_id = max(existing_ids)
        
        dialog = AddEntryDialog(self, schema, max_id, dbc_name, existing_ids)
        if dialog.exec():
            # Insert the new entry at the end of the file
            code = dialog.get_code()
            current_text = editor.get_text()
            
            # Add newlines before the new entry if needed
            if current_text and not current_text.endswith('\n\n'):
                if current_text.endswith('\n'):
                    code = '\n' + code
                else:
                    code = '\n\n' + code
            
            # Use efficient append instead of replacing entire text
            # This avoids re-highlighting the entire document for large files
            if hasattr(editor, 'append_text'):
                editor.append_text(code)
            else:
                editor.set_text(current_text + code)
            
            self.status_file.setText(f"Added new entry with ID {dialog.id_input.value()}")
    
    def _show_about(self):
        """Show about dialog."""
        QMessageBox.about(
            self, "About HexDBC",
            "<h2>HexDBC</h2>"
            "<p>Version 1.0.0</p>"
            "<p>A modern code-based DBC editor for WoW 3.3.5a modding.</p>"
            "<p>Edit DBC files using readable code instead of spreadsheets.</p>"
        )
    
    def _on_reference_hover(self, editor, field_name: str, value_str: str, value_int: int, cursor_pos):
        """Handle hover over a potential FK field."""
        # Get the DBC name from the editor
        dbc_name = ""
        if hasattr(editor, 'get_dbc_name'):
            dbc_name = editor.get_dbc_name()
        
        if not dbc_name:
            return
        
        # Check if this field has a FK reference
        target_dbc = get_reference(dbc_name, field_name)
        if not target_dbc:
            return
        
        # Get preview of the referenced entry
        preview = self.dbc_cache.get_entry_preview(target_dbc, value_int)
        
        # Only show tooltip if we have actual data to display
        if not preview:
            return
        
        # Show the tooltip
        self.reference_tooltip.show_reference(
            source_dbc=dbc_name,
            field_name=field_name,
            value=value_int,
            target_dbc=target_dbc,
            entry_preview=preview,
            position=cursor_pos
        )
    
    def _on_reference_leave(self):
        """Handle mouse leaving a FK field."""
        self.reference_tooltip.schedule_hide(delay_ms=400)
    
    def _on_reference_navigate(self, dbc_name: str, entry_id: int):
        """Handle navigation to a referenced DBC entry."""
        if not self.current_folder:
            QMessageBox.warning(self, "Navigation", "No folder open. Open a folder to enable navigation.")
            return
        
        # Check if DBC file exists
        dbc_path = self.current_folder / f"{dbc_name}.dbc"
        if not dbc_path.is_file():
            QMessageBox.warning(self, "Navigation", f"{dbc_name}.dbc not found in folder.")
            return
        
        # Load the DBC in a new tab
        self._load_dbc(dbc_path)
        
        # Find the line containing the entry ID and scroll to it
        editor = self._get_current_editor()
        if editor:
            text = editor.get_text()
            lines = text.split('\n')
            
            # Look for entry with matching ID
            for i, line in enumerate(lines):
                # Match entry header like "entry(123)" or "ID = 123"
                if f'entry({entry_id})' in line or f'ID = {entry_id}' in line:
                    editor.scroll_to_line(i)
                    self.status_file.setText(f"Navigated to {dbc_name} entry {entry_id}")
                    return
            
            self.status_file.setText(f"Opened {dbc_name}.dbc (entry {entry_id} not found in text)")
    
    def _show_command_palette(self):
        """Show command palette for quick action access."""
        # Build command dictionary
        commands = {
            "Open File": ("Open a DBC or HexDBC file", self.action_open.trigger),
            "Open Folder": ("Open a folder containing DBC files", self.action_open_folder.trigger),
            "Save": ("Save the current file", self.action_save.trigger),
            "Save As": ("Save the current file with a new name", self.action_save_as.trigger),
            "Export to DBC": ("Export current file to DBC format", self.action_export_dbc.trigger),
            "Export to HexDBC": ("Export current file to HexDBC format", self.action_export_hexdbc.trigger),
            "Close Tab": ("Close the current tab", self.action_close_tab.trigger),
            "Search": ("Advanced search in current file", self.action_advanced_search.trigger),
            "Add New Entry": ("Add a new DBC entry", self.action_add_entry.trigger),
            "Compare Files": ("Compare two DBC files", self.action_file_comparison.trigger),
            "Zoom In": ("Increase editor font size", self.action_zoom_in.trigger),
            "Zoom Out": ("Decrease editor font size", self.action_zoom_out.trigger),
            "Undo": ("Undo last change", self.action_undo.trigger),
            "Redo": ("Redo last undone change", self.action_redo.trigger),
        }
        
        dialog = CommandPaletteDialog(self, commands)
        dialog.exec()
    
    def _show_file_comparison(self):
        """Show file comparison dialog."""
        state = self._get_current_state()
        editor = self._get_current_editor()
        
        # Pre-fill with current file if available
        file1_path = str(state.file_path) if state and state.file_path else ""
        content1 = editor.get_text() if editor and hasattr(editor, 'get_text') else ""
        
        dialog = FileComparisonDialog(self, file1_path=file1_path, content1=content1)
        dialog.exec()
    
    
    def closeEvent(self, event):
        """Handle window close - check all tabs for unsaved changes."""
        # Check all tabs for unsaved changes
        unsaved_tabs = []
        for idx, state in self.tab_states.items():
            if state.is_modified:
                name = state.file_path.name if state.file_path else "Untitled"
                unsaved_tabs.append(name)
        
        if unsaved_tabs:
            files_list = "\n".join(f"  • {name}" for name in unsaved_tabs[:5])
            if len(unsaved_tabs) > 5:
                files_list += f"\n  ... and {len(unsaved_tabs) - 5} more"
            
            reply = QMessageBox.question(
                self, "Unsaved Changes",
                f"The following files have unsaved changes:\n\n{files_list}\n\nDiscard all changes and exit?",
                QMessageBox.StandardButton.Discard | 
                QMessageBox.StandardButton.Cancel
            )
            
            if reply == QMessageBox.StandardButton.Cancel:
                event.ignore()
                return
        
        event.accept()


def run():
    """Run the HexDBC application."""
    import sys
    
    app = QApplication(sys.argv)
    app.setApplicationName("HexDBC")
    app.setApplicationVersion("1.0.0")
    
    window = HexDBCWindow()
    window.show()
    
    sys.exit(app.exec())
