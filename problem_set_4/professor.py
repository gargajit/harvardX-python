import random


def main():
    score = 0
    n = get_level()
    for _ in range(10):
        x, y = generate_integer(n)
        right_answer = x + y

        for attempt in range(3):
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer != right_answer:
                    raise ValueError
                else:
                    score += 1
                    break

            except ValueError:
                print("EEE")
                if attempt == 2:
                    print(f"{x} + {y} = {right_answer}")


    print("Score:", score)


def get_level():
    try:
        lev = int(input("Level: "))
        if 1 <= lev <= 3:
            return lev
        else:
            return get_level()
    except ValueError:
        return get_level()

def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
        return x, y
    if level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
        return x, y
    if level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
        return x, y



if __name__ == "__main__":
    main()
