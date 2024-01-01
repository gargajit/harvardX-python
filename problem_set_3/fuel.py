def main():
    fuel = fuel_percent("Fraction: ")
    if 1<fuel<99:
        print(f"{fuel:.0f}%")
    elif fuel <= 1:
        print("E")
    else:
        print("F")




def fuel_percent(prompt):
    while True:
        try:
            x, y = input(prompt).split('/')
            numerator = int(x)
            denominator = int(y)
            if numerator <= denominator:
                return (numerator / denominator)*100
        except (ValueError, ZeroDivisionError):
            pass

main()
