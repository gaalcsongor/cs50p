# 1. input the user for a string in camelCase, and print the output
def main():
    name = input("camelCase: ").strip()
    print("snake_case: ", end="")
    case_change(name)
    

# 2. check where the uppercase char are within the string literal,
# insert a "_", and convert all char to lowercase
def case_change(x):
    for c in x:
        if c.isupper():
            print("_", c.lower(), sep="", end="")
        else:
            print(c, end="")


main()



        

        
        
