import inflect

p = inflect.engine()

names = []

while True:
    name = input("Name: ")
    # exit by inputting "q"
    if name == "q":
        break
    names.append(name)

mylist = p.join(names)
print(f"Adieu, adieu, to {mylist}")
