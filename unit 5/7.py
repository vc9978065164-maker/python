
import pandas as pd

data = {
    'Name': ['Amit', 'Rahul', 'Neha', 'Priya'],
    'Age': [20, None, 22, None],
    'Marks': [85, 90, None, 95]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Remove missing values
print("After dropna():")
print(df.dropna())

# Fill missing values
print("After fillna():")
print(df.fillna(0))
