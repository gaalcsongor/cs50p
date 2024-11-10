import sys
import requests


if len(sys.argv) == 2:
    try: 
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    r = r.json()
    btc_rate = r["bpi"]["USD"]["rate"]
    btc_rate = float(btc_rate.replace(",", ""))
    print(f"${(btc_rate * amount):,.4f}")
elif len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
else:
    sys.exit("Too much command-line arguments")
    