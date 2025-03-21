# Selecting a specific column (e.g., 'sepal_length')
sepal_length = df['sepal_length']
print("Sepal Length Column:\n", sepal_length.head())

# Selecting rows by integer location (first 5 rows)
first_five_rows = df.iloc[0:5]
print("\nFirst 5 Rows using iloc:")
print(first_five_rows)

# Access DataFrame attributes
print("\nDataFrame Columns:", df.columns)
print("DataFrame Index:", df.index)
