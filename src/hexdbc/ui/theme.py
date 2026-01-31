"""
Modern dark theme and styling for HexDBC.
"""

# Color palette - Premium modern dark theme
COLORS = {
    # Background colors - Richer, deeper tones
    'bg_primary': '#0A0E14',      # Main background (deeper dark)
    'bg_secondary': '#14181F',    # Panel/sidebar background
    'bg_tertiary': '#1F2430',     # Hover states, elevated surfaces
    'bg_input': '#0D1117',        # Input backgrounds
    
    # Border colors - More defined
    'border_primary': '#3D4450',  # Main borders (more visible)
    'border_secondary': '#252A35', # Subtle borders
    'border_focus': '#4FC3F7',    # Focused elements (brighter cyan-blue)
    
    # Text colors - Better contrast
    'text_primary': '#F0F4F8',    # Main text (brighter white)
    'text_secondary': '#9CA3AF',  # Secondary/muted text
    'text_disabled': '#4B5563',   # Disabled text
    'text_link': '#60A5FA',       # Links
    
    # Accent colors - More vibrant
    'accent_blue': '#4FC3F7',     # Primary accent (cyan-blue)
    'accent_green': '#4ADE80',    # Success (vibrant green)
    'accent_red': '#F87171',      # Error (softer red)
    'accent_orange': '#FB923C',   # Warning (vibrant orange)
    'accent_purple': '#C084FC',   # Special (vibrant purple)
    'accent_cyan': '#22D3EE',     # Info (bright cyan)
    
    # Syntax highlighting - Enhanced colors
    'syntax_keyword': '#FF6B9D',     # Keywords (pink-red)
    'syntax_string': '#95E1D3',      # Strings (mint green)
    'syntax_number': '#82AAFF',      # Numbers (sky blue)
    'syntax_comment': '#7E8B98',     # Comments (muted gray)
    'syntax_function': '#C792EA',    # Functions (purple)
    'syntax_variable': '#FFCB6B',    # Variables/fields (golden yellow)
    'syntax_operator': '#89DDFF',    # Operators (cyan)
    'syntax_type': '#C3E88D',        # Types/enums (lime green)
    
    # Editor specific
    'editor_bg': '#0A0E14',
    'editor_gutter': '#14181F',
    'editor_gutter_text': '#4B5563',
    'editor_selection': '#2D3748',
    'editor_current_line': '#14181F',
    'editor_matching_bracket': '#4ADE80',
}


