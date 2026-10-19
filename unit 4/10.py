# Step 1: Create a sample file and write 
with open("sample.txt", "w") as file:
  file.write("Hello, welcome to Python file handling")

# Step 2: Open the file in read mode and use tell() and seek()
with open("sample.txt", "r") as file:
  # Initial position of the file pointer
  print("Initial position (tell):", file.tell())

  # Read the first 5 characters
  print("Read first 5 chars:", file.read(5))
  print("Position after reading 5 chars (tell):", file.tell())

  # Use seek() to move the file pointer back to position 0 (beginning)
  file.seek(0)
  print("Position after seek(0):", file.tell())
  print("Read from beginning:", file.read(13))

  # Use seek() to move the file pointer to position 14
  file.seek(14)
  print("Position after seek(14):", file.tell())
  print("Read from position 14:", file.read())
