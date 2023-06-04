# A Dictionary of Similar Objects
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

# To use this dictionary, given the name of a person who took the poll, you can easily look up their favorite language:

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward':'ruby', 
    'phil':'python',
}
for name,language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# Looping Through All the Keys in a Dictionary
# the keys() method is useful when you don't want to work with all the values in a dictionary. 

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward':'ruby', 
    'phil':'python',
}
for name in favorite_languages.values():
    print(name.title())

# YOu can access the value associated with any key you care about inside the loop by using the current key. 
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward':'ruby', 
    'phil':'python',
}
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(f"\nHi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
    print(f"{name.title()}, I see you love {language}!")

# Looping Through a Dictionary's Keys in a Particular Order
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward':'ruby', 
    'phil':'python',
}
for name in sorted(favorite_languages.keys()):
    print(f"\n{name.title()}, thank you for taking the poll.")

# Looping Through All Values in a Dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward':'ruby', 
    'phil':'python',
}
print("The following languages have been mentioned:")
for value in favorite_languages.values():
    print(value.title())

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward':'ruby', 
    'phil':'python',
}
print("The following languages have been mentioned.")
for language in set(favorite_languages.values()):
    print(language.title())
    