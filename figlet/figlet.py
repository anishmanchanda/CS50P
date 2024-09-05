from pyfiglet import Figlet
from sys import argv
import sys
import random

figlet = Figlet()

# the user would like to output text in a random font.
if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(font_list))

# the user would like to output text in a specific font
elif len(sys.argv) == 3 and (argv[1] == "-f" or argv[1] == "--font"):
    if argv[2] in figlet.getFonts():
        figlet.setFont(font=argv[2])
    else:
        sys.exit("Invalid usage")

# otherwise error
else:
    sys.exit("Invalid usage")

string = input("Input: ")
print(f"Output: \n{figlet.renderText(string)}")
