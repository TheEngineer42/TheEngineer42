#tkinter = Tk interface
#Tk = tool kit


import tkinter as tk # - importing  tkinter MODULE and giving it tk alias 
                     #   for convenience
                     # - this module used to create GUIs
                     #   (Graphical User Interfaces)
                
 
root = tk.Tk() # - root(or any other name) is the main or top lvl window of
               #   our application. Container for all other widgets(labels,
               #   buttons,etc.)
               # - tk.Tk() class that creates main window. kinda when calling it creates and actual window
               # - Tk means toolkit
root.geometry() # setting size of the main application windwow

label = tk.Label(root, text = 'Hello World')
                # - label(or any other name) = is the variable we use to
                #   reference the Label widget we've created
                # - tk.Label = class provided by Tkinter to create a Label widget
                # - .Label(root, text = ...) root specifies that this label will 
                #   appear in root window


label.pack() # - method used to arrange/pack widget into the window
             # - geometry manager that tell Tkinter how to position the 
             #   widget inside its parent(root here)
             # - withouth calling geometry manager(pack, grid or place)
             #   the widget wont be displayed

                 
root.mainloop() # - starts the event loop of the Tkinter application  
                # - this loop keepss the application running, waiting 
                #   for user's intereactions(clicking, typing)         
                # - without mainloop(), the GUI window would open and immediately
                #   close because the program would terminate