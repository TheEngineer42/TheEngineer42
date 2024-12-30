"""
Tkinter BUTTON

- the Button widget is used to add buttons in a Python application.
  These buttons can display tex or images that convey the 
  purpose of the buttons. You can attach a function or a method
  to a button which is called automatically when you click the
  button
"""

#Syntax:
# w = Button(master, option = value, option = value,... )
# master - represents the parent window



"""
////////////////////////////////////////////////////////////////
///////////////OPTIONS:///////////////////////////////////////// 
////////////////////////////////////////////////////////////////

..............TEXT AND FONT OPTIONS -->..............

text             - sets the label on the button, typically as
                   a string of characters. Visible text that
                   tells a user what the button dos. If not
                   specified, the button will not display
                   any text

Font             - specifies the font style, size, and family
                   of the text on the button. For example:
                   'Arial 12 bold'

Underline        - specifies the index of the character in the
                   buttons text that should be underlined, e.g.
                   underline = 0, will underline the first
                   character. By default = -1, which means that
                   none character will be underlined. 
                   Underlines only one character.  


................APPEARANCE OPTIONS -->..................

Activebackground - the background color of the button when it
                   it is active(e.g., while being clicked or
                   hovered over)

Activeforeground - the foreground(text or content) color of the 
                   button when its active

Bg(background)   - the normal background color of the button

Fg(foreground)   - the normal color of the text or content of
                   the button

Bd(borderwidth)  - specifies the width of the buttons border in
                   pixels. By default = -2



........................SIZE -->..............................

Height           - specifies the height of the button in terms
                   of text lines(if the button contains) or
                   pixels(if an image is used). Value '1'
                   corresponds to the height of a single line
                   of text

Width            - specifies the width of the button in terms
                   of characters (for text) or pixels (for
                   images). A value of 10 means the width will
                   be wide enough to fit 10 characters of text.




.........................FUNCTIONALITY -->.....................

Command          - a callback function that is executed when 
                   clicked, e.g., command = my_function

              
..............................CONTENT -->......................
??? Image        - allows you to display an image on the
                   button instead of text. The value should be
                   an image object



////////////////////////////////////////////////////////////////
///////////////METHODS://///////////////////////////////////////
////////////////////////////////////////////////////////////////

flash()          - temporarily changes the appearance of the
                   button(like a quick flash) to indicate it
                   was clicked or intercted with
                 - purely visual, does not trigger any action
                 - causes the button to flash bwtween the 
                   active and normal colors several times. 
                   Leaves the button in its original state. 
                   Ignored if the button is disabled.  

invoke()???      - programmatically 'clicks' the button,
                   triggering the action bout to button's
                   command option.
                 - e.g., if the button is linked to a fucntion,
                   calling invoke() will execute the function
"""


