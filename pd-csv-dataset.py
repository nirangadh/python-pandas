import pandas as pd

# Load the dataset from the same CSV URL
csv_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(csv_url)

# Display the first 5 rows
print("Dataset Head:")
print(df.head())

# Get concise summary of the DataFrame
print("\nDataset Info:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())
