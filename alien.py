# A Simple Dictionary
# Consider a game featuring aliens that can have different colors and point values. This simple dictionary stores information about a particular alien:
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

# Now you can access either the color or the point value of alien_0. If a player shoots down this alien, you can look up how many points they should earn using the code like this:
alien_0 ={'color':'green','points':5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0 = {'color':'green','points':5}
print(alien_0)

# Adding New Value Pairs
alien_0 = {'color':'green','points':5}
print(alien_0,'\n')

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an Empty Dictionary
# It's sometimes convenient, or even necessary, to start with an empty dictionary and then add each new item to it. Ti start filling an empty dictionary, define a dictionary with an empty set of braces and then add each key-value pair on its own line. 
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0) 
# 
# Typically, you'll use empty dictionaries when storing user-supplied data in a dictionary or when you write code that generates a large number of key-value pairs automatically.
# 
# Modifying Values in a Dictionary
# To modify a value in a dictionary, give the name of the dictionary with the key in square brackets and then the new value you want associated with that key. 
alien_0 = {'color':'green'} 
print(f"\nThe alien is {alien_0['color']}.")

alien_0['color'] ='yellow'
print(f"The alien is now {alien_0['color']}.")

# For a more interesting example, let's track the position of an alien that can move at different speeds. We'll store a value representing the alien's current speed and then use it to determine how far to the right the alien should move:
alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print(f"\nOriginal position: {alien_0['x_position']}")

#Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The new position in the old position plus the increment. 
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

# Removing Key Value Pairs
# When you no longer need a piece of information that's stored in a dictionary, you can use the del statement to completely remove a key-value pair. All del needs is the name of the dictionary and the key that you want to remove.
alien_0 = {'color':'green','points':5}
print(alien_0)

del alien_0['points']
print(alien_0)

# A Dictionary of Similar Objects
