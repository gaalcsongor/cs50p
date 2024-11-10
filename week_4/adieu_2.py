# this version implements exittig with ctrl + d

import inflect
import sys

p = inflect.engine()

names = []

try:
    while True:
        name = input("Name: ")
        names.append(name)
except EOFError:
    mylist = p.join(names)
    print(f"Adieu, adieu, to {mylist}")
    sys.exit()