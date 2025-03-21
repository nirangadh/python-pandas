import pandas as pd

# Create a dictionary with sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)
print("Pandas DataFrame:")
print(df)

# Access the first row using integer-location based indexing
print("\nFirst row using iloc:")
print(df.iloc[0])

# Access the 'Age' column using its name
print("\n'Age' column:")
print(df['Age'])
