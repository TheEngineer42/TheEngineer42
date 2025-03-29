import tkinter as tk

def create_table(root, data):
    # Create the table using Label widgets arranged in a grid
    for row_num, row_data in enumerate(data):
        for col_num, value in enumerate(row_data):
            label = tk.Label(root, text=value, borderwidth=1, relief="solid", width=10, height=2)
            label.grid(row=row_num, column=col_num)

# Create main window
root = tk.Tk()
root.title("Table Example")

# Sample data (rows and columns)
data = [
    [1, 'A', 10.5],
    [2, 'B', 20.1],
    [3, 'C', 30.3],
    [4, 'D', 40.9]
]

# Create table
create_table(root, data)

# Run the app
root.mainloop()
