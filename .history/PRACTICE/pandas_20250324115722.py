import tkinter as tk

def create_text_table(root, data):
    # Create a Text widget for displaying the table
    text_widget = tk.Text(root, wrap="none", width=50, height=10)
    text_widget.grid(row=0, column=0)

    # Insert data into the Text widget
    for row in data:
        text_widget.insert(tk.END, "\t".join(str(cell) for cell in row) + "\n")
    
    # Disable editing the table for display purposes
    text_widget.config(state=tk.DISABLED)

# Create main window
root = tk.Tk()
root.title("Text Widget Table")

# Sample data (rows and columns)
data = [
    [1, 'A', 10.5],
    [2, 'B', 20.1],
    [3, 'C', 30.3],
    [4, 'D', 40.9]
]

# Create text-based table
create_text_table(root, data)

# Run the app
root.mainloop()
