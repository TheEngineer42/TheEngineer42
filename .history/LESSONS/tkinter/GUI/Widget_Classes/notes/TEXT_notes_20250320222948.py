"""
Tkinter Text Widget

- This widget allows the user to enter and edit multiline text.
  It can also be used to display formatted text and supports
  advanced features like tagging, undo, and scrolling.

#Syntax:
# w = Text(master, option = value, option = value,... )
# master - represents the parent window


////////////////////////////////////////////////////////////////
///////////////OPTIONS://///////////////////////////////////////
////////////////////////////////////////////////////////////////

.................TEXT AND FONT OPTIONS -->....................
text             - Initial text can be inserted using the insert()
                   method. No direct text option is available.

Fg(foreground)   - Sets the text color inside the Text widget.

font             - Specifies the font style, size, and family
                   of the text. Example: 'Arial 12 bold'.

undo             - Enables the undo feature for the Text widget
                   when set to True.

maxundo          - Specifies the maximum number of undo actions
                   that can be performed.

spacing1         - Sets the spacing above each line of text.

spacing2         - Controls the spacing between wrapped lines
                   of text inside a single paragraph.

spacing3         - Defines the spacing below each line of text.

..................APPEARANCE OPTIONS -->....................

bg(background)   - Sets the background color of the Text widget.

bd (borderwidth) - Defines the width of the border surrounding
                   the Text widget.

cursor           - Specifies the type of mouse cursor to display
                   when hovering over the Text widget.
                   Examples: "arrow", "hand2", "xterm".

height           - Specifies the height of the Text widget in terms
                   of number of text lines.

width            - Specifies the width of the Text widget in terms
                   of characters.

insertbackground - Defines the color of the text insertion cursor.

insertborderwidth - Specifies the width of the cursor border.

insertwidth      - Specifies the width of the insertion cursor.

relief           - Defines the type of border around the Text widget.
                 - Options: "flat", "raised", "sunken",
                   "groove", "ridge".

wrap             - Defines how text wrapping should occur.
                 - Options: "none" (no wrapping), "char" (wrap
                   at character level), "word" (wrap at word level).

..................PADDING OPTIONS -->....................

padx             - Adds horizontal padding inside the Text widget
                   (space on the left and right of the content).

pady             - Adds vertical padding inside the Text widget
                   (space above and below the content).

..................SCROLLING & SELECTION -->....................

yscrollcommand   - Used to connect a vertical scrollbar to the
                   Text widget.

xscrollcommand   - Used to connect a horizontal scrollbar to the
                   Text widget.

selectbackground - Defines the background color of selected text.

selectforeground - Defines the text color of selected text.

state            - Controls whether the Text widget is editable.
                 - Options: "normal" (editable), "disabled"
                   (read-only).

exportselection  - Determines whether the text selected in the
                   Text widget is also copied to the clipboard.

"""