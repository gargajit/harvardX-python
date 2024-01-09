def main():
    name_list = []

    while True:
        try:
            name = input("Name: ").title()
            name_list.append(name)

        except EOFError:
            print()
            sing(name_list)
            break

def sing(list):
    n = len(list)
    result = "Adieu, adieu, to"
    for i in range(n):
        if n == 1:
            result += " " + list[i]
            break
        elif n == 2:
            if i < n-1:
                result += " " + list[i]
            else:
                result = result + " and " + list[i]
        else:
            if i < 1:
                result += " " + list[i]
            elif i < n-1:
                result = result + ", " + list[i]
            else:
                result = result + ", and " + list[i]
    print(result)


main()
