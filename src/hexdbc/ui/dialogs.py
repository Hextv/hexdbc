"""
Advanced dialogs for HexDBC editor.
- AdvancedSearchDialog: Multi-field search with Find All
- AddEntryDialog: Easy record creation with schema support
- QuickJumpDialog: Quick ID-based navigation (Ctrl+I)
- CommandPaletteDialog: Command launcher (Ctrl+Shift+P)
- ChangeHistoryDialog: View edit history
- FileComparisonDialog: Side-by-side file comparison
"""

import re
import difflib
from datetime import datetime
from typing import Optional, List, Tuple, Dict
from pathlib import Path

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QCheckBox, QListWidget, QListWidgetItem,
    QFormLayout, QScrollArea, QWidget, QFrame, QSpinBox,
    QDoubleSpinBox, QGroupBox, QSplitter, QComboBox, QMessageBox,
    QTextBrowser, QFileDialog
)

from hexdbc.ui.theme import COLORS
from hexdbc.core.schema import SchemaManager, FieldType


class AdvancedSearchDialog(QDialog):
    """Advanced search dialog with multi-field filtering and Find All."""
    
    # Signal emitted when user wants to go to a specific line
    goto_line = Signal(int)
    
    def __init__(self, parent=None, editor=None):
        super().__init__(parent)
        self.editor = editor
        self.results: List[Tuple[int, str]] = []  # (line_number, preview)
        
        self.setWindowTitle("Advanced Search")
        self.setMinimumSize(600, 500)
        self.setStyleSheet(f"""
            QDialog {{
                background-color: {COLORS['bg_primary']};
                color: {COLORS['text_primary']};
            }}
        """)
        
        self._init_ui()
    
    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(12)
        layout.setContentsMargins(16, 16, 16, 16)
        
        # Search input section
        search_group = QGroupBox("Search")
        search_group.setStyleSheet(f"""
            QGroupBox {{
                font-weight: bold;
                border: 1px solid {COLORS['border_primary']};
                border-radius: 6px;
                margin-top: 8px;
                padding-top: 8px;
            }}
            QGroupBox::title {{
                color: {COLORS['text_primary']};
                subcontrol-origin: margin;
                left: 12px;
            }}
        """)
        search_layout = QVBoxLayout(search_group)
        
        # Search text field
        input_row = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search text or ID...")
        self.search_input.returnPressed.connect(self._do_find_all)
        input_row.addWidget(self.search_input)
        search_layout.addLayout(input_row)
        
        # Field filter
        field_row = QHBoxLayout()
        field_row.addWidget(QLabel("Field:"))
        self.field_filter = QLineEdit()
        self.field_filter.setPlaceholderText("Filter by field name (optional, e.g. 'Name' or 'ID')")
        field_row.addWidget(self.field_filter)
        search_layout.addLayout(field_row)
        
        # Options row
        options_row = QHBoxLayout()
        self.case_sensitive = QCheckBox("Case Sensitive")
        self.regex_mode = QCheckBox("Regex")
        self.whole_word = QCheckBox("Whole Word")
        options_row.addWidget(self.case_sensitive)
        options_row.addWidget(self.regex_mode)
        options_row.addWidget(self.whole_word)
        options_row.addStretch()
        search_layout.addLayout(options_row)
        
        layout.addWidget(search_group)
        
        # Button row
        button_row = QHBoxLayout()
        
        self.find_next_btn = QPushButton("Find Next")
        self.find_next_btn.clicked.connect(self._do_find_next)
        
        self.find_all_btn = QPushButton("Find All")
        self.find_all_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {COLORS['accent_blue']};
                border-color: {COLORS['accent_blue']};
            }}
        """)
        self.find_all_btn.clicked.connect(self._do_find_all)
        
        button_row.addWidget(self.find_next_btn)
        button_row.addWidget(self.find_all_btn)
        button_row.addStretch()
        
        layout.addLayout(button_row)
        
        # Results section
        results_label = QLabel("Results:")
        results_label.setStyleSheet(f"color: {COLORS['text_secondary']}; font-weight: bold;")
        layout.addWidget(results_label)
        
        self.results_list = QListWidget()
        self.results_list.setStyleSheet(f"""
            QListWidget {{
                background-color: {COLORS['bg_secondary']};
                border: 1px solid {COLORS['border_primary']};
                border-radius: 6px;
            }}
            QListWidget::item {{
                padding: 8px;
                border-bottom: 1px solid {COLORS['border_secondary']};
            }}
            QListWidget::item:selected {{
                background-color: {COLORS['accent_blue']};
            }}
            QListWidget::item:hover:!selected {{
                background-color: {COLORS['bg_tertiary']};
            }}
        """)
        self.results_list.itemClicked.connect(self._on_result_clicked)
        layout.addWidget(self.results_list)
        
        # Status label
        self.status_label = QLabel("")
        self.status_label.setStyleSheet(f"color: {COLORS['text_secondary']};")
        layout.addWidget(self.status_label)
        
        # Close button
        close_row = QHBoxLayout()
        close_row.addStretch()
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.close)
        close_row.addWidget(close_btn)
        layout.addLayout(close_row)
    
    def _do_find_next(self):
        """Find next occurrence."""
        if not self.editor:
            return
        
        text = self.search_input.text()
        if not text:
            return
        
        if hasattr(self.editor, 'findFirst'):
            case = self.case_sensitive.isChecked()
            regex = self.regex_mode.isChecked()
            word = self.whole_word.isChecked()
            
            # Try findNext first, then findFirst
            if not self.editor.findNext():
                self.editor.findFirst(text, regex, case, word, True)
    
    def _do_find_all(self):
        """Find all occurrences and populate results list."""
        self.results.clear()
        self.results_list.clear()
        
        if not self.editor:
            self.status_label.setText("No editor available")
            return
        
        search_text = self.search_input.text()
        if not search_text:
            self.status_label.setText("Enter search text")
            return
        
        field_filter = self.field_filter.text().strip().lower()
        case_sensitive = self.case_sensitive.isChecked()
        use_regex = self.regex_mode.isChecked()
        whole_word = self.whole_word.isChecked()
        
        # Get editor content
        content = self.editor.get_text() if hasattr(self.editor, 'get_text') else ""
        lines = content.split('\n')
        
        # Build search pattern
        if use_regex:
            try:
                flags = 0 if case_sensitive else re.IGNORECASE
                pattern = re.compile(search_text, flags)
            except re.error as e:
                self.status_label.setText(f"Invalid regex: {e}")
                return
        else:
            if not case_sensitive:
                search_text_lower = search_text.lower()
        
        # Search through lines
        for line_num, line in enumerate(lines, 1):
            # Field filter check
            if field_filter:
                # Check if line contains the field
                line_lower = line.lower()
                if f"{field_filter} =" not in line_lower and f"{field_filter}=" not in line_lower:
                    continue
            
            # Search pattern check
            match_found = False
            if use_regex:
                match_found = pattern.search(line) is not None
            elif case_sensitive:
                if whole_word:
                    match_found = re.search(rf'\b{re.escape(search_text)}\b', line) is not None
                else:
                    match_found = search_text in line
            else:
                line_lower = line.lower()
                if whole_word:
                    match_found = re.search(rf'\b{re.escape(search_text_lower)}\b', line_lower) is not None
                else:
                    match_found = search_text_lower in line_lower
            
            if match_found:
                preview = line.strip()[:80]
                if len(line.strip()) > 80:
                    preview += "..."
                self.results.append((line_num, preview))
                
                item = QListWidgetItem(f"Line {line_num}: {preview}")
                item.setData(Qt.ItemDataRole.UserRole, line_num)
                self.results_list.addItem(item)
        
        self.status_label.setText(f"Found {len(self.results)} matches")
    
    def _on_result_clicked(self, item: QListWidgetItem):
        """Go to the clicked result line."""
        line_num = item.data(Qt.ItemDataRole.UserRole)
        if line_num and self.editor:
            if hasattr(self.editor, 'scroll_to_line'):
                self.editor.scroll_to_line(line_num - 1)
            elif hasattr(self.editor, 'setCursorPosition'):
                self.editor.setCursorPosition(line_num - 1, 0)
            
            self.editor.setFocus()
            self.goto_line.emit(line_num)


class AddEntryDialog(QDialog):
    """Dialog to add a new DBC entry with schema-aware field inputs."""
    
    # Signal emitted with the generated code
    entry_created = Signal(str)
    
    def __init__(self, parent=None, schema=None, current_max_id=0, dbc_name="", existing_ids=None):
        super().__init__(parent)
        self.schema = schema
        self.current_max_id = current_max_id
        self.dbc_name = dbc_name
        self.field_inputs = {}
        self.existing_ids = existing_ids or set()  # Set of IDs that already exist
        
        self.setWindowTitle(f"Add New Entry - {dbc_name}" if dbc_name else "Add New Entry")
        self.setMinimumSize(500, 600)
        self.setStyleSheet(f"""
            QDialog {{
                background-color: {COLORS['bg_primary']};
                color: {COLORS['text_primary']};
            }}
        """)
        
        self._init_ui()
    
    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(12)
        layout.setContentsMargins(16, 16, 16, 16)
        
        # Header
        header = QLabel(f"Create new {self.dbc_name} record" if self.dbc_name else "Create new record")
        header.setStyleSheet(f"""
            font-size: 16px;
            font-weight: bold;
            color: {COLORS['text_primary']};
            padding-bottom: 8px;
        """)
        layout.addWidget(header)
        
        # ID input (always first)
        id_layout = QHBoxLayout()
        
        self.id_input = QSpinBox()
        self.id_input.setRange(1, 999999999)
        self.id_input.setValue(self.current_max_id + 1)
        self.id_input.setStyleSheet(f"""
            QSpinBox {{
                background-color: {COLORS['bg_input']};
                color: {COLORS['text_primary']};
                border: 1px solid {COLORS['border_primary']};
                border-radius: 6px;
                padding: 8px;
                font-size: 14px;
            }}
        """)
        
        id_layout.addWidget(QLabel("ID:"))
        id_layout.addWidget(self.id_input)
        self.id_hint_label = QLabel(f"(Next available: {self.current_max_id + 1})")
        id_layout.addWidget(self.id_hint_label)
        id_layout.addStretch()
        
        # Warning label for duplicate IDs
        self.id_warning_label = QLabel("")
        self.id_warning_label.setStyleSheet(f"color: {COLORS['accent_red']}; font-weight: bold;")
        self.id_warning_label.hide()
        
        id_group_layout = QVBoxLayout()
        id_group_layout.addLayout(id_layout)
        id_group_layout.addWidget(self.id_warning_label)
        
        id_group = QGroupBox("Record ID")
        id_group.setStyleSheet(f"""
            QGroupBox {{
                font-weight: bold;
                border: 1px solid {COLORS['border_primary']};
                border-radius: 6px;
                margin-top: 8px;
                padding-top: 8px;
            }}
            QGroupBox::title {{
                color: {COLORS['text_primary']};
                subcontrol-origin: margin;
                left: 12px;
            }}
        """)
        id_group.setLayout(id_group_layout)
        layout.addWidget(id_group)
        
        # Connect ID change to validation
        self.id_input.valueChanged.connect(self._validate_id)
        
        # Fields scroll area
        fields_group = QGroupBox("Fields")
        fields_group.setStyleSheet(f"""
            QGroupBox {{
                font-weight: bold;
                border: 1px solid {COLORS['border_primary']};
                border-radius: 6px;
                margin-top: 8px;
                padding-top: 8px;
            }}
            QGroupBox::title {{
                color: {COLORS['text_primary']};
                subcontrol-origin: margin;
                left: 12px;
            }}
        """)
        fields_outer = QVBoxLayout(fields_group)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet(f"""
            QScrollArea {{
                border: none;
                background-color: transparent;
            }}
        """)
        
        scroll_widget = QWidget()
        self.fields_layout = QFormLayout(scroll_widget)
        self.fields_layout.setSpacing(8)
        
        # Add field inputs based on schema
        if self.schema:
            for i, field_def in enumerate(self.schema.fields):
                if field_def.name.upper() == 'ID':
                    continue  # Skip ID, we handle it separately
                
                self._add_field_input(field_def.name, field_def.type, field_def.description)
        else:
            # No schema - add generic fields
            for i in range(10):
                self._add_field_input(f"Field_{i}", FieldType.INT, "")
        
        scroll.setWidget(scroll_widget)
        fields_outer.addWidget(scroll)
        layout.addWidget(fields_group, 1)  # Stretch factor 1
        
        # Buttons
        button_row = QHBoxLayout()
        button_row.addStretch()
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        
        add_btn = QPushButton("Add Entry")
        add_btn.setDefault(True)  # Make this the default button (responds to Enter)
        add_btn.setAutoDefault(True)
        add_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {COLORS['accent_green']};
                border-color: {COLORS['accent_green']};
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: #2ea043;
            }}
        """)
        add_btn.clicked.connect(self._create_entry)
        
        button_row.addWidget(cancel_btn)
        button_row.addWidget(add_btn)
        layout.addLayout(button_row)
        
        # Store add button for enabling/disabling
        self.add_btn = add_btn
    
    def _validate_id(self, value: int):
        """Validate if the ID already exists."""
        if value in self.existing_ids:
            self.id_warning_label.setText(f"Warning: ID {value} already exists!")
            self.id_warning_label.show()
            self.add_btn.setEnabled(False)
            self.add_btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {COLORS['text_disabled']};
                    border-color: {COLORS['text_disabled']};
                    font-weight: bold;
                }}
            """)
        else:
            self.id_warning_label.hide()
            self.add_btn.setEnabled(True)
            self.add_btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {COLORS['accent_green']};
                    border-color: {COLORS['accent_green']};
                    font-weight: bold;
                }}
                QPushButton:hover {{
                    background-color: #2ea043;
                }}
            """)
    
    def _add_field_input(self, name: str, field_type: FieldType, description: str):
        """Add an input widget for a field."""
        label = QLabel(name)
        if description:
            label.setToolTip(description)
        
        # Create appropriate input based on type
        if field_type == FieldType.FLOAT:
            widget = QDoubleSpinBox()
            widget.setRange(-999999999, 999999999)
            widget.setDecimals(6)
            widget.setValue(0.0)
        elif field_type == FieldType.STRING or field_type == FieldType.LOCSTRING:
            widget = QLineEdit()
            widget.setPlaceholderText("Enter text..." if field_type == FieldType.STRING else "Localized text...")
        else:
            widget = QSpinBox()
            widget.setRange(-2147483648, 2147483647)
            widget.setValue(0)
        
        widget.setStyleSheet(f"""
            QSpinBox, QDoubleSpinBox, QLineEdit {{
                background-color: {COLORS['bg_input']};
                color: {COLORS['text_primary']};
                border: 1px solid {COLORS['border_primary']};
                border-radius: 4px;
                padding: 6px;
            }}
        """)
        
        self.field_inputs[name] = (widget, field_type)
        self.fields_layout.addRow(label, widget)
    
    def _create_entry(self):
        """Generate the record code and emit signal."""
        record_id = self.id_input.value()
        
        # Double-check for duplicates
        if record_id in self.existing_ids:
            QMessageBox.warning(
                self, "Duplicate ID",
                f"ID {record_id} already exists. Please choose a different ID."
            )
            return
        
        # Get the record function name (table name in lowercase)
        record_name = self.dbc_name.lower() if self.dbc_name else "record"
        
        # Build the record code
        lines = [f"{record_name}({record_id}) {{"]
        
        # Add ID first
        lines.append(f"    ID = {record_id}")
        
        # Add other fields
        for name, (widget, field_type) in self.field_inputs.items():
            if field_type == FieldType.FLOAT:
                value = widget.value()
                lines.append(f"    {name} = {value}")
            elif field_type == FieldType.STRING or field_type == FieldType.LOCSTRING:
                text = widget.text()
                # Escape quotes
                text = text.replace('\\', '\\\\').replace('"', '\\"')
                lines.append(f'    {name} = "{text}"')
            else:
                value = widget.value()
                lines.append(f"    {name} = {value}")
        
        lines.append("}")
        
        code = "\n".join(lines)
        self.entry_created.emit(code)
        self.accept()
    
    def get_code(self) -> str:
        """Get the generated code (call after exec())."""
        record_id = self.id_input.value()
        record_name = self.dbc_name.lower() if self.dbc_name else "record"
        lines = [f"{record_name}({record_id}) {{"]
        lines.append(f"    ID = {record_id}")
        
        for name, (widget, field_type) in self.field_inputs.items():
            if field_type == FieldType.FLOAT:
                lines.append(f"    {name} = {widget.value()}")
            elif field_type in (FieldType.STRING, FieldType.LOCSTRING):
                text = widget.text().replace('\\', '\\\\').replace('"', '\\"')
                lines.append(f'    {name} = "{text}"')
            else:
                lines.append(f"    {name} = {widget.value()}")
        
        lines.append("}")
        return "\n".join(lines)


