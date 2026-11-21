
import pandas as pd

# Create DataFrame
data = {
    'Name': ['Amit', 'Rahul', 'Neha'],
    'Marks': [85, 90, 95]
}

df = pd.DataFrame(data)

# Save as CSV
df.to_csv('student.csv', index=False)

# Read CSV file
data1 = pd.read_csv('student.csv')
print("CSV File Data:")
print(data1)

# Save as Excel
df.to_excel('student.xlsx', index=False)

# Read Excel file
data2 = pd.read_excel('student.xlsx')
print("Excel File Data:")
print(data2)
