# problem set nr. 3 / Grocery List

grocery_list = {}

while True:
    try:
        user_item = input()
        if user_item == "q":
            break
        elif user_item in grocery_list:
            grocery_list[user_item] += 1
        else:
            grocery_list[user_item] = 1
    except EOFError:
        break

for i in sorted(grocery_list.keys()):
    print(f"{grocery_list.get(i)} {i.upper()}")
        
        

    
