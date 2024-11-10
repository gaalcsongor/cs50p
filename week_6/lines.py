import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")   
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        code = sys.argv[1]
        if not code.endswith("py"):
            sys.exit("Not a Python file")

    lines = []

    try: 
        with open(code) as file:
            for line in file:
                line = line.strip()
                if (line != "") and (line.startswith("#") == False):
                    lines.append(line)
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(len(lines))


if __name__ == "__main__":
    main()