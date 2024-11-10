# a loopon belülre be kell epiteni az exceptiont ha nem intet ad meg valasznak
# a user
import random


def main():
    level = get_level()
    score = 0
    
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        j = 0
        while j < 3:
            solution = int(input(f"{x} + {y} = "))
            if solution == x + y:
                score += 1
                break
            else:
                print("EEE")
                j += 1
                if j == 3:
                    print(x + y)
                continue
        i += 1  
                  
    print(f"Score: {score}")
    

def get_level():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            continue
        if n > 0 and n < 4:
            break
    return n
        

def generate_integer(level):
    if level == 1:
        m = random.randint(0, 9)
    elif level == 2:
        m = random.randint(10, 99)
    else:
        m = random.randint(100, 999)
    return m


if __name__ == "__main__":
    main()