# Error Type 1: ValueError 
# Occurs when a function gets an argument of the right type but an inappropriate value.
try:
    number = int("apple")  # Cannot convert letters into a number
except ValueError:
    print("Error 1: Caught a ValueError! You cannot convert text to an integer.")

# Error Type 2: ZeroDivisionError
# Occurs when you try to divide any number by zero.
try:
    result = 10 / 0  # Mathematically impossible
except ZeroDivisionError:
    print("Error 2: Caught a ZeroDivisionError! You cannot divide by zero.")
