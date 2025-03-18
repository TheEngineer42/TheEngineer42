from tkinter import *
import random

# Set up the canvas
root = Tk()
root.geometry('700x700')
canvas = Canvas(root, height=500, width=500, bg='white')
canvas.pack(expand=1)

# Grid size and cell size
grid_size = 25  # 25x25 cells (500/20 = 25)
cell_size = 20

# Draw grid
for i in range(0, 520, cell_size):
    canvas.create_line(i, 0, i, 500, width=1)  # Vertical lines
    canvas.create_line(0, i, 500, i, width=1)  # Horizontal lines

# Draw borders manually
canvas.create_line(2, 0, 2, 500, width=2)  # Left border
canvas.create_line(0, 2, 500, 2, width=2)  # Top border

# Choose entrance and exit
entrance = (0, random.randint(0, grid_size - 1))  # Top row
exit = (grid_size - 1, random.randint(0, grid_size - 1))  # Bottom row

# Mark entrance and exit visually
canvas.create_rectangle(entrance[0] * cell_size, entrance[1] * cell_size,
                        (entrance[0] + 1) * cell_size, (entrance[1] + 1) * cell_size,
                        fill='green', outline='green')
canvas.create_rectangle(exit[0] * cell_size, exit[1] * cell_size,
                        (exit[0] + 1) * cell_size, (exit[1] + 1) * cell_size,
                        fill='red', outline='red')

# Carve a path between entrance and exit
x, y = entrance
path = [entrance]

while (x, y) != exit:
    if random.choice([True, False]):  # Randomly move horizontally or vertically
        if x < exit[0]:  # Move right
            x += 1
        elif x > exit[0]:  # Move left
            x -= 1
    else:
        if y < exit[1]:  # Move down
            y += 1
        elif y > exit[1]:  # Move up
            y -= 1
    path.append((x, y))

# Remove walls along the path
for (x, y) in path:
    if (x - 1, y) in path:  # Remove left wall
        canvas.create_line(x * cell_size, y * cell_size,
                           x * cell_size, (y + 1) * cell_size, fill='white')
    if (x + 1, y) in path:  # Remove right wall
        canvas.create_line((x + 1) * cell_size, y * cell_size,
                           (x + 1) * cell_size, (y + 1) * cell_size, fill='white')
    if (x, y - 1) in path:  # Remove top wall
        canvas.create_line(x * cell_size, y * cell_size,
                           (x + 1) * cell_size, y * cell_size, fill='white')
    if (x, y + 1) in path:  # Remove bottom wall
        canvas.create_line(x * cell_size, (y + 1) * cell_size,
                           (x + 1) * cell_size, (y + 1) * cell_size, fill='white')

# Randomly remove additional walls for a maze effect
for _ in range(300):
    n = random.randint(0, grid_size - 1) * cell_size
    m = random.randint(0, grid_size - 1) * cell_size
    if (n // cell_size, m // cell_size) not in path:
        canvas.create_line(n + 1, m, n + cell_size, m, fill='white')
for _ in range(300):
    n = random.randint(0, grid_size - 1) * cell_size
    m = random.randint(0, grid_size - 1) * cell_size
    if (n // cell_size, m // cell_size) not in path:
        canvas.create_line(n, m + 1, n, m + cell_size, fill='white')

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
