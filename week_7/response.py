from validator_collection import validators, checkers, errors

user_email = input("What's your email address? ")

try: 
    if valid := validators.email(user_email):
        print("Valid")
except errors.InvalidEmailError:
    print("Invalid")
except errors.EmptyValueError:
    print("Invalid")


