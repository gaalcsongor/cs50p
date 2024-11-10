#checks if hungarian mobile phone numbers are valid
import re

provider = {
    "20": "Telenor",
    "30": "T-Mobile",
    "70": "Vodafone"
    }

phone_number = input("the number: ")

pattern = r"(?:\+36|06) ([237]0) \d{3} \d{4}"

if matches := re.search(pattern, phone_number):
    print("valid")
else:
    print("not valid")
print(provider[matches.group(1)])