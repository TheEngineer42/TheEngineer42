"""
///////////EXPAND//////////


EXPAND option - in Tkinters 'pack' geometry manager determines whether
                a widget should take up any extra space available in the
                parent container(like 'root' window or 'Frame')

expand = 0 --> (default) the widget does not request extra space in the 
               parent container. It only takes up the space required by
               its size and options like fill(if specified)
expand = 1 --> (expand = True) widget is 'allowed' into any extra space 
               available in the parent container. The extra space is 
               distributed equally among all widgets with expand = 1
           --> does not stretch widget itself, it determines how extra space
               in the parent container is allocated to the widget
           --> the extra space in container is evenly distributed around the 
               widget, effectively centering it within the available space

               
/////////FILL/////////////

FILL option - determines whether and how the widget stetches to fill
              the extra space allocated to it. Works with conjuction
              with 'expand', because 'expand' determines whether extra
              space is available. Fill determines how to use that space 

fill = 'None' - default

fill = 'x' - stretches the widget horizontally to fill the available space
             left and rigth

fill = 'y' - stretches the widget vertically to fill the available space
             above and below

fill = 'both' -  Stretches the widget both horizontally and vertically 
                 to fill all available space.        

"""

from tkinter import*

root = Tk()
root.geometry('500x500')

canvas = Canvas(root, height=200, width=200, bg='skyblue')
#canvas.pack()                               # No expand, no fill
canvas.pack(expand = 1)                     # Allows canvas to utilize extra space
#canvas.pack(expand=1, fill='both')          # Fills the entire available space#


root.mainloop()