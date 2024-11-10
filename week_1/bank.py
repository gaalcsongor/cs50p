def main():
    greeting = input("Greeting: ").lower().strip()
    money(greeting)


def money(n):
    if n[:5] == "hello":
        print("$0")
    elif n[0] == "h":
        print("$20")
    else:
        print("$100")


main()