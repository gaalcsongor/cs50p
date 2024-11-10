import csv

guitars = []

with open("guitars.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        guitar = {"brand": row["brand"], "make": row["make"]}
        guitars.append(guitar)
        
for guitar in sorted(guitars, key=lambda guitar: guitar['make'], reverse=True):
    print(f"the {guitar['make']} is made by {guitar['brand']}")