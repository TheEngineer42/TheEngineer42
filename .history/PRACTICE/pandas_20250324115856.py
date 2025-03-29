import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Column Graph with X and Y Axes")

# Data for the graph
data = [50, 100, 150, 200, 250]  # The values of the columns
categories = ['A', 'B', 'C', 'D', 'E']  # The labels for the x-axis

# Create a Canvas widget
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

# Define graph parameters
margin = 20  # Margin from the edge of the canvas
bar_width = 40  # Width of each column/bar
max_value = max(data)  # Maximum value for scaling the y-axis
canvas_height = 250  # Height of the area to draw the graph

# Draw X and Y axes
canvas.create_line(margin, canvas_height, 350, canvas_height, arrow=tk.LAST)  # X axis
canvas.create_line(margin, canvas_height, margin, 50, arrow=tk.LAST)  # Y axis

# Labels for X axis
for i, category in enumerate(categories):
    x = margin + (i + 1) * (bar_width + 10)
    canvas.create_text(x, canvas_height + 10, text=category)

# Draw the columns (bars)
for i, value in enumerate(data):
    x1 = margin + (i + 1) * (bar_width + 10)
    y1 = canvas_height - (value / max_value) * canvas_height
    x2 = x1 + bar_width
    y2 = canvas_height

    # Draw the rectangle (column/bar)
    canvas.create_rectangle(x1, y1, x2, y2, fill="blue")

    # Add the value on top of the bar
    canvas.create_text((x1 + x2) / 2, y1 - 10, text=str(value))

# Start the Tkinter main loop
root.mainloop()
