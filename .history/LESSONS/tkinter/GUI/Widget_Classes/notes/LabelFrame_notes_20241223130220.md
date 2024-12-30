# <p style = "color: Blue;"> Tkinter LabelFrame </p>

- widget class is like the **Frame widget** 
- a spatial container - a rectangular area that can contain other
  widgets
- unlike the **Frame widget**, the **LabelFrame** widget allows 
  you to display a **label** as part of the border around the area


 ## <p style = "color: CornFlowerBlue;">Syntax:</p>

w = LabelFrame(master, option = value, option = value,... )
master - represents the parent window



## <p style = "color: CornFlowerBlue;">OPTIONS:</p>


### <p style = "color: CornFlowerBlue;">TEXT AND FONT OPTIONS -->

text- Text of the label

Fg(foreground)   - the normal color of the text

### <p style = "color: CornFlowerBlue;">APPEARANCE -->

bg(background)   - The background color to be displayed inside the widget

bd(borderwidth)  - Width of the border drawn around the perimeter of the widget. The default value is 2 pixels

cursor           - Specifies the type of mouse cursor to 
                   display when hovering over the LabelFrame.
                   Common values are "arrow", "hand2", "cross"

relief - This option controls the appearance of the border around the outside of the widget. The default style is tk.GROOVE

height - The vertical dimension of the new frame

width	- The horizontal dimension of the new frame

### <p style = "color: CornFlowerBlue;">FOCUS BEHAVIOR -->

highlightbackground	- Color of the focus highlight when the widget does not have focus.

highlightcolor - The color of the focus highlight when the widget has focus.

highlightthickness - Thickness of the focus highlight.

### <p style = "color: CornFlowerBlue;">LAYOUT AND POSITIONING -->

padx- Use this option to add additional padding inside the left and right sides of the widget's frame. The value is in pixels.

pady	- Use this option to add additional padding inside the top and bottom of the widget's frame. The value is in pixels.

labelanchor	- Use this option to specify the position of the label on the widget's border. The default position is 'nw', which places the label at the left end of the top border.

For the nine possible label positions, refer to this diagram:
![diagram](/IMAGES\LabelFrame_diagram.png) 




















 





