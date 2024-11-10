# problem set nr. 2 / Felipe’s Taqueria

import sys

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

item_price = 0

while True:

    try:
        item = input("Item: ")
    except EOFError:
        print(" ")
        sys.exit()

    for i in menu:
        if item.lower() == i.lower():
            item_price = item_price + menu[i]
            print(f"${item_price:.2f}")

