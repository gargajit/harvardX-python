def main():
    text = str(input())
    convert(text)

def convert(input):
    mod_text = input.replace(':)', '🙂')
    mod_text = mod_text.replace(':(', '🙁')
    print(mod_text)

main()
