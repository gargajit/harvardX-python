import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$"
    matches = re.search(pattern, s)

    if not matches:
        raise ValueError

    hour1 = int(matches.group(1))
    min1 = int(matches.group(2) or 0)
    period1 = matches.group(3)
    hour2 = int(matches.group(4))
    min2 = int(matches.group(5) or 0)
    period2 = matches.group(6)


    if period1 == 'PM' and hour1 != 12:
        hour1 += 12
    elif period1 == 'AM' and hour1 == 12:
        hour1 = 0

    if period2 == 'PM' and hour2 != 12:
        hour2 += 12
    elif period2 == 'AM' and hour2 == 12:
        hour2 = 0


    if not (0 <= hour1 <= 23 and 0 <= min1 <= 59 and 0 <= hour2 <= 23 and 0 <= min2 <= 59):
        raise ValueError("Invalid time")

    formatted_time1 = "{:02}:{:02}".format(hour1, min1)
    formatted_time2 = "{:02}:{:02}".format(hour2, min2)

    new_format = f"{formatted_time1} to {formatted_time2}"
    return new_format


if __name__ == "__main__":
    main()
