def divide_numbers(a, b):
    print(f"\n--- Running calculation for: {a} / {b} ---")
    
    try:
        # 1. try: Put the code that might cause an error here
        result = a / b
        
    except ZeroDivisionError:
        # 2. except: Runs ONLY if a specific error happens inside the try block
        print(" Error: You cannot divide by zero")
        
    else:
        # 3. else: Runs ONLY if the try block succeeds with NO errors
        print(f" Success! The answer is: {result}")
        
    finally:
        # 4. finally: ALWAYS runs, no matter what happens (even if the code crashed)
        print(" Cleanup complete. This block always runs.")

# Test Case 1: Triggering the ELSE block (Successful division)
divide_numbers(10, 2)

# Test Case 2: Triggering the EXCEPT block (Division by zero)
divide_numbers(10, 0)
