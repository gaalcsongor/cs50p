import csv

guitars = []

with open("guitars.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        guitars.append({"brand": row["brand"], "model": row["model"]})
        
for guitar in sorted(guitars, key=lambda guitar: guitar['model'], reverse=True):
    print(f"the {guitar['model']} is made by {guitar['brand']}")