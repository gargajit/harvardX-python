expression = input("Expression: ").strip()
x, y, z = expression.split(" ")

if y == '+':
    sum = float(x) + float(z)
    print(f"{sum: .1f}")
elif y == '-':
    minus = float(x) - float(z)
    print(f"{minus: .1f}")
elif y == '*':
    multiply = float(x) * float(z)
    print(f"{multiply: .1f}")
elif y == '/':
    divide = float(x) / float(z)
    print(f"{divide: .1f}")
else:
    print("Wrong Expression")
