"""
Reference Tooltip Widget for DBC cross-references.

Shows a popup with referenced entry data on hover/click.
"""

from typing import Optional, Callable

from PySide6.QtCore import Qt, QTimer, QPoint, Signal
from PySide6.QtWidgets import (
    QFrame, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QWidget, QApplication
)
from PySide6.QtGui import QFont, QCursor

from hexdbc.ui.theme import COLORS


class ReferenceTooltip(QFrame):
    """
    Tooltip popup showing referenced DBC entry data.
    
    Features:
    - Shows target DBC name and entry ID
    - Shows key fields from the referenced entry
    - "Go to" button to navigate to the target DBC
    """
    
    # Signal emitted when user wants to navigate to reference
    navigate_requested = Signal(str, int)  # (dbc_name, entry_id)
    
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent, Qt.WindowType.ToolTip | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_ShowWithoutActivating)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        
        self._target_dbc: str = ""
        self._target_id: int = 0
        self._hide_timer = QTimer(self)
        self._hide_timer.setSingleShot(True)
        self._hide_timer.timeout.connect(self.hide)
        
        self._init_ui()
    
    def _init_ui(self):
        """Initialize the tooltip UI."""
        self.setStyleSheet(f"""
            ReferenceTooltip {{
                background-color: {COLORS['bg_tertiary']};
                border: 1px solid {COLORS['accent_blue']};
                border-radius: 6px;
                padding: 8px;
            }}
        """)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 8, 10, 8)
        layout.setSpacing(6)
        
        # Header with DBC name and ID
        header_layout = QHBoxLayout()
        header_layout.setSpacing(8)
        
        self.title_label = QLabel()
        self.title_label.setStyleSheet(f"""
            color: {COLORS['accent_blue']};
            font-weight: bold;
            font-size: 12px;
        """)
        header_layout.addWidget(self.title_label)
        
        header_layout.addStretch()
        
        # Go to button
        self.goto_btn = QPushButton("Go →")
        self.goto_btn.setFixedSize(70, 24)
        self.goto_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.goto_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {COLORS['accent_blue']};
                color: white;
                border: none;
                border-radius: 4px;
                font-size: 11px;
                font-weight: bold;
                padding: 0 8px;
            }}
            QPushButton:hover {{
                background-color: {COLORS['accent_cyan']};
            }}
        """)
        self.goto_btn.clicked.connect(self._on_goto_clicked)
        header_layout.addWidget(self.goto_btn)
        
        layout.addLayout(header_layout)
        
        # Content area for entry fields
        self.content_label = QLabel()
        self.content_label.setStyleSheet(f"""
            color: {COLORS['text_secondary']};
            font-family: Consolas, monospace;
            font-size: 11px;
        """)
        self.content_label.setWordWrap(True)
        layout.addWidget(self.content_label)
        
        # Status label for errors
        self.status_label = QLabel()
        self.status_label.setStyleSheet(f"""
            color: {COLORS['text_disabled']};
            font-style: italic;
            font-size: 11px;
        """)
        self.status_label.hide()
        layout.addWidget(self.status_label)
        
        self.setMinimumWidth(280)
        self.setMaximumWidth(400)
    
    def show_reference(
        self,
        source_dbc: str,
        field_name: str,
        value: int,
        target_dbc: str,
        entry_preview: Optional[str],
        position: QPoint
    ):
        """
        Show the tooltip with reference data.
        
        Args:
            source_dbc: Source DBC name
            field_name: Field containing the reference
            value: The FK value
            target_dbc: Target DBC being referenced
            entry_preview: Preview text of the entry, or None if not available
            position: Screen position to show at
        """
        self._target_dbc = target_dbc
        self._target_id = value
        
        # Update title
        self.title_label.setText(f"→ {target_dbc}.dbc  ID: {value}")
        
        # Update content
        if entry_preview:
            self.content_label.setText(entry_preview)
            self.content_label.show()
            self.status_label.hide()
            self.goto_btn.setEnabled(True)
        else:
            self.content_label.hide()
            self.status_label.setText(f"{target_dbc}.dbc not available in folder")
            self.status_label.show()
            self.goto_btn.setEnabled(False)
        
        # Position and show
        self.adjustSize()
        self.move(position)
        self.show()
        
        # Cancel any pending hide
        self._hide_timer.stop()
    
    def show_at_cursor(
        self,
        source_dbc: str,
        field_name: str,
        value: int,
        target_dbc: str,
        entry_preview: Optional[str]
    ):
        """Show tooltip near the cursor position."""
        cursor_pos = QCursor.pos()
        # Offset slightly so tooltip doesn't cover cursor
        position = cursor_pos + QPoint(15, 15)
        
        # Ensure tooltip stays on screen
        screen = QApplication.primaryScreen()
        if screen:
            screen_rect = screen.availableGeometry()
            if position.x() + self.width() > screen_rect.right():
                position.setX(cursor_pos.x() - self.width() - 10)
            if position.y() + self.height() > screen_rect.bottom():
                position.setY(cursor_pos.y() - self.height() - 10)
        
        self.show_reference(source_dbc, field_name, value, target_dbc, entry_preview, position)
    
    def schedule_hide(self, delay_ms: int = 300):
        """Schedule the tooltip to hide after a delay."""
        self._hide_timer.start(delay_ms)
    
    def cancel_hide(self):
        """Cancel a scheduled hide."""
        self._hide_timer.stop()
    
    def _on_goto_clicked(self):
        """Handle Go button click."""
        if self._target_dbc and self._target_id:
            self.navigate_requested.emit(self._target_dbc, self._target_id)
            self.hide()
    
    def enterEvent(self, event):
        """Cancel hide when mouse enters tooltip."""
        self.cancel_hide()
        super().enterEvent(event)
    
    def leaveEvent(self, event):
        """Schedule hide when mouse leaves tooltip."""
        self.schedule_hide()
        super().leaveEvent(event)
