def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    #First check: All vanity plates must start with at least two letters
    if not first_check(s):
        return False

    #Second check: Numbers cannot be used in the middle of a plate; they must come at the end.
    if not second_check(s):
        return False

    #Third check: No periods, spaces, or punctuation marks are allowed.
    return third_check(s)

def first_check(s):
    return s[0:2].isalpha()


def second_check(s):
    if len(s) == 2:
        return True
    is_digit_mode = False
    for i in s[2:]:
        if is_digit_mode:
            if i.isalpha():
                return False
        elif i.isdigit():
            is_digit_mode = True
            if i == '0':
                return False
    return True


def third_check(s):
    return s.isalnum()

main()
