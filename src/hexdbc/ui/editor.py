"""
Custom syntax highlighter for .hexdbc files.

Uses QScintilla for advanced code editing features.
"""

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont, QFontDatabase
from PySide6.QtWidgets import QWidget

try:
    # Disable QScintilla - it requires PyQt5/6 which conflicts with PySide6
    # To re-enable, install a PySide6-compatible QScintilla and uncomment below
    # from PyQt6.Qsci import QsciScintilla, QsciLexerCustom
    raise ImportError("QScintilla disabled - using PySide6 fallback")
    QSCI_AVAILABLE = True
except ImportError:
    try:
        # from PyQt5.Qsci import QsciScintilla, QsciLexerCustom
        raise ImportError("QScintilla disabled - using PySide6 fallback")
        QSCI_AVAILABLE = True
    except ImportError:
        QSCI_AVAILABLE = False

from hexdbc.ui.theme import get_editor_colors, COLORS


if QSCI_AVAILABLE:
    class HexDBCLexer(QsciLexerCustom):
        """Custom lexer for .hexdbc syntax highlighting."""
        
        # Token styles
        STYLE_DEFAULT = 0
        STYLE_COMMENT = 1
        STYLE_KEYWORD = 2
        STYLE_STRING = 3
        STYLE_NUMBER = 4
        STYLE_FUNCTION = 5
        STYLE_VARIABLE = 6
        STYLE_OPERATOR = 7
        STYLE_TYPE = 8  # Enums and types
        STYLE_DIRECTIVE = 9  # @schema etc
        
        KEYWORDS = {'true', 'false', 'null', 'nil'}
        
        def __init__(self, parent=None):
            super().__init__(parent)
            self._init_styles()
        
        def _init_styles(self):
            """Initialize syntax highlighting styles."""
            colors = get_editor_colors()
            
            # Get a good monospace font
            font = QFont("JetBrains Mono", 11)
            if not QFontDatabase.hasFamily("JetBrains Mono"):
                for family in ["Cascadia Code", "Fira Code", "Consolas", "Courier New"]:
                    if QFontDatabase.hasFamily(family):
                        font = QFont(family, 11)
                        break
            
            # Default style
            self.setDefaultColor(QColor(colors['text']))
            self.setDefaultPaper(QColor(colors['paper']))
            self.setDefaultFont(font)
            
            # Comment style (#)
            self.setColor(QColor(colors['comment']), self.STYLE_COMMENT)
            self.setFont(font, self.STYLE_COMMENT)
            
            # Keyword style
            self.setColor(QColor(colors['keyword']), self.STYLE_KEYWORD)
            bold_font = QFont(font)
            bold_font.setBold(True)
            self.setFont(bold_font, self.STYLE_KEYWORD)
            
            # String style
            self.setColor(QColor(colors['string']), self.STYLE_STRING)
            self.setFont(font, self.STYLE_STRING)
            
            # Number style
            self.setColor(QColor(colors['number']), self.STYLE_NUMBER)
            self.setFont(font, self.STYLE_NUMBER)
            
            # Function/record name style
            self.setColor(QColor(colors['function']), self.STYLE_FUNCTION)
            self.setFont(bold_font, self.STYLE_FUNCTION)
            
            # Variable/field name style
            self.setColor(QColor(colors['variable']), self.STYLE_VARIABLE)
            self.setFont(font, self.STYLE_VARIABLE)
            
            # Operator style
            self.setColor(QColor(colors['operator']), self.STYLE_OPERATOR)
            self.setFont(font, self.STYLE_OPERATOR)
            
            # Type/enum style
            self.setColor(QColor(colors['type']), self.STYLE_TYPE)
            self.setFont(bold_font, self.STYLE_TYPE)
            
            # Directive style (@schema)
            self.setColor(QColor(COLORS['accent_purple']), self.STYLE_DIRECTIVE)
            self.setFont(bold_font, self.STYLE_DIRECTIVE)
        
        def language(self):
            return "HexDBC"
        
        def description(self, style):
            styles = {
                self.STYLE_DEFAULT: "Default",
                self.STYLE_COMMENT: "Comment",
                self.STYLE_KEYWORD: "Keyword",
                self.STYLE_STRING: "String",
                self.STYLE_NUMBER: "Number",
                self.STYLE_FUNCTION: "Function",
                self.STYLE_VARIABLE: "Variable",
                self.STYLE_OPERATOR: "Operator",
                self.STYLE_TYPE: "Type/Enum",
                self.STYLE_DIRECTIVE: "Directive",
            }
            return styles.get(style, "Unknown")
        
        def styleText(self, start, end):
            """Apply syntax highlighting to the text."""
            if not self.editor():
                return
            
            # Get text to style
            text = self.editor().text()[start:end]
            
            self.startStyling(start)
            
            i = 0
            while i < len(text):
                char = text[i]
                
                # Comment
                if char == '#':
                    # Find end of line
                    eol = text.find('\n', i)
                    if eol == -1:
                        eol = len(text)
                    self.setStyling(eol - i, self.STYLE_COMMENT)
                    i = eol
                    continue
                
                # String
                if char == '"':
                    end_quote = i + 1
                    while end_quote < len(text):
                        if text[end_quote] == '"' and text[end_quote - 1] != '\\':
                            break
                        end_quote += 1
                    length = end_quote - i + 1
                    self.setStyling(length, self.STYLE_STRING)
                    i = end_quote + 1
                    continue
                
                # Directive (@schema)
                if char == '@':
                    end_word = i + 1
                    while end_word < len(text) and text[end_word].isalnum():
                        end_word += 1
                    self.setStyling(end_word - i, self.STYLE_DIRECTIVE)
                    i = end_word
                    continue
                
                # Number (including hex)
                if char.isdigit() or (char == '-' and i + 1 < len(text) and text[i + 1].isdigit()):
                    end_num = i + 1 if char == '-' else i
                    # Check for hex
                    if end_num + 1 < len(text) and text[end_num:end_num + 2].lower() == '0x':
                        end_num += 2
                        while end_num < len(text) and text[end_num] in '0123456789abcdefABCDEF':
                            end_num += 1
                    else:
                        while end_num < len(text) and (text[end_num].isdigit() or text[end_num] == '.'):
                            end_num += 1
                        # Scientific notation
                        if end_num < len(text) and text[end_num] in 'eE':
                            end_num += 1
                            if end_num < len(text) and text[end_num] in '+-':
                                end_num += 1
                            while end_num < len(text) and text[end_num].isdigit():
                                end_num += 1
                    self.setStyling(end_num - i, self.STYLE_NUMBER)
                    i = end_num
                    continue
                
                # Identifier
                if char.isalpha() or char == '_':
                    end_word = i
                    while end_word < len(text) and (text[end_word].isalnum() or text[end_word] == '_'):
                        end_word += 1
                    word = text[i:end_word]
                    
                    # Check if it's a function call (followed by '(')
                    remaining = text[end_word:].lstrip()
                    if remaining.startswith('('):
                        self.setStyling(end_word - i, self.STYLE_FUNCTION)
                    # Check if it's an enum/constant (all uppercase)
                    elif word.isupper() or (word[0].isupper() and '_' in word):
                        self.setStyling(end_word - i, self.STYLE_TYPE)
                    # Check if it's a keyword
                    elif word.lower() in self.KEYWORDS:
                        self.setStyling(end_word - i, self.STYLE_KEYWORD)
                    # Check if it's followed by '=' (field name)
                    elif '=' in remaining.split('\n')[0][:10]:
                        self.setStyling(end_word - i, self.STYLE_VARIABLE)
                    else:
                        self.setStyling(end_word - i, self.STYLE_DEFAULT)
                    
                    i = end_word
                    continue
                
                # Operators
                if char in '={}(),':
                    self.setStyling(1, self.STYLE_OPERATOR)
                    i += 1
                    continue
                
                # Default
                self.setStyling(1, self.STYLE_DEFAULT)
                i += 1


