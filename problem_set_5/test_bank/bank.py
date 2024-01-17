def main():
    greeting = input("Greeting: ").strip()
    dollars = value(greeting)
    print(f"${dollars}")


def value(greeting):
    word = 'Hello'
    letter = 'H'
    if greeting.lower().startswith(word.lower()):
        return 0
    elif greeting.lower().startswith(letter.lower()):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
