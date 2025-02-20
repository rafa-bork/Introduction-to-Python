#1 Write a function sum_all that takes any number of positional arguments and returns their sum.

def sum_all(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

# Example usage:
print(sum_all(1, 2, 3))       # Output: 6
print(sum_all(10, 20, 30, 5))  # Output: 65


#2 Create a function concat_strings that takes any number of string arguments using *args and concatenates them into a single string.

def concat_strings(*args):
    phrase = ""
    for x in args:
        phrase += x
    return phrase

# Example usage:
print(concat_strings("Hello", " ", "world", "!"))  # Output: "Hello world!"
print(concat_strings("Python", " is", " fun!"))    # Output: "Python is fun!"


#3 Write a function greet that accepts a keyword argument name (default value: "Guest") and an optional keyword argument greeting (default value: "Hello"). Return the formatted greeting message.

def greet(**kwargs):
    name = kwargs.get('name', 'Guest')
    greeting = kwargs.get('greeting', 'Hello')
    return f"{greeting} {name}"

# Example usage:
print(greet(name="Alice", greeting="Hi"))  # Output: "Hi Alice"
print(greet(name="Bob"))                   # Output: "Hello Bob"
print(greet())                             # Output: "Hello Guest"


#4 Write a function describe_person that takes positional arguments (*args) for hobbies and keyword arguments (**kwargs) for personal details (e.g., name, age). Return a formatted string describing the person.


#Exercise iv) Combine *args and **kwargs
#Write a function describe_person that takes positional arguments (*args) for hobbies and keyword arguments (**kwargs) for personal details (e.g., name, age). Return a formatted string describing the person.

def describe_person(*args, **kwargs):
    name = kwargs.get("name", "Guest")
    age = kwargs.get("age", "unknown age")
    hobbies = ", ".join(args)
    if hobbies:
        hobby_text = f"enjoys {hobbies}."
    else:
        hobby_text = "has not shared any hobbies."
    return f"{name} ({age} years old) {hobby_text}"

# Example usage:
print(describe_person("reading", "traveling", name="Alice", age=30))


#1 Convert the following for loop into a list comprehension:

result = [x**2 for x in range(10)]
print(result)

# output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


#2 Rewrite this code using a list comprehension:

result = [x**2 for x in range(10) if x % 2 == 0]
print(result)

# output: [0, 4, 16, 36, 64]


#3 Convert the following code to a dictionary comprehension:

squares = {x: x**2 for x in range(5)}
print(squares)

# output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


#4 Rewrite the nested loop as a list comprehension:

pairs = [(x, y) for x in range(3) for y in range(2)]
print(pairs)

# output: [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]


#5 Transform the following code into a dictionary comprehension with a condition:

filtered_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(filtered_squares)

# output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}


#6 Convert the following loop into a list comprehension that includes a conditional transformation:

result = [x**2 if x % 3 == 0 else x for x in range(15)]
print(result)

# output: [0, 1, 2, 9, 4, 5, 36, 7, 8, 81, 10, 11, 144, 13, 14]


#7 Transform the following loop into a dictionary comprehension, using strings as keys:

words = ["apple", "banana", "cherry", "date"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)

# output: {'apple': 5, 'banana': 6, 'cherry': 6, 'date': 4}


#8 Rewrite this code using a single list comprehension to flatten the nested list:

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)

# output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


#9 Convert the following nested loop into a dictionary comprehension with a condition:

result = {(i, j): i + j for i in range(1, 3) for j in range(3, 6) if j % i != 0}
print(result)

# output: {(2, 3): 5, (2, 5): 7}


#10 Use a dictionary comprehension to filter and transform the following dictionary of dictionaries:

data = {
    "A": {"score": 90, "passed": True},
    "B": {"score": 65, "passed": False},
    "C": {"score": 75, "passed": True},
    "D": {"score": 50, "passed": False},
}
# Include only students who passed, and create a dictionary of their scores.
result = {key: value["score"] for key, value in data.items() if value["passed"]}
print(result)

# output: {'A': 90, 'C': 75}
