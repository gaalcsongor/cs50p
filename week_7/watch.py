import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r'<iframe .* ?src="https?://(www)?\.?youtube\.com/embed/(xvFZjo5PgG0)" ?.*></iframe>', s):
        short_url = f"https://youtu.be/{matches.group(2)}"
        return short_url
    else:
        return None


if __name__ == "__main__":
    main()