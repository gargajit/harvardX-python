from random import randint

n = 0
while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        continue


random_value = randint(1, n)

while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue
        elif guess < random_value:
            print("Too small!")
        elif guess > random_value:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        continue
