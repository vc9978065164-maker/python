#Define the custom user-defined exception
class InvalidAgeError(Exception):
    pass

def check_voting_eligibility(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be a negative number!")
    elif age < 18:
        raise InvalidAgeError("You must be 18 or older to vote.")
    else:
        print("Success You are eligible to vote.")

# Handle the custom exception using try-except
try:
    user_age = 15
    check_voting_eligibility(user_age)
    
except InvalidAgeError as error:
    # This block catches our custom exception and prints the error message
    print(f"Caught a User-Defined Exception: {error}")
