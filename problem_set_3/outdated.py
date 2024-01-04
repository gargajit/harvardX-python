def main():
    while True:
        try:
            input_date = input("Date: ").strip()
            if '/' in input_date:
                month, day, year = input_date.split('/')
                month = int(month)
                day = int(day)
                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year}-{month:02}-{day:02}")
                    break
            elif ',' in input_date:
                parts = input_date.split(' ')
                month = parts[0]
                day = int(parts[1][:-1])     # removing the comma from the day part
                year = parts[2]
                month_num = convert(month)
                if 1 <= day <= 31:
                    print(f"{year}-{month_num:02}-{day:02}")
                    break
        except (NameError, ValueError):
            continue

def convert(m):
    month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    for i in range(len(month_list)):
        if m == month_list[i]:
            x = i + 1
            return x


main()
