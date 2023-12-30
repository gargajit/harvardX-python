input = input("Input: ")
output = ""
for s in input:
    if s.lower() not in ['a', 'e', 'i', 'o', 'u']:
        output += s
print("Output:", output)
