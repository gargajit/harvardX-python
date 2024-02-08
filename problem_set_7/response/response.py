from validator_collection import validators, checkers, errors

to_validate = input("What's your email address? ")

email_address = ''

try:
    email_address = validators.email(to_validate)

except errors.EmptyValueError:
    print("Input is empty")
except errors.InvalidEmailError:
    print("Invalid")


is_email_address = checkers.is_email(email_address)

if is_email_address:
    print("Valid")
