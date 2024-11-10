# problem set nr. 1 / Fuel Gauge
def main():
    
    fraction = round(get_fraction(), 2)        

    if fraction <= 0.01:
        print("E")
    elif fraction >= 0.99:
        print("F")
    else:
        print(f"{int(fraction * 100)}%")


def get_fraction():
    """prompts the user for the number and prompts again in case of errors"""
    while True:
        try:
            number = input("Fraction: ")
            x, y = number.split('/')
            x, y = int(x), int(y)
            if x > y:
                continue
            return x / y
        except:
            pass


main()
