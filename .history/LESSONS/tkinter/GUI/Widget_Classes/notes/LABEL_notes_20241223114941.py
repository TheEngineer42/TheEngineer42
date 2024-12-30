"""
Tkinter Label

- This widget implements a display box where you can place text
  images. The text displayed by this widget can be updated at 
  time you want

"""
#Syntax:
# w = Label(master, option = value, option = value,... )
# master - represents the parent window



"""
////////////////////////////////////////////////////////////////
///////////////OPTIONS:///////////////////////////////////////// 
////////////////////////////////////////////////////////////////

.................TEXT AND FONT OPTIONS -->....................
text             - Sets the text to be displayed inside the 
                   Label widget

Fg(foreground)   - the normal color of the text or content of
                   the button

font             - specifies the font style, size, and family
                   of the text on the button. For example:
                   'Arial 12 bold'

underline        - Specifies the index of the character to 
                   underline in the Label's text. It only 
                   underlines a single character.

.................APPEARANCE OPTIONS -->....................


bg(background)   - Sets the background color of the Label 
                   widget

justify          - Controls the alignment of multiple lines of 
                   text with in the Label. The possible values
                   are "left", "right", "center"

bitmap           - Displays a bitmap image in the Label instead
                   of regular text. You can use predefined 
                   bitmaps such as "error", "info", "warning",
                   "question"

bd (borderwidth) - Defines the width of the border surrounding 
                   the Label widget

cursor           - Specifies the type of mouse cursor to 
                   display when hovering over the Label widget.
                   Common values are "arrow", "hand2", "cross"
                  
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

wraplength       - Defines the maximum width (in pixels) of 
                   the text inside the Label. If the text 
                   exceeds this width, it will wrap to the 
                   next line      

                   
.........................PADDING OPTIONS -->...................

padx             - Adds horizontal padding inside the Label 
                   widget (space on the left and right of the 
                   content)

pady             - Adds vertical padding inside the Label widget
                   (space above and below the content).


.........................ANCHOR -->............................
anchor           - Determines where the text (or image) will 
                   be placed within the Label widget.
                 - values: "N","NW","SW","SE","NE","W","S","E"      

"""