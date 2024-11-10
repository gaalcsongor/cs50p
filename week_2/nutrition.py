#create a dict with food names as keyes and calories as values
nutrition = [
    {"name":"Apple", "cal":"130"},
    {"name":"Avocado California", "cal":"50"},
    {"name":"Banana", "cal":"110"},
    {"name":"Cantaloupe", "cal":"50"},
    {"name":"Grapefruit", "cal":"60"},
    {"name":"Grapes", "cal":"90"},
    {"name":"Honeydrew Melon", "cal":"50"},
    {"name":"Kiwifruit", "cal":"90"},
    {"name":"Lemon", "cal":"15"},
    {"name":"Lime", "cal":"20"},
    {"name":"Nectarine", "cal":"60"},
    {"name":"Orange", "cal":"80"},
    {"name":"Peach", "cal":"60"},
    {"name":"Pear", "cal":"100"},
    {"name":"Pineapple", "cal":"50"},
    {"name":"Plums", "cal":"70"},
    {"name":"Strawberries", "cal":"50"},
    {"name":"Sweet Cherries", "cal":"100"},
    {"name":"Tangerine", "cal":"50"},
    {"name":"Watermelon", "cal":"80"}
]

#take a str input from the user, case-insensitively
s = input("Item: ").lower()

#check if the input matches they "name" key in the dictionary, 
#if yes print out the value "cal"
for i in nutrition:
    if s == (i["name"]).lower():
        print("Calories:", i["cal"])
