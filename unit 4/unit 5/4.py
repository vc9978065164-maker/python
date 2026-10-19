def vote_age(age):
    assert age >= 18, "Age cannot be negative!"
    return age

print(vote_age(20) ) # Triggers AssertionError: Age cannot be negative
