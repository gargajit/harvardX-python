import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        if matches := re.search(r"^(.+)\.(.+)\.(.+)\.(.+)$", ip):
            one = int(matches.group(1))
            two = int(matches.group(2))
            three = int(matches.group(3))
            four = int(matches.group(4))
            if one in range(0, 256) and two in range(0, 256) and three in range(0, 256) and four in range(0, 256):
                return True
            else:
                return False

        else:
            return False

    except ValueError:
        return False


if __name__ == "__main__":
    main()