def get_stylesheet() -> str:
    """Generate the main application stylesheet."""
    return f"""
        /* Main Window */
        QMainWindow {{
            background-color: {COLORS['bg_primary']};
            color: {COLORS['text_primary']};
        }}
        
        /* Menu Bar */
        QMenuBar {{
            background-color: {COLORS['bg_secondary']};
            color: {COLORS['text_primary']};
            border-bottom: 1px solid {COLORS['border_primary']};
            padding: 4px 8px;
            font-size: 13px;
        }}
        
        QMenuBar::item {{
            background-color: transparent;
            padding: 6px 12px;
            border-radius: 4px;
        }}
        
        QMenuBar::item:selected {{
            background-color: {COLORS['bg_tertiary']};
        }}
        
        QMenuBar::item:pressed {{
            background-color: {COLORS['accent_blue']};
        }}
        
        /* Menus */
        QMenu {{
            background-color: {COLORS['bg_secondary']};
            color: {COLORS['text_primary']};
            border: 1px solid {COLORS['border_primary']};
            border-radius: 6px;
            padding: 4px;
        }}
        
        QMenu::item {{
            padding: 8px 24px 8px 16px;
            border-radius: 4px;
        }}
        
        QMenu::item:selected {{
            background-color: {COLORS['accent_blue']};
        }}
        
        QMenu::separator {{
            height: 1px;
            background-color: {COLORS['border_primary']};
            margin: 4px 8px;
        }}
        
        /* Toolbar */
        QToolBar {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 {COLORS['bg_secondary']}, stop:1 #0F1318);
            border-bottom: 2px solid {COLORS['border_primary']};
            spacing: 8px;
            padding: 8px 16px;
        }}
        
        QToolButton {{
            background-color: transparent;
            color: {COLORS['text_primary']};
            border: 1px solid transparent;
            border-radius: 8px;
            padding: 10px 16px;
            font-size: 13px;
            font-weight: 600;
        }}
        
        QToolButton:hover {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 {COLORS['bg_tertiary']}, stop:1 #1A1F2C);
            border-color: {COLORS['border_primary']};
        }}
        
        QToolButton:pressed {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 {COLORS['accent_blue']}, stop:1 #3BA8D9);
            border-color: {COLORS['accent_blue']};
            color: white;
        }}
        
        /* Status Bar */
        QStatusBar {{
            background-color: {COLORS['bg_secondary']};
            color: {COLORS['text_secondary']};
            border-top: 1px solid {COLORS['border_primary']};
            font-size: 12px;
            padding: 4px;
        }}
        
        QStatusBar::item {{
            border: none;
        }}
        
        /* Labels */
        QLabel {{
            color: {COLORS['text_primary']};
        }}
        
        /* Push Buttons */
        QPushButton {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 {COLORS['bg_tertiary']}, stop:1 #1A1F2C);
            color: {COLORS['text_primary']};
            border: 1px solid {COLORS['border_primary']};
            border-radius: 8px;
            padding: 10px 18px;
            font-size: 13px;
            font-weight: 600;
        }}
        
        QPushButton:hover {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 #2A3040, stop:1 #1F2430);
            border-color: {COLORS['accent_blue']};
        }}
        
        QPushButton:pressed {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 {COLORS['accent_blue']}, stop:1 #3BA8D9);
            border-color: {COLORS['accent_blue']};
        }}
        
        QPushButton:disabled {{
            background-color: {COLORS['bg_secondary']};
            color: {COLORS['text_disabled']};
            border-color: {COLORS['border_secondary']};
        }}
        
        /* Primary Button Style */
        QPushButton[primary="true"] {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 {COLORS['accent_blue']}, stop:1 #3BA8D9);
            border-color: {COLORS['accent_blue']};
            color: white;
        }}
        
        QPushButton[primary="true"]:hover {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 #60D0FF, stop:1 {COLORS['accent_blue']});
        }}
        
        /* Line Edit */
        QLineEdit {{
            background-color: {COLORS['bg_input']};
            color: {COLORS['text_primary']};
            border: 2px solid {COLORS['border_primary']};
            border-radius: 8px;
            padding: 10px 14px;
            font-size: 13px;
            selection-background-color: {COLORS['editor_selection']};
        }}
        
        QLineEdit:focus {{
            border-color: {COLORS['border_focus']};
            background-color: #0F1318;
        }}
        
        QLineEdit:disabled {{
            background-color: {COLORS['bg_secondary']};
            color: {COLORS['text_disabled']};
        }}
        
        /* Text Edit */
        QTextEdit, QPlainTextEdit {{
            background-color: {COLORS['editor_bg']};
            color: {COLORS['text_primary']};
            border: 1px solid {COLORS['border_primary']};
            border-radius: 6px;
            font-family: 'JetBrains Mono', 'Cascadia Code', 'Fira Code', 'Consolas', monospace;
            font-size: 13px;
            selection-background-color: {COLORS['editor_selection']};
        }}
        
        /* Scrollbars */
        QScrollBar:vertical {{
            background-color: {COLORS['bg_primary']};
            width: 14px;
            margin: 0;
        }}
        
        QScrollBar::handle:vertical {{
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 {COLORS['border_primary']}, stop:1 #4A5568);
            border-radius: 7px;
            min-height: 30px;
            margin: 2px;
        }}
        
        QScrollBar::handle:vertical:hover {{
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 #4A5568, stop:1 {COLORS['text_secondary']});
        }}
        
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
            height: 0;
        }}
        
        QScrollBar:horizontal {{
            background-color: {COLORS['bg_primary']};
            height: 14px;
            margin: 0;
        }}
        
        QScrollBar::handle:horizontal {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 {COLORS['border_primary']}, stop:1 #4A5568);
            border-radius: 7px;
            min-width: 30px;
            margin: 2px;
        }}
        
        QScrollBar::handle:horizontal:hover {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 #4A5568, stop:1 {COLORS['text_secondary']});
        }}
        
        QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{
            width: 0;
        }}
        
        /* Tab Widget */
        QTabWidget::pane {{
            background-color: {COLORS['bg_primary']};
            border: 2px solid {COLORS['border_primary']};
            border-radius: 8px;
        }}
        
        QTabBar::tab {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 {COLORS['bg_secondary']}, stop:1 #0F1318);
            color: {COLORS['text_secondary']};
            border: none;
            padding: 12px 24px;
            margin-right: 2px;
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
            font-weight: 600;
        }}
        
        QTabBar::tab:selected {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 {COLORS['bg_primary']}, stop:1 {COLORS['bg_primary']});
            color: {COLORS['text_primary']};
            border-bottom: 3px solid {COLORS['accent_blue']};
        }}
        
        QTabBar::tab:hover:!selected {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 {COLORS['bg_tertiary']}, stop:1 #1A1F2C);
            color: {COLORS['text_primary']};
        }}
        
        /* Splitter */
        QSplitter::handle {{
            background-color: {COLORS['border_primary']};
        }}
        
        QSplitter::handle:horizontal {{
            width: 2px;
        }}
        
        QSplitter::handle:vertical {{
            height: 2px;
        }}
        
        /* Tree Widget */
        QTreeWidget, QTreeView {{
            background-color: {COLORS['bg_secondary']};
            color: {COLORS['text_primary']};
            border: 1px solid {COLORS['border_primary']};
            border-radius: 6px;
            outline: none;
        }}
        
        QTreeWidget::item, QTreeView::item {{
            padding: 6px 8px;
            border-radius: 4px;
        }}
        
        QTreeWidget::item:selected, QTreeView::item:selected {{
            background-color: {COLORS['accent_blue']};
        }}
        
        QTreeWidget::item:hover:!selected, QTreeView::item:hover:!selected {{
            background-color: {COLORS['bg_tertiary']};
        }}
        
        /* Dialog */
        QDialog {{
            background-color: {COLORS['bg_primary']};
            color: {COLORS['text_primary']};
        }}
        
        /* File Dialog */
        QFileDialog {{
            background-color: {COLORS['bg_primary']};
        }}
        
        /* Message Box */
        QMessageBox {{
            background-color: {COLORS['bg_primary']};
            color: {COLORS['text_primary']};
        }}
        
        /* Progress Bar */
        QProgressBar {{
            background-color: {COLORS['bg_tertiary']};
            border: none;
            border-radius: 4px;
            height: 8px;
            text-align: center;
        }}
        
        QProgressBar::chunk {{
            background-color: {COLORS['accent_blue']};
            border-radius: 4px;
        }}
        
        /* Tooltips */
        QToolTip {{
            background-color: {COLORS['bg_secondary']};
            color: {COLORS['text_primary']};
            border: 1px solid {COLORS['border_primary']};
            border-radius: 4px;
            padding: 4px 8px;
            font-size: 12px;
        }}
    """


def get_editor_colors() -> dict:
    """Get colors specifically for the code editor."""
    return {
        'paper': COLORS['editor_bg'],
        'text': COLORS['text_primary'],
        'margin_bg': COLORS['editor_gutter'],
        'margin_text': COLORS['editor_gutter_text'],
        'selection': COLORS['editor_selection'],
        'current_line': COLORS['editor_current_line'],
        'matching_bracket': COLORS['editor_matching_bracket'],
        
        # Syntax colors
        'keyword': COLORS['syntax_keyword'],
        'string': COLORS['syntax_string'],
        'number': COLORS['syntax_number'],
        'comment': COLORS['syntax_comment'],
        'function': COLORS['syntax_function'],
        'variable': COLORS['syntax_variable'],
        'operator': COLORS['syntax_operator'],
        'type': COLORS['syntax_type'],
    }
