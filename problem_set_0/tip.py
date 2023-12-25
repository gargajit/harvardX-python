def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    cost = float(d.removeprefix('$'))
    return cost


def percent_to_float(p):
    your_tip = float(p.removesuffix('%'))
    return your_tip / 100

main()
