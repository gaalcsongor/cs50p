import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    try:
        with open(sys.argv[1], "r") as before, open(sys.argv[2], "w", newline='') as after:
            reader = csv.DictReader(before)
            writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                first, last = row["name"].split(",")
                writer.writerow(
                    {
                        "first": first.strip(),
                        "last": last.strip(),
                        "house": row["house"]
                    }
                )
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    
        
          

