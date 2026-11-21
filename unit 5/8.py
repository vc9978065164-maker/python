
import matplotlib.pyplot as plt

names = ['Amit', 'Rahul', 'Neha', 'Priya']
marks = [85, 90, 78, 95]

# Line Chart
plt.plot(names, marks)
plt.title("Line Chart")
plt.show()

# Bar Chart
plt.bar(names, marks)
plt.title("Bar Chart")
plt.show()

# Histogram
plt.hist(marks, bins=4)
plt.title("Histogram")
plt.show()

# Pie Chart
plt.pie(marks, labels=names, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