class CodeEditor(QsciScintilla if QSCI_AVAILABLE else QWidget):
    """Enhanced code editor with syntax highlighting."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        if not QSCI_AVAILABLE:
            return
        
        self._setup_editor()
        self._setup_margins()
        self._setup_lexer()
    
    def _setup_editor(self):
        """Configure editor settings."""
        colors = get_editor_colors()
        
        # Get a good monospace font
        font = QFont("JetBrains Mono", 11)
        if not QFontDatabase.hasFamily("JetBrains Mono"):
            for family in ["Cascadia Code", "Fira Code", "Consolas", "Courier New"]:
                if QFontDatabase.hasFamily(family):
                    font = QFont(family, 11)
                    break
        
        self.setFont(font)
        
        # Colors
        self.setPaper(QColor(colors['paper']))
        self.setColor(QColor(colors['text']))
        
        # Current line highlighting
        self.setCaretLineVisible(True)
        self.setCaretLineBackgroundColor(QColor(colors['current_line']))
        self.setCaretForegroundColor(QColor(colors['text']))
        self.setCaretWidth(2)
        
        # Selection
        self.setSelectionBackgroundColor(QColor(colors['selection']))
        
        # Brace matching
        self.setBraceMatching(QsciScintilla.BraceMatch.SloppyBraceMatch)
        self.setMatchedBraceBackgroundColor(QColor(colors['matching_bracket']))
        self.setMatchedBraceForegroundColor(QColor(COLORS['bg_primary']))
        
        # Indentation
        self.setIndentationsUseTabs(False)
        self.setTabWidth(4)
        self.setAutoIndent(True)
        self.setIndentationGuides(True)
        self.setIndentationGuidesBackgroundColor(QColor(COLORS['border_secondary']))
        self.setIndentationGuidesForegroundColor(QColor(COLORS['border_primary']))
        
        # Edge line (column guide)
        self.setEdgeMode(QsciScintilla.EdgeMode.EdgeLine)
        self.setEdgeColumn(100)
        self.setEdgeColor(QColor(COLORS['border_secondary']))
        
        # Code folding
        self.setFolding(QsciScintilla.FoldStyle.BoxedTreeFoldStyle)
        self.setFoldMarginColors(QColor(colors['margin_bg']), QColor(colors['margin_bg']))
        
        # Auto-completion
        self.setAutoCompletionSource(QsciScintilla.AutoCompletionSource.AcsAll)
        self.setAutoCompletionThreshold(2)
        self.setAutoCompletionCaseSensitivity(False)
        
        # Word wrap
        self.setWrapMode(QsciScintilla.WrapMode.WrapNone)
        
        # Scrollbar
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
    
    def _setup_margins(self):
        """Configure editor margins (line numbers, etc.)."""
        colors = get_editor_colors()
        
        # Line numbers margin
        self.setMarginType(0, QsciScintilla.MarginType.NumberMargin)
        self.setMarginWidth(0, "00000")
        self.setMarginsForegroundColor(QColor(colors['margin_text']))
        self.setMarginsBackgroundColor(QColor(colors['margin_bg']))
        self.setMarginsFont(self.font())
        
        # Folding margin
        self.setMarginType(2, QsciScintilla.MarginType.SymbolMargin)
        self.setMarginWidth(2, 16)
        self.setMarginSensitivity(2, True)
    
    def _setup_lexer(self):
        """Set up the HexDBC syntax highlighter."""
        lexer = HexDBCLexer(self)
        self.setLexer(lexer)
    
    def set_text(self, text: str):
        """Set editor text content."""
        self.setText(text)
    
    def get_text(self) -> str:
        """Get editor text content."""
        return self.text()
    
    def scroll_to_line(self, line: int):
        """Scroll to make the specified line visible and position cursor there."""
        # Set cursor position (0-indexed line)
        self.setCursorPosition(line, 0)
        # Ensure this line is visible in the viewport
        self.ensureCursorVisible()
        # Also use SendScintilla for more reliable scrolling
        self.SendScintilla(QsciScintilla.SCI_GOTOLINE, line)


# Fallback plain text editor if QScintilla is not available
if not QSCI_AVAILABLE:
    from PySide6.QtWidgets import QPlainTextEdit
    from PySide6.QtGui import QSyntaxHighlighter, QTextCharFormat
    import re
    
    class SimpleSyntaxHighlighter(QSyntaxHighlighter):
        """Simple syntax highlighter fallback for when QScintilla is unavailable."""
        
        def __init__(self, parent=None):
            super().__init__(parent)
            self._init_formats()
            self._init_rules()
        
        def _init_formats(self):
            colors = get_editor_colors()
            
            self.comment_format = QTextCharFormat()
            self.comment_format.setForeground(QColor(colors['comment']))
            
            self.string_format = QTextCharFormat()
            self.string_format.setForeground(QColor(colors['string']))
            
            self.number_format = QTextCharFormat()
            self.number_format.setForeground(QColor(colors['number']))
            
            self.keyword_format = QTextCharFormat()
            self.keyword_format.setForeground(QColor(colors['keyword']))
            self.keyword_format.setFontWeight(700)
            
            self.function_format = QTextCharFormat()
            self.function_format.setForeground(QColor(colors['function']))
            
            self.variable_format = QTextCharFormat()
            self.variable_format.setForeground(QColor(colors['variable']))
            
            self.type_format = QTextCharFormat()
            self.type_format.setForeground(QColor(colors['type']))
        
        def _init_rules(self):
            self.rules = [
                (re.compile(r'#.*'), self.comment_format),
                (re.compile(r'"[^"\\]*(\\.[^"\\]*)*"'), self.string_format),
                (re.compile(r'\b0x[0-9a-fA-F]+\b'), self.number_format),
                (re.compile(r'\b-?\d+\.?\d*\b'), self.number_format),
                (re.compile(r'\b[A-Z][A-Z0-9_]+\b'), self.type_format),
                (re.compile(r'\b\w+(?=\s*\()'), self.function_format),
                (re.compile(r'\b\w+(?=\s*=)'), self.variable_format),
                (re.compile(r'@\w+'), self.keyword_format),
            ]
        
        def highlightBlock(self, text):
            for pattern, fmt in self.rules:
                for match in pattern.finditer(text):
                    self.setFormat(match.start(), match.end() - match.start(), fmt)
    
    class CodeEditor(QPlainTextEdit):
        """Fallback plain text editor when QScintilla is unavailable."""
        
        # Signal for FK reference hover
        from PySide6.QtCore import Signal
        reference_hovered = Signal(str, str, int, object)  # (field_name, value_str, value_int, cursor_pos)
        reference_left = Signal()
        
        def __init__(self, parent=None):
            super().__init__(parent)
            
            self._dbc_name: str = ""  # Current DBC name for FK lookups
            self._hover_timer = None
            self._last_hover_field = None
            
            colors = get_editor_colors()
            
            font = QFont("Consolas", 11)
            self.setFont(font)
            
            self.setStyleSheet(f"""
                QPlainTextEdit {{
                    background-color: {colors['paper']};
                    color: {colors['text']};
                    border: none;
                    selection-background-color: {colors['selection']};
                }}
            """)
            
            self.highlighter = SimpleSyntaxHighlighter(self.document())
            
            # Enable mouse tracking for hover
            self.setMouseTracking(True)
            
            # Connect scroll to rehighlight visible content
            self.verticalScrollBar().valueChanged.connect(self._on_scroll)
        
        def set_dbc_name(self, name: str):
            """Set the current DBC name for FK lookups."""
            self._dbc_name = name
        
        def get_dbc_name(self) -> str:
            """Get the current DBC name."""
            return self._dbc_name
        
        def set_text(self, text: str):
            """Set text with deferred highlighting to prevent freeze on large files."""
            # Block signals to prevent highlighting during load
            self.highlighter.blockSignals(True)
            self.document().blockSignals(True)
            
            self.setPlainText(text)
            
            # Re-enable signals
            self.document().blockSignals(False)
            self.highlighter.blockSignals(False)
            
            # Schedule a deferred rehighlight for visible content only
            from PySide6.QtCore import QTimer
            QTimer.singleShot(100, self._deferred_rehighlight)
        
        def _deferred_rehighlight(self):
            """Rehighlight only visible blocks for performance."""
            # Get visible area
            first_visible = self.firstVisibleBlock()
            if not first_visible.isValid():
                return
            
            # Rehighlight visible blocks only (approx 50-100 lines)
            block = first_visible
            count = 0
            while block.isValid() and count < 100:
                self.highlighter.rehighlightBlock(block)
                block = block.next()
                count += 1
        
        def _on_scroll(self, value):
            """Rehighlight visible content when scrolling."""
            self._deferred_rehighlight()
        
        def get_text(self) -> str:
            return self.toPlainText()
        
        def append_text(self, text: str):
            """Append text at the end efficiently without re-processing entire document."""
            from PySide6.QtGui import QTextCursor
            cursor = self.textCursor()
            cursor.movePosition(QTextCursor.MoveOperation.End)
            cursor.insertText(text)
            self.setTextCursor(cursor)
            self.ensureCursorVisible()
        
        def scroll_to_line(self, line: int):
            """Scroll to make the specified line visible."""
            cursor = self.textCursor()
            block = self.document().findBlockByLineNumber(line)
            cursor.setPosition(block.position())
            self.setTextCursor(cursor)
            self.ensureCursorVisible()
        
        def mouseMoveEvent(self, event):
            """Handle mouse move to detect hover over FK values."""
            super().mouseMoveEvent(event)
            
            # Get position under cursor
            cursor = self.cursorForPosition(event.pos())
            
            # Get the line text
            block = cursor.block()
            line_text = block.text()
            
            # Parse for field = value pattern
            field_info = self._parse_field_at_cursor(line_text, cursor.positionInBlock())
            
            if field_info:
                field_name, value_str = field_info
                # Only trigger if this is a new hover
                if self._last_hover_field != (field_name, value_str):
                    self._last_hover_field = (field_name, value_str)
                    try:
                        value_int = int(value_str)
                        # Get global cursor position for tooltip placement
                        global_pos = self.mapToGlobal(event.pos())
                        self.reference_hovered.emit(field_name, value_str, value_int, global_pos)
                    except ValueError:
                        pass
            else:
                if self._last_hover_field:
                    self._last_hover_field = None
                    self.reference_left.emit()
        
        def leaveEvent(self, event):
            """Handle mouse leaving the editor."""
            super().leaveEvent(event)
            if self._last_hover_field:
                self._last_hover_field = None
                self.reference_left.emit()
        
        def _parse_field_at_cursor(self, line_text: str, cursor_col: int):
            """
            Parse field = value at cursor position.
            
            Returns (field_name, value_str) if cursor is over a numeric value, else None.
            """
            import re
            
            # Skip comments
            if '#' in line_text:
                comment_start = line_text.index('#')
                if cursor_col >= comment_start:
                    return None
                line_text = line_text[:comment_start]
            
            # Find all field = value pairs
            # Pattern: identifier = number (not string)
            pattern = r'(\w+)\s*=\s*(-?\d+)'
            
            for match in re.finditer(pattern, line_text):
                start = match.start()
                end = match.end()
                
                # Check if cursor is within this match (specifically over the value part)
                value_start = match.start(2)  # Start of the number
                value_end = match.end(2)
                
                if value_start <= cursor_col <= value_end:
                    field_name = match.group(1)
                    value_str = match.group(2)
                    return (field_name, value_str)
            
            return None

