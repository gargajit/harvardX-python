greeting = input("Greeting: ").strip()

word = 'Hello'
letter = 'H'

if greeting.lower().startswith(word.lower()):
    print("$0")
elif greeting.lower().startswith(letter.lower()):
    print("$20")
else:
    print("$100")
