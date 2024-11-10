import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.fullmatch(r"(([1]?\d{1,2})|([2][0-5]{2}))\.(([1]?\d{1,2})|([2][0-5]{2}))\.(([1]?\d{1,2})|([2][0-5]{2}))\.(([1]?\d{1,2})|([2][0-5]{2}))", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()