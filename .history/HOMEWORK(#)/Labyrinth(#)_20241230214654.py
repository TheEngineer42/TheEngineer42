from tkinter import*
root = Tk()
root.geometry('700x700')
import random

canvas = Canvas(root, height = 500, width = 500, bg = 'skyblue')
canvas.pack(expand = 1)# same as expand = True



for i in range(0,520,20):
    canvas.create_line(i,0,i,500)
    canvas.create_line(0,i,500,i)

#drawing borders manually because they are not visible
canvas.create_line(2,0,2,500)
canvas.create_line(0,2,500,2)

#extracting horizontal pieces
for _ in range(500):
    n = random.randrange(0,521,20)
    m = random.randrange(0,521,20) 
    canvas.create_line(n+1,m,n+20,m, fill = 'skyblue') #n+1 so that other lines are not damaged

#extracting vertical pieces
for _ in range(500):
    k = random.randrange(0,521,20)
    l = random.randrange(0,521,20) 
    canvas.create_line(l,k+1,l,k+20, fill = 'skyblue')

    # Add a movable character
character = canvas.create_oval(entrance[0] * cell_size + 5, entrance[1] * cell_size + 5,
                                entrance[0] * cell_size + cell_size - 5, entrance[1] * cell_size + cell_size - 5,
                                fill='blue')
current_position = entrance

# Move character function
def move_character(event):
    global current_position
    x, y = current_position

    # Determine the new position based on the key press
    if event.keysym == "Up" and y > 0:
        new_position = (x, y - 1)
    elif event.keysym == "Down" and y < grid_size - 1:
        new_position = (x, y + 1)
    elif event.keysym == "Left" and x > 0:
        new_position = (x - 1, y)
    elif event.keysym == "Right" and x < grid_size - 1:
        new_position = (x + 1, y)
    else:
        new_position = current_position

    # Check if the new position is part of the path
    if new_position in path:
        # Update the character's position
        canvas.move(character, (new_position[0] - x) * cell_size, (new_position[1] - y) * cell_size)
        current_position = new_position

        # Check if the player has reached the exit
        if new_position == exit:
            canvas.create_text(250, 250, text="You Win!", font=("Arial", 24), fill="green")

# Bind arrow keys to move the character
root.bind("<Up>", move_character)
root.bind("<Down>", move_character)
root.bind("<Left>", move_character)
root.bind("<Right>", move_character)

root.mainloop()