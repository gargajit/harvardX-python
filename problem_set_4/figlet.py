from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

list = figlet.getFonts()
'''
if sys.argv[2] not in list:
    sys.exit("Not is list")

else:
    sys.exit("In list")
'''

if len(sys.argv) < 2:
    font_choice = random.choice(list)
    figlet.setFont(font=font_choice)
    text = input("Input: ")
    print(figlet.renderText(text))

elif len(sys.argv) <4:
    if sys.argv[1] != '-f' and sys.argv[1] != '--font' or sys.argv[2] not in list:
        sys.exit("Invalid usage")
    else:
        figlet.setFont(font=sys.argv[2])
        text = input("Input: ")
        print(figlet.renderText(text))
