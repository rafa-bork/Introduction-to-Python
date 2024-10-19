import sys


# returns a given script's number of rows with text
def main():
    try:
        # script import and line caltulation
        with open(get_py(), "r") as file:
            lines = file.readlines()
            get_lenght(lines)
    # if there is not a script with the given name the progrem stops
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)


# returns the scripts name if the conditions arent met
def get_py():
    # does not return the file if were giver more arguments than necessary
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
    # does not return the file if it isnt a python file
    elif not sys.argv[1].endswith(".py"):
        print("Not a Python file")
    else:
        return sys.argv[1]
    # if any condition is met the program stops
    sys.exit(1)


# calculates the number of code lines in a script
def get_lenght(lines):
    line_number = 0
    # only count the line if it isnt empty or a comment
    for item in lines:
        item = item.strip()
        if item.startswith("#") or item == "":
            continue
        line_number += 1
    print(line_number)


if __name__ == "__main__":
    main()
