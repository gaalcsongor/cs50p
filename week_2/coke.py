# egy while ciklussal teszteli az aktualis allas 50-hez valo viszonyat
def main():
    print("Amount Due: 50")
    num = get_number()
    while True:
        if num < 50:
            due = 50 - num
            print("Amount Due: ", due)
            num = num + get_number(due)
        else:
            print("Change Owed: ", num - 50)
            break


# ker egy int inputot amit tesztel egy while ciklussal
def get_number(m=50):
    while True:
        x = int(input("Insert Coin: "))
        if x == 5 or x == 10 or x == 25:
            break
        else:
            print("Amount Due: ", m) #ide be kell adni valtozonak az aktualis allast => due valtozo
    return x


main()

# meg kene meg nezni hogy lehetne-e egy picit optimalizalni, 
# mondjuk beleagyazni a printet az elejen az egyik functionbe
    
    








