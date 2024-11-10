def main():
    greeting = input("input: ")
    print(value(greeting))


def value(greeting):
    n = 100
    greeting = str(greeting).lower().strip()
    if greeting[0:5] == "hello":
        n = 0
    elif greeting[0] == "h" and greeting[1:5] != "ello":
        n = 20
    return n


if __name__ == "__main__":
    main()
