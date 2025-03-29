from tkinter import *
import random

root = Tk()
root.geometry('500x600')
canvas = Canvas(root, bg='white', height=500, width=500)
canvas.pack()

colors = ['green', 'light green', 'dark green']
grass_blades = []

# Initial grass creation
for i in range(0, 500, 10):
    y = random.randrange(100, 500)  # Prevent grass from being too short
    c = random.choice(colors)
    canvas.create_rectangle(i, y, i + 10, 500, fill=c, outline="")
    grass_blades.append((i, y, c))

frame = Frame(root)
frame.pack()


# ✅ Fix: Growing now correctly increases height each time the button is pressed
def growing():
    global grass_blades
    canvas.delete('all')

    new_grass = []
    for i, y, c in grass_blades:
        y_new = max(y - 10, 50)  # Stop growing if it reaches 50
        canvas.create_rectangle(i, y_new, i + 10, 500, fill=c, outline="")
        new_grass.append((i, y_new, c))

    grass_blades = new_grass  # Update the grass list


# ✅ Fix: Cutting now properly removes grass above a certain height but doesn't delete everything
def cutting():
    global grass_blades
    canvas.delete('all')

    new_grass = []
    for i, y, c in grass_blades:
        if y > 50:  # Only cut grass that is taller than 50 pixels
            y_new = 50  # Shorten it to 50 pixels
        else:
            y_new = y  # Keep the same height

        canvas.create_rectangle(i, y_new, i + 10, 500, fill=c, outline="")
        new_grass.append((i, y_new, c))  # Save updated grass height

    grass_blades = new_grass  # Update the grass list


# Buttons
grow = Button(frame, text="Grow", font=("Calibri", 14), command=growing)
grow.pack(side="left", padx=10, pady=10)

cut = Button(frame, text="Cut", font=("Calibri", 14), command=cutting)
cut.pack(side="right", padx=10, pady=10)

root.mainloop()
