import pandas as pd
import numpy as np

# Generate synthetic data
ages = pd.Series([25, 30, 35, np.nan, 28, 22, 40, 30, 29])
names = pd.Series(["Alice", "Bob", "Charlie"], index=["A", "B", "C"])
print(ages.values)
print(names.index)
print(ages.describe())
print(ages.value_counts())
