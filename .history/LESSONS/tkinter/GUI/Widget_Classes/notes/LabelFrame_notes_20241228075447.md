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

<p><span style = "color: SkyBlue;">text</span> - Text of the label</p>

<p><span style = "color: SkyBlue;">Fg(foreground)</span> - the normal color of the text</p>

### <p style = "color: CornFlowerBlue;">APPEARANCE -->

<p><span style = "color: SkyBlue;">bg(background)</span> - The background color to be displayed inside the widget</p>

<p><span style = "color: SkyBlue;">bd(borderwidth)</span> - Width of the border drawn around the perimeter of the widget. The default value is 2 pixels</p>

<p><span style = "color: SkyBlue;">cursor</span> - Specifies the type of mouse cursor to display when hovering over the LabelFrame. Common values are "arrow", "hand2", "cross"</p>

<p><span style = "color: SkyBlue;">relief</span> - This option controls the appearance of the border around the outside of the widget. The default style is tk.GROOVE</p>

<p><span style = "color: SkyBlue;">height</span> - The vertical dimension of the new frame</p>

<p><span style = "color: SkyBlue;">width</span> - The horizontal dimension of the new frame</p>

### <p style = "color: CornFlowerBlue;">FOCUS BEHAVIOR -->

<p><span style = "color: SkyBlue;">highlightbackground</span> - Color of the focus highlight when the widget does not have focus.</p>

<p><span style = "color: SkyBlue;">highlightcolor</span> - The color of the focus highlight when the widget has focus.</p>

<p><span style = "color: SkyBlue;">highlightthickness</span> - Thickness of the focus highlight.</p>

### <p style = "color: CornFlowerBlue;">LAYOUT AND POSITIONING -->

<p><span style = "color: SkyBlue;">padx</span> - Use this option to add additional padding inside the left and right sides of the widget's frame. The value is in pixels.</p>

<p><span style = "color: SkyBlue;">pady</span> - Use this option to add additional padding inside the top and bottom of the widget's frame. The value is in pixels.</p>

<p><span style = "color: SkyBlue;">labelanchor</span> - Use this option to specify the position of the label on the widget's border. The default position is 'nw', which places the label at the left end of the top border.</p>


For the nine possible label positions, refer to this diagram:
![diagram](/IMAGES\LabelFrame_diagram.png) 




















 





