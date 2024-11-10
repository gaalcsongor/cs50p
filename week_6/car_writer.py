import csv

brand = input("Which brand? ")
model = input("Which model? ")
year = input("What year? ")

with open("car_data.csv", "a", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["brand", "model", "year"])
    writer.writerow({"brand": brand, "model": model, "year": year})
