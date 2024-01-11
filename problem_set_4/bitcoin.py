import sys
import requests

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

else:
    try:
        n = float(sys.argv[1])
        response = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json")
        obj = response.json()
        current_value = obj["bpi"]["USD"]["rate_float"]
        cost = n * current_value
        print(f"${cost:,.4f}")
    except (ValueError, RequestException):
        print("Command-line argument is not a number")
