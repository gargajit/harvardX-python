import sys
import csv
from PIL import Image, ImageOps

try:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input = sys.argv[1]
    output = sys.argv[2]
    valid_ext = ['jpg', 'jpeg', 'png']
    input_ext =  input.split('.')[-1].lower()
    output_ext = output.split('.')[-1].lower()
    if input_ext not in valid_ext:
        sys.exit("Invalid Input")
    if output_ext not in valid_ext:
        sys.exit("Invalid Output")

    if input_ext != output_ext:
        sys.exit("Input and Output have different extensions")

    shirt = Image.open("shirt.png")
    size = shirt.size

    im = Image.open(input)
    resized_image = ImageOps.fit(im, size)

    resized_image.paste(shirt, shirt)

    resized_image.save(output)

except FileNotFoundError:
    sys.exit("Input does not exist")
