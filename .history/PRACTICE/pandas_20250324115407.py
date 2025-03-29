import pandas as pd

# Create a DataFrame (table)
data = {
    'Column 1': [1, 2, 3, 4],
    'Column 2': ['A', 'B', 'C', 'D'],
    'Column 3': [10.5, 20.1, 30.3, 40.9]
}

df = pd.DataFrame(data)

# Display the table
print(df)