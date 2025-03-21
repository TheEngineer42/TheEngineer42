import tkinter as tk
import random

# File to store coordinates
FILE_NAME = "kreslenie.txt"

# Function to generate a random color
def random_color():
    return f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}"

# Function to draw a circle and save coordinates
def draw_circle(event):
    x, y = event.x, event.y
    r = 10  # Radius of circle
    color = random_color()
    
    # Draw circle on canvas
    canvas.create_oval(x-r, y-r, x+r, y+r, fill=color, outline=color)
    
    # Save coordinates to file
    with open(FILE_NAME, "a") as file:
        file.write(f"{x}, {y}\n")

# Function to clear canvas and delete file contents
def clear_canvas(event):
    canvas.delete("all")  # Remove all drawn elements
    open(FILE_NAME, "w").close()  # Clear file by overwriting with empty content

# Initialize Tkinter window
root = tk.Tk()
root.title("Kresli Myšou")
root.geometry("600x400")

# Create canvas
canvas = tk.Canvas(root, bg="white", width=600, height=400)
canvas.pack(fill=tk.BOTH, expand=True)

# Bind events
canvas.bind("<Button-1>", draw_circle)  # Left mouse click
root.bind("<space>", clear_canvas)  # Space key

# Run application
root.mainloop()
