import sys

prices = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def main():
    price_total = 0
    # repeatedly asks for an item and updates the total order amount
    while True:
        price_total += item_input()
        print(f"Total: ${price_total:.2f}")


# returns a inputed item's value
def item_input():
    while True:
        try:
            item_name = input("Item: ")
            # looks up the capitalized item's name in the "prices" dictionary and returns its value
            return prices[item_name.title()]
        # if the user CRTL+Ds the program closes
        except EOFError:
            sys.exit()
        # if the item is not in the dictionary it reprompts
        except KeyError:
            pass


if __name__ == "__main__":
    main()
