def main():
    exp = input("Expression: ")
    x, y, z = exp.split(" ")
    x = int(x)
    z = int(z)
    math(x, y, z)

def math(i, n, j):
    if n == "+":
        print(float(i + j))
    elif n == "-":
        print(float(i - j))
    elif n == "*":
        print(float(i * j))
    elif n == "/":
        if j == 0:
            print("dividing with 0 is not possible")
        else:    
            print(float(i / j))


main()
        
        

    










