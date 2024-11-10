from datetime import date
import inflect
import sys


def main():
    birthday = get_user_date()
    result = calculate_time(birthday)
    print((f"{convert(result)} minutes").capitalize())
    

def get_user_date():
    user_date = input("Date of Birth: ")
    try:
        year, month, day = user_date.split("-")
        birthday = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid date")
    return birthday


def calculate_time(birthday):
    today = date.today()
    result = int(((today - birthday).total_seconds()) / 60)
    return result
    

def convert(number):
    words = inflect.engine().number_to_words(number, andword="")
    return words


if __name__ == "__main__":
    main()
