import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    root_1, ext_1 = os.path.splitext(sys.argv[1])
    root_2, ext_2 = os.path.splitext(sys.argv[2])
    if ext_1.lower() not in [".jpg", "jpeg", ".png"]:
        sys.exit("Invalid input")
    else:
        if ext_1.lower() != ext_2.lower():
            sys.exit("Input and output have different extensions")
        else:
            try:
                with Image.open(sys.argv[1]) as img, Image.open("shirt.png") as shirt_img:
                    resized_image = ImageOps.fit(img, shirt_img.size)
                    Image.Image.paste(resized_image, shirt_img, mask=shirt_img)
                    Image.Image.save(resized_image, sys.argv[2])
            except FileNotFoundError:
                sys.exit("Invalid input")