class QuickJumpDialog(QDialog):
    """Quick jump to entry by ID (Ctrl+I)."""
    
    jump_to_id = Signal(int)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Quick Jump to ID")
        self.setModal(True)
        self.setStyleSheet(f"""
            QDialog {{
                background-color: {COLORS['bg_primary']};
                color: {COLORS['text_primary']};
            }}
        """)
        
        self._init_ui()
    
    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(12)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Title
        title = QLabel("Jump to Entry ID")
        title.setStyleSheet(f"""
            font-size: 16px;
            font-weight: bold;
            color: {COLORS['text_primary']};
            padding-bottom: 8px;
        """)
        layout.addWidget(title)
        
        # ID input
        id_layout = QHBoxLayout()
        id_label = QLabel("ID:")
        id_label.setStyleSheet(f"font-size: 14px; color: {COLORS['text_secondary']};")
        
        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("Enter entry ID...")
        self.id_input.setStyleSheet(f"""
            QLineEdit {{
                background-color: {COLORS['bg_input']};
                color: {COLORS['text_primary']};
                border: 2px solid {COLORS['border_focus']};
                border-radius: 8px;
                padding: 12px 16px;
                font-size: 16px;
                font-weight: bold;
            }}
        """)
        self.id_input.returnPressed.connect(self._jump)
        self.id_input.setFocus()
        
        id_layout.addWidget(id_label)
        id_layout.addWidget(self.id_input, 1)
        layout.addLayout(id_layout)
        

        
        # Buttons
        button_row = QHBoxLayout()
        button_row.addStretch()
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        
        jump_btn = QPushButton("Jump")
        jump_btn.setDefault(True)
        jump_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {COLORS['accent_blue']};
                border-color: {COLORS['accent_blue']};
                font-weight: bold;
                padding: 10px 24px;
            }}
            QPushButton:hover {{
                background-color: #60D0FF;
            }}
        """)
        jump_btn.clicked.connect(self._jump)
        
        button_row.addWidget(cancel_btn)
        button_row.addWidget(jump_btn)
        layout.addLayout(button_row)
        
        # Set compact size with more height
        self.setFixedSize(450, 190)
    
    def _jump(self):
        """Emit jump signal and close."""
        text = self.id_input.text().strip()
        if text.isdigit():
            entry_id = int(text)
            self.jump_to_id.emit(entry_id)
            self.accept()
        else:
            self.id_input.setStyleSheet(f"""
                QLineEdit {{
                    background-color: {COLORS['bg_input']};
                    color: {COLORS['accent_red']};
                    border: 2px solid {COLORS['accent_red']};
                    border-radius: 8px;
                    padding: 12px 16px;
                    font-size: 16px;
                    font-weight: bold;
                }}
            """)


class CommandPaletteDialog(QDialog):
    """Command palette for quick action access (Ctrl+Shift+P)."""
    
    command_selected = Signal(str)
    
    def __init__(self, parent=None, commands: Dict[str, tuple] = None):
        super().__init__(parent)
        self.commands = commands or {}  # {action_name: (description, callback)}
        self.filtered_commands = []
        
        self.setWindowTitle("Command Palette")
        self.setModal(True)
        self.setStyleSheet(f"""
            QDialog {{
                background-color: {COLORS['bg_primary']};
                color: {COLORS['text_primary']};
            }}
        """)
        
        self._init_ui()
        self._populate_commands()
    
    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Search input
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Type a command...")
        self.search_input.setStyleSheet(f"""
            QLineEdit {{
                background-color: {COLORS['bg_secondary']};
                color: {COLORS['text_primary']};
                border: none;
                border-bottom: 2px solid {COLORS['border_focus']};
                padding: 16px 20px;
                font-size: 16px;
            }}
        """)
        self.search_input.textChanged.connect(self._filter_commands)
        self.search_input.returnPressed.connect(self._execute_selected)
        layout.addWidget(self.search_input)
        
        # Command list
        self.command_list = QListWidget()
        self.command_list.setStyleSheet(f"""
            QListWidget {{
                background-color: {COLORS['bg_primary']};
                border: none;
                outline: none;
                padding: 8px;
            }}
            QListWidget::item {{
                padding: 12px 16px;
                border-radius: 6px;
                margin: 2px 0;
            }}
            QListWidget::item:selected {{
                background-color: {COLORS['accent_blue']};
                color: white;
            }}
            QListWidget::item:hover:!selected {{
                background-color: {COLORS['bg_tertiary']};
            }}
        """)
        self.command_list.itemDoubleClicked.connect(self._execute_selected)
        layout.addWidget(self.command_list)
        
        # Set size
        self.setMinimumSize(600, 400)
        self.search_input.setFocus()
    
    def keyPressEvent(self, event):
        """Handle key press events."""
        # Close on Escape or Ctrl+Shift+P
        if event.key() == Qt.Key.Key_Escape:
            self.reject()
        elif event.modifiers() == (Qt.KeyboardModifier.ControlModifier | Qt.KeyboardModifier.ShiftModifier) and event.key() == Qt.Key.Key_P:
            self.reject()
        else:
            super().keyPressEvent(event)
    
    def _populate_commands(self):
        """Populate the command list."""
        self.filtered_commands = list(self.commands.keys())
        self._update_list()
    
    def _filter_commands(self, text: str):
        """Filter commands based on search text."""
        text = text.lower()
        if not text:
            self.filtered_commands = list(self.commands.keys())
        else:
            # Fuzzy matching
            self.filtered_commands = [
                cmd for cmd in self.commands.keys()
                if text in cmd.lower() or text in self.commands[cmd][0].lower()
            ]
        self._update_list()
    
    def _update_list(self):
        """Update the command list display."""
        self.command_list.clear()
        for cmd in self.filtered_commands:
            description = self.commands[cmd][0]
            item = QListWidgetItem(f"{cmd}\n  {description}")
            item.setData(Qt.ItemDataRole.UserRole, cmd)
            
            # Style the item
            font = QFont()
            font.setPointSize(11)
            item.setFont(font)
            
            self.command_list.addItem(item)
        
        # Select first item
        if self.command_list.count() > 0:
            self.command_list.setCurrentRow(0)
    
    def _execute_selected(self):
        """Execute the selected command."""
        current = self.command_list.currentItem()
        if current:
            cmd = current.data(Qt.ItemDataRole.UserRole)
            if cmd in self.commands:
                callback = self.commands[cmd][1]
                self.accept()
                if callback:
                    callback()
    
    def keyPressEvent(self, event):
        """Handle keyboard navigation."""
        if event.key() == Qt.Key.Key_Down:
            current = self.command_list.currentRow()
            if current < self.command_list.count() - 1:
                self.command_list.setCurrentRow(current + 1)
        elif event.key() == Qt.Key.Key_Up:
            current = self.command_list.currentRow()
            if current > 0:
                self.command_list.setCurrentRow(current - 1)
        elif event.key() == Qt.Key.Key_Escape:
            self.reject()
        else:
            super().keyPressEvent(event)


class ChangeHistoryDialog(QDialog):
    """Dialog to view change history for the current file."""
    
    def __init__(self, parent=None, changes: List[Dict] = None, file_name: str = ""):
        super().__init__(parent)
        self.changes = changes or []
        self.file_name = file_name
        
        self.setWindowTitle(f"Change History - {file_name}" if file_name else "Change History")
        self.setMinimumSize(700, 500)
        self.setStyleSheet(f"""
            QDialog {{
                background-color: {COLORS['bg_primary']};
                color: {COLORS['text_primary']};
            }}
        """)
        
        self._init_ui()
    
    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(12)
        layout.setContentsMargins(16, 16, 16, 16)
        
        # Header
        header = QLabel(f"Change History: {self.file_name}" if self.file_name else "Change History")
        header.setStyleSheet(f"""
            font-size: 18px;
            font-weight: bold;
            color: {COLORS['text_primary']};
            padding-bottom: 8px;
        """)
        layout.addWidget(header)
        
        # Stats
        stats = QLabel(f"Total changes: {len(self.changes)}")
        stats.setStyleSheet(f"color: {COLORS['text_secondary']}; font-size: 13px;")
        layout.addWidget(stats)
        
        # Change list
        self.change_list = QListWidget()
        self.change_list.setStyleSheet(f"""
            QListWidget {{
                background-color: {COLORS['bg_secondary']};
                border: 1px solid {COLORS['border_primary']};
                border-radius: 6px;
                padding: 4px;
            }}
            QListWidget::item {{
                padding: 12px;
                border-bottom: 1px solid {COLORS['border_secondary']};
                border-radius: 4px;
            }}
            QListWidget::item:selected {{
                background-color: {COLORS['accent_blue']};
            }}
            QListWidget::item:hover:!selected {{
                background-color: {COLORS['bg_tertiary']};
            }}
        """)
        
        # Populate changes
        for change in self.changes:
            timestamp = change.get('timestamp', 'Unknown time')
            change_type = change.get('type', 'edit')
            description = change.get('description', 'No description')
            
            item_text = f"[{timestamp}] {change_type.upper()}: {description}"
            item = QListWidgetItem(item_text)
            item.setData(Qt.ItemDataRole.UserRole, change)
            self.change_list.addItem(item)
        
        layout.addWidget(self.change_list)
        
        # Buttons
        button_row = QHBoxLayout()
        button_row.addStretch()
        
        clear_btn = QPushButton("Clear History")
        clear_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {COLORS['accent_red']};
                border-color: {COLORS['accent_red']};
            }}
        """)
        clear_btn.clicked.connect(self._clear_history)
        
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.accept)
        
        button_row.addWidget(clear_btn)
        button_row.addWidget(close_btn)
        layout.addLayout(button_row)
    
    def _clear_history(self):
        """Clear the change history."""
        reply = QMessageBox.question(
            self, "Clear History",
            "Are you sure you want to clear the change history?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.changes.clear()
            self.change_list.clear()


class FileComparisonDialog(QDialog):
    """Side-by-side file comparison dialog."""
    
    def __init__(self, parent=None, file1_path: str = "", file2_path: str = "",
                 content1: str = "", content2: str = ""):
        super().__init__(parent)
        self.file1_path = file1_path
        self.file2_path = file2_path
        self.content1 = content1
        self.content2 = content2
        
        self.setWindowTitle("File Comparison")
        self.setMinimumSize(1000, 600)
        self.setStyleSheet(f"""
            QDialog {{
                background-color: {COLORS['bg_primary']};
                color: {COLORS['text_primary']};
            }}
        """)
        
        self._init_ui()
        if content1 and content2:
            self._show_diff()
    
    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(12)
        layout.setContentsMargins(16, 16, 16, 16)
        
        # Header
        header = QLabel("File Comparison")
        header.setStyleSheet(f"""
            font-size: 18px;
            font-weight: bold;
            color: {COLORS['text_primary']};
            padding-bottom: 8px;
        """)
        layout.addWidget(header)
        
        # File selection
        file_row = QHBoxLayout()
        
        # File 1
        file1_group = QGroupBox("File 1")
        file1_group.setStyleSheet(f"""
            QGroupBox {{
                font-weight: bold;
                border: 1px solid {COLORS['border_primary']};
                border-radius: 6px;
                margin-top: 8px;
                padding-top: 8px;
            }}
        """)
        file1_layout = QHBoxLayout(file1_group)
        self.file1_label = QLabel(self.file1_path or "No file selected")
        self.file1_label.setStyleSheet(f"color: {COLORS['text_secondary']};")
        file1_btn = QPushButton("Browse...")
        file1_btn.clicked.connect(lambda: self._select_file(1))
        file1_layout.addWidget(self.file1_label, 1)
        file1_layout.addWidget(file1_btn)
        
        # File 2
        file2_group = QGroupBox("File 2")
        file2_group.setStyleSheet(f"""
            QGroupBox {{
                font-weight: bold;
                border: 1px solid {COLORS['border_primary']};
                border-radius: 6px;
                margin-top: 8px;
                padding-top: 8px;
            }}
        """)
        file2_layout = QHBoxLayout(file2_group)
        self.file2_label = QLabel(self.file2_path or "No file selected")
        self.file2_label.setStyleSheet(f"color: {COLORS['text_secondary']};")
        file2_btn = QPushButton("Browse...")
        file2_btn.clicked.connect(lambda: self._select_file(2))
        file2_layout.addWidget(self.file2_label, 1)
        file2_layout.addWidget(file2_btn)
        
        file_row.addWidget(file1_group)
        file_row.addWidget(file2_group)
        layout.addLayout(file_row)
        
        # Compare button
        compare_btn = QPushButton("Compare Files")
        compare_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {COLORS['accent_blue']};
                border-color: {COLORS['accent_blue']};
                font-weight: bold;
                padding: 10px;
            }}
        """)
        compare_btn.clicked.connect(self._compare_files)
        layout.addWidget(compare_btn)
        
        # Diff display
        self.diff_display = QTextBrowser()
        self.diff_display.setStyleSheet(f"""
            QTextBrowser {{
                background-color: {COLORS['editor_bg']};
                color: {COLORS['text_primary']};
                border: 1px solid {COLORS['border_primary']};
                border-radius: 6px;
                font-family: 'Consolas', 'Courier New', monospace;
                font-size: 12px;
                padding: 8px;
            }}
        """)
        layout.addWidget(self.diff_display, 1)
        
        # Stats
        self.stats_label = QLabel("")
        self.stats_label.setStyleSheet(f"color: {COLORS['text_secondary']}; font-size: 12px;")
        layout.addWidget(self.stats_label)
        
        # Close button
        close_row = QHBoxLayout()
        close_row.addStretch()
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.accept)
        close_row.addWidget(close_btn)
        layout.addLayout(close_row)
    
    def _select_file(self, file_num: int):
        """Select a file for comparison."""
        file_path, _ = QFileDialog.getOpenFileName(
            self, f"Select File {file_num}",
            "", "HexDBC Text Files (*.hexdbc);;All Files (*.*)"
        )
        if file_path:
            # Check if it's a binary DBC file
            if file_path.lower().endswith('.dbc'):
                QMessageBox.warning(
                    self, "Binary File",
                    "Binary .dbc files cannot be compared directly.\n\n"
                    "Please open the DBC file in the editor first, then use File Comparison "
                    "to compare the converted text."
                )
                return
            
            if file_num == 1:
                self.file1_path = file_path
                self.file1_label.setText(Path(file_path).name)
            else:
                self.file2_path = file_path
                self.file2_label.setText(Path(file_path).name)
    
    def _compare_files(self):
        """Load and compare the selected files."""
        if not self.file1_path or not self.file2_path:
            QMessageBox.warning(self, "Missing Files", "Please select both files to compare.")
            return
        
        try:
            # Check file sizes first (warn if > 1MB)
            from pathlib import Path
            file1_size = Path(self.file1_path).stat().st_size
            file2_size = Path(self.file2_path).stat().st_size
            
            if file1_size > 1_000_000 or file2_size > 1_000_000:
                reply = QMessageBox.question(
                    self, "Large File",
                    "One or both files are very large. Comparison may take a while. Continue?",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                )
                if reply == QMessageBox.StandardButton.No:
                    return
            
            # Try to read as UTF-8 first, fall back to latin-1 if that fails
            try:
                with open(self.file1_path, 'r', encoding='utf-8') as f:
                    self.content1 = f.read()
            except (UnicodeDecodeError, PermissionError) as e:
                try:
                    with open(self.file1_path, 'r', encoding='latin-1', errors='replace') as f:
                        self.content1 = f.read()
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Failed to read file 1: {e}")
                    return
            
            try:
                with open(self.file2_path, 'r', encoding='utf-8') as f:
                    self.content2 = f.read()
            except (UnicodeDecodeError, PermissionError) as e:
                try:
                    with open(self.file2_path, 'r', encoding='latin-1', errors='replace') as f:
                        self.content2 = f.read()
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Failed to read file 2: {e}")
                    return
            
            self._show_diff()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to compare files: {e}")
    
    def _show_diff(self):
        """Generate and display the diff."""
        lines1 = self.content1.splitlines(keepends=True)
        lines2 = self.content2.splitlines(keepends=True)
        
        diff = difflib.unified_diff(
            lines1, lines2,
            fromfile=self.file1_path or "File 1",
            tofile=self.file2_path or "File 2",
            lineterm=''
        )
        
        # Format diff with colors
        html_lines = ['<pre style="margin: 0; padding: 0;">']
        additions = 0
        deletions = 0
        
        for line in diff:
            line = line.rstrip()
            if line.startswith('+++') or line.startswith('---'):
                html_lines.append(f'<span style="color: {COLORS["text_secondary"]}; font-weight: bold;">{line}</span>')
            elif line.startswith('@@'):
                html_lines.append(f'<span style="color: {COLORS["accent_cyan"]}; font-weight: bold;">{line}</span>')
            elif line.startswith('+'):
                additions += 1
                html_lines.append(f'<span style="background-color: #1a3a1a; color: {COLORS["accent_green"]};">{line}</span>')
            elif line.startswith('-'):
                deletions += 1
                html_lines.append(f'<span style="background-color: #3a1a1a; color: {COLORS["accent_red"]};">{line}</span>')
            else:
                html_lines.append(f'<span style="color: {COLORS["text_secondary"]};">{line}</span>')
        
        html_lines.append('</pre>')
        
        if additions == 0 and deletions == 0:
            self.diff_display.setHtml(f'<p style="color: {COLORS["accent_green"]}; font-size: 14px; text-align: center; padding: 20px;">✓ Files are identical</p>')
            self.stats_label.setText("No differences found")
        else:
            self.diff_display.setHtml('\n'.join(html_lines))
            self.stats_label.setText(f"Changes: +{additions} additions, -{deletions} deletions")

