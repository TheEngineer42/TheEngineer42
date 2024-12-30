"""
////////////////////////////////////////////
///////////////////EXPAND///////////////////
////////////////////////////////////////////


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

              

"""

from tkinter import*

root = Tk()
root.geometry('500x500')

canvas = Canvas(root, height=200, width=200, bg='skyblue')
#canvas.pack() ---------------> # No expand, no fill
canvas.pack(expand = 1)

root.mainloop()