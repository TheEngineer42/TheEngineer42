from tkinter import *

root = Tk()
root.geometry('500x500')

canvas = Canvas(root, width=500, height=500, bg='white')  # Added background color for clarity
canvas.pack()

for j in range(0, 10):
    # Using a simpler font and ensuring text is within visible area
    canvas.create_text(50, j * 50 + 20, text=str(j), fill='black', font=('Arial', 20))  # Adjusted font size and position

root.mainloop()
