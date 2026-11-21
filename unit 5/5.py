
import pandas as pd

data = {
    'Name': ['Amit', 'Rahul', 'Neha', 'Priya'],
    'Age': [20, 21, 22, 20],
    'Marks': [85, 90, 78, 95]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

print("First 2 Records:")
print(df.head(2))

print("Basic Information:")
print(df.info())

print("Statistical Analysis:")
print(df.describe())

print("Average Marks:")
print(df['Marks'].mean())
