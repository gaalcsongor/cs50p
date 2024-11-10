import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")   
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        csv_file = sys.argv[1]
        if not csv_file.endswith("csv"):
            sys.exit("Not a CSV file")
            
    pizzas = []
            
    with open(csv_file) as file:
        reader = csv.reader(file)  
        for name, small, large in reader:
            pizzas.append({"name": name, "small": small, "large": large})
    
    header = pizzas.pop(0)
    print(tabulate(pizzas, header, tablefmt="grid"))


if __name__ == "__main__":
    main()
                  