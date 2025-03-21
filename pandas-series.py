import pandas as pd

# Create a Pandas Series with custom indices
data_series = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print("Pandas Series:")
print(data_series)

# Access an element by its index label
print("\nElement with index 'b':", data_series['b'])
