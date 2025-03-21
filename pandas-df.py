import pandas as pd

# Create a Pandas Series
data_series = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print("Series:\n", data_series)

# Create a Pandas DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)
