#main function prompts the user for a string
#and calls the answer() function
def main():
    a = input("What is the answer to the great Question of Life, the Universe, and Everything? ")
    a = a.lower()
    if answer(a):
        print("Yes")
    else:
        print("No")


def answer(n):
    match n:
        case "42" | "forty-two" | "forty two":
            return True
        case _:
            return False


main()
        