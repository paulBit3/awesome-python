dict_0 = {'color': 'green', 'points': 5}
print(dict_0)

# print a value
print(f"{dict_0['color']}.")  # green

# accessing values in our dictionary
new_points = dict_0['points']
print(f"You just earned {new_points} points!")

# let's add new key-value pair
dict_0 = {'color': 'green', 'points': 5}
dict_0['x_position'] = 0
dict_0['y_position'] = 25
print(dict_0)
# {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}

turtle_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# the turtle original position
print(f"Turtle original position: {turtle_0['x_position']}")

# let's move turtle to the right
# determine how far to move the turtle based on its current position
if turtle_0['speed'] == 'slow':
    x_increment = 1
elif turtle_0['speed'] == 'medium':
    x_increment = 2
else:
    # this must be a fast turtle
    x_increment = 3
# the new position of out turtle is the old position + the new position
turtle_0['x_position'] = turtle_0['x_position'] + x_increment

print(f"Turtle new position: {turtle_0['x_position']}")

# Turtle original position: 0
# Turtle new position: 2

person = {'first_name': 'Omar', 'last_name': 'Kouadio', 'age': 35, 'city': 'Nashville'}
print(person)
# {'first_name': 'Omar', 'last_name': 'Kouadio', 'age': 35, 'city': 'Nashville'}

# looping
users = {
    'username': 'paulbit',
    'first_name': 'Paul',
    'last_name': 'Bit',
}
for key, value in users.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# Key: username
# Value: paulbit
#
# Key: first_name
# Value: Paul
#
# Key: last_name
# Value: Bit

# I can also use abbreviation
for k, v in users.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
# Key: last_name
# Value: Bit
#
# Key: last_name
# Value: Bit
#
# Key: last_name
# Value: Bit

languages = {
    'paul': 'English',
    'Ablo': 'French',
    'Bit': 'Bit',
}

# let's create a list of users
user_2 = ['Paul', 'Ablo', 'Yohan']
for name in languages.keys():
    print(f"Hi {name.title()}")
    if name in user_2:
        language = languages[name].title()
        print(f"\t{name.title()}, I see you soon {language}!")
# Hi Paul
# Hi Ablo
# Hi Bit
# Ablo, I see you soon French!

# Nested dictionaries
dict_0 = {'color': 'green', 'points': 5}
turtle_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# create our list of dictionaries
turtle_color = [dict_0, turtle_0]
for turtle in turtle_color:
    print(turtle_color)

# make an empty list for sorting turtles
turtles = []
# make a dictionary of 30 green turtles
for turtle_number in range(30):
    new_turtle = {'color': 'green', 'points': 5, 'speed': 'slow'}
    turtles.append(new_turtle)
# show the first 5 turtles
for turtle in turtles:
    print(turtle)
print("...")
# show how many turtles have been created
print(f"Total number of turtles: {len(turtles)}")

# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# ...
# Total number of turtles: 30

# a list of dictionaries
# let's storing information about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
# summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza "   
      "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

fluent_languages = {
    'paul': ['English', 'French'],
    'John': ['French'],
    'Laeticia': ['italian', 'french', 'japanese'],
}
for name, languages in fluent_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# Paul's favorite languages are:
# 	English
# 	French
#
# John's favorite languages are:
# 	French
#
# Laeticia's favorite languages are:
# 	Italian
# 	French
# 	Japanese