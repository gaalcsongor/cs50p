import random, sys


while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        continue
    if level >= 1:
        break
    
number = random.randint(1, level)

while True:
    try:
        user_guess = int(input("Guess: "))
    except ValueError:
        continue
    if user_guess >= 1:
        if user_guess < level:
            print("Too small!")
            continue
        elif user_guess > level:
            print("Too large!")
            continue
        else:
            sys.exit("Just right!")
    else:
        continue
