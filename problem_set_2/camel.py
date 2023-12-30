def main():
    camel_case = input("camelCase: ")
    snake_case = to_snake_case(camel_case)
    print("snake_case:", snake_case)

def to_snake_case(input):
    output = ""
    for s in input:
        if s.isupper():
            output += '_' + s.lower()
        else:
            output += s
    return output

main()
