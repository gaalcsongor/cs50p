def main():
    name = input("Input: ")
    print("Output: ", end="") 
    omit_vowel(name)


def omit_vowel(n):
    for c in n:
        if c.upper() in ("A", "E", "I", "O", "U"):
            print("", end="")
        elif c.lower() in ("a", "e", "i", "o", "u"):
            print("", end="")
        else:
            print(c, end="")


main()
