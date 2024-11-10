def main():
    n = input("What time is it? ")
    x = convert(n)
    decide(x)

def convert(time):
    x, y = time.split(":")
    x = float(x)
    y = float(y) / 60
    return x + y


def decide(z):
    if z >= 7.00 and z <= 8.00:
        print("breakfast time")
    elif z >= 12.00 and z <= 13.00:
        print("lunch time")
    elif z >= 18.00 and z <= 19.00:
        print("dinner time")


if __name__ == "__main__":
    main()
     
