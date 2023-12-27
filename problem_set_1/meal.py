def main():
    ask_time = input("What time is it? ").strip()
    converted = convert(ask_time)
    if 7.0 <= converted <= 8.0:
        print("breakfast time")
    elif 12.0 <= converted <= 13.0:
        print("lunch time")
    elif 18.0 <= converted <= 19.0:
        print("dinner time")

def convert(time):
    hours, mins = time.split(':')
    hours = float(hours)
    mins = float(mins) / 60
    return hours + mins

if __name__ == "__main__":
    main()

