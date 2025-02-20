import sys


distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU",
}


def main():
    spacecraft = input("Enter a spacecraft: ")
    au=get_au(spacecraft)
    m = convert(au)
    print(f"{m} m")

def get_au(spacecraft):
    try:
        au = float(distances[spacecraft])
        return (au)
    except KeyError:
        sys.exit(f"'{spacecraft}' is not in dictionary")
    except ValueError:
        sys.exit(f"Can't convert '{distances[spacecraft]}' to a float")

def convert(au):
    return (au * 149597870700)


main()
