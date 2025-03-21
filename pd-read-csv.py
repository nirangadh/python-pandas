import pandas as pd

# Sample CSV URL (for example purposes)
csv_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

# Read the CSV into a DataFrame
df = pd.read_csv(csv_url)

# Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())
