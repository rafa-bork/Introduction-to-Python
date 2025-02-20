import requests
import sys


# coverts a given number of bitcoins into its value in USD$
def main():
    input = get_input()
    bitcoin = bitcoin_api(input)
    print(f"${bitcoin:,.4f}")


# returns the coin ammount as a float
def get_input():
    try:
        value = float(sys.argv[1])
        return value
    # if the coin ammount cant be turned into a float the program stops
    except Exception:
        sys.exit(1)


# returns the coin ammount in $USD by its current exchange rate
def bitcoin_api(value):
    try:
        bit_value = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        # pulls the bitcoin rate in USD from the API
        one_bit = bit_value.json()["bpi"]["USD"]["rate_float"]
        return one_bit * value
    # if theres a problem in the API the program stops
    except requests.RequestException:
        sys.exit(1)


if __name__ == "__main__":
    main()
