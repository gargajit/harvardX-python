def main():
    prompt = input("Fraction: ")
    fuel = convert(prompt)
    print(gauge(fuel))


def convert(fraction):
    x, y = fraction.split('/')
    numerator = int(x)
    denominator = int(y)
    if denominator == 0:
        raise ZeroDivisionError
    elif numerator <= denominator:
        return int((numerator / denominator)*100)
    else:
        raise ValueError


def gauge(percentage):
    if 1<percentage<99:
        return f"{percentage:.0f}%"
    elif percentage <= 1:
        return "E"
    else:
        return "F"


if __name__ == "__main__":
    main()
