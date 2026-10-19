filename = "demo_file.txt"

with open(filename, 'w') as file:
    file.write("Line 1: writing using 'w' mode.\n")
print("Data successfully wrtten")

with open(filename, 'a') as file:
    file.write("Line 2: appending using 'a' mode.\n")
print("Data successfully wrtten")

print("\n reading the final file content")
with open(filename, 'r') as file:
    content = file.read()
    print(content)
