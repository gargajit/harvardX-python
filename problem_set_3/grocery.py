grocery_dict = {}

while True:
    try:
        item = input()
        if item not in grocery_dict:
            grocery_dict.update({item: 1})
        else:
            x = grocery_dict.get(item)
            x = x + 1
            grocery_dict.update({item: x})
    except EOFError:
        sorted_dict = dict(sorted(grocery_dict.items(), key=lambda item: item[0]))
        break

for item in sorted_dict:
    print(sorted_dict[item], item.upper())
