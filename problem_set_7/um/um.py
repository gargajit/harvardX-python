import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\bum\b"
    list_of_ums = re.findall(pattern, s, re.IGNORECASE)
    total_ums = len(list_of_ums)
    return total_ums
  

if __name__ == "__main__":
    main()
