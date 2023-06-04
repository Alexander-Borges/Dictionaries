# 1 Person: Use a dictionary to store information about a person you know. Store their fist name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information from your dictionary. 
person = {
    'first_name': 'Jessica',
    'last_name': 'Levine',
    'age': 31,
    'city':'New York City'
}
print(person)

# 2 Favorite Numbers: Use a dictionary to store people's favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in you dictionary. Print each person's name and their favorite number.
favorite_numbers = {
    'alex':27,
    'alan':31,
    'andrew':42,
    'anthony':7,
    'amir': 99
}
for name, number in favorite_numbers.items():
    print(f"{name.title()}'s favorite number is {number}.\n")

# 3 Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let's call it a glossary.
# - Think of five programming words you've learned about in the previous chapters. Use these the words as keys in your glossary, and store their meanings as values.
glossary = {
    'variable': 'A named container that holds a value.',
    'function': 'A named block of code that performs a specific task.',
    'loop': 'A programming construct that repeats a set of instructions until a certain condition is met.',
    'list': 'An ordered collection of items.',
    'condition': 'A statement that controls the flow of execution based on a given condition.'
}

# Print the programming terms and their meanings
for term, meaning in glossary.items():
    print(f"\n{term}: {meaning}")

# Looping Through a dictionary
# Looping Through All Key-Value Pairs
