#inputs the user for a str and calls is_valid function
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


#tests the str trough a series of logical expressions
def is_valid(s):
    if len(s) >= 2 and len(s) <= 6 and s[0:2].isalpha() and s.isalnum():
        for i in s:
            if i.isdigit():
                result = s.index(i) #stores the actual number of the loop in a variable
                if int(i) != 0 and s[result:].isdigit(): #creates a string sequence starting from the number opf the actual loop
                    return True
                else:
                    return False
        return True #returns true also if the character is not digit


main()