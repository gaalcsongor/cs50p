import sys, random
from pyfiglet import Figlet


figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    font_type = random.choice(fonts)
    figlet.setFont(font=font_type)
    user_text = input("Input: ")
    print("Output: \n")
    print(figlet.renderText(user_text))
elif len(sys.argv) == 3:
    if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
        font_type = sys.argv[2]
        figlet.setFont(font=font_type)
        user_text = input("Input: ")
        print("Output: \n")
        print(figlet.renderText(user_text))
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
    

