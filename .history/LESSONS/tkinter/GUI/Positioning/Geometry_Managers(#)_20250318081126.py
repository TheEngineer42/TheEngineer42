import tkinter as tk

root = tk.Tk()
root.geometry('500x500')

# Create a canvas as the base layer
canvas = tk.Canvas(root, width=300, height=200, bg="blue")
canvas.place(x=0, y=0)  # Place at the top-left corner

# Add a label on top of the canvas
label = tk.Label(root, text="Hello, World!", bg="yellow", font=("Arial", 16))
label.place(x=100, y=200)  # Place at the desired position

root.mainloop()