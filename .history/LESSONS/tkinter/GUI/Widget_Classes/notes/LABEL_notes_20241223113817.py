"""
Tkinter Label

- widget is a spatial container - rectangular area that can
  contain other widgets. However unlike Frame widget, the 
  Label Frame allows you to display a label as part of the 
  border around the area. 

"""
"""

text             - Sets the text to be displayed inside the 
                   Label widget

anchor           - Determines where the text (or image) will 
                   be placed within the Label widget.
                 - values: "N","NW","SW","SE","NE","W","S","E"

bg(background)   - Sets the background color of the Label 
                   widget

bitmap           - Displays a bitmap image in the Label instead
                   of regular text. You can use predefined 
                   bitmaps such as "error", "info", "warning"

bd (borderwidth) - Defines the width of the border surrounding 
                   the Label widget

cursor           - Specifies the type of mouse cursor to 
                   display when hovering over the Label widget.
                   Common values are "arrow", "hand2", "cross"
                  
font             - specifies the font style, size, and family
                   of the text on the button. For example:
                   'Arial 12 bold'

Fg(foreground)   - the normal color of the text or content of
                   the button

height           - specifies the height of the button in terms
                   of text lines(if the button contains) or
                   pixels(if an image is used). Value '1'
                   corresponds to the height of a single line
                   of text

width            - specifies the width of the button in terms
                   of characters (for text) or pixels (for
                   images). A value of 10 means the width will
                   be wide enough to fit 10 characters of text.

image            - Displays an image on the Label widget instead
                   of text

justify          - Controls the alignment of multiple lines of 
                   text with in the Label. The possible values
                   are "left", "right", "center"

"""