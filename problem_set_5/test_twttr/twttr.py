def main():
    from_user = input("Input: ")
    print("Output:", shorten(from_user))


def shorten(word):
    output = ""
    for s in word:
        if s.isalpha():
            continue
        elif s.lower() not in ['a', 'e', 'i', 'o', 'u']:
            output += s
    return output


if __name__ == "__main__":
    main()
