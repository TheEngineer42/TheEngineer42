# Create the main window
root = tk.Tk()
root.title("Table Example")

# Create a treeview widget (for table)
tree = ttk.Treeview(root, columns=("Column 1", "Column 2", "Column 3"), show="headings")

# Define the columns
tree.heading("Column 1", text="Column 1")
tree.heading("Column 2", text="Column 2")
tree.heading("Column 3", text="Column 3")

# Insert rows
tree.insert("", "end", values=(1, 'A', 10.5))
tree.insert("", "end", values=(2, 'B', 20.1))
tree.insert("", "end", values=(3, 'C', 30.3))
tree.insert("", "end", values=(4, 'D', 40.9))

# Pack the treeview
tree.pack()

# Run the app
root.mainloop()