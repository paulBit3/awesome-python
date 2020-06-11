# let's importing our pizza module here
import pizza

def greet_user():
    print("Hello!")

greet_user()
# Hello!

# let's passing information to our function

# passing parameter
def greet_user(username):
    print(f"Hello, {username.title()}!")

# passing argument
greet_user('Paul')
# Hello, Paul!

def favorite_book(title):
    print(f"My favorite books is {title.title()}")

favorite_book('Alice in Wonderland')

# My favorite books is Alice In Wonderland

# Positional Argument
# let's a function tells us what kind of animal each pet is and the pet's name
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('dog', 'willie')
# I have a hamster.
# My hamster's name is Harry.

# I have a dog.
# My dog's name is Willie.

# Keyword Arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='dog', pet_name='willie')
# I have a dog
# My dog's name is Willie.
describe_pet(pet_name='willie', animal_type='dog')
# I have a dog
# My dog's name is Willie.


def make_shirt(size, description):
    """Displaying information about the t-shirt"""
    print(f"\nThe shirt size is {size.title()}.")
    print(f"Title: {description.title()}")

# calling using the positional argument
make_shirt('s', 'python engineering empire')
#  The shirt size is S.
# Title: Python Engineering Empire

# calling using keyword argument
make_shirt(size='m', description='ml next gen')
#  The shirt size is M.
# Title: Ml Next Gen

# passing default value
def make_shirt(description, size='l'):
    """Displaying information about the t-shirt"""
    print(f"\nThe shirt size is {size.title()}")
    print(f"Title: {description.title()}")

make_shirt(description='my software engineer empire')
# The shirt size is L
# Title: My Software Engineer Empire

def describe_city(city_name, country):
    """Displaying city information"""
    print(f"\n{city_name.title()} is in {country.title()}.")
describe_city('Nashville', 'United States')
# Nashville is in United States.

# giving country a default value
def describe_city(city_name, country='France'):
    """Displaying city information"""
    print(f"\n{city_name.title()} is in {country.title()}.")

describe_city(city_name='paris')
# Paris is in France.
describe_city(city_name='London', country='United Kingdom')
# London is in United Kingdom.
describe_city(city_name='roma', country='italy')
# Roma is in Italy.


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'john')
print(musician)
# Jimi John

"""PRACTICING"""

def city_country(city_name, country):
    city_country_name = f"{city_name}, {country}"
    return city_country_name
city_country_na = city_country("Santiego", "Chilie")
print(city_country_na)
# Santiego, Chilie

# let's create a directory album
def make_album(artist_name, album_title):
    """Returning album and artist information"""
    album = {'artist': artist_name.title(), 'album': album_title.title()}
    return album
album_detail = make_album('fally', 'deliberation')
print(album_detail)
# {'artist': 'Fally', 'album': 'Deliberation'}

album_detail = make_album('celine dion', 'all come back')
print(album_detail)
# {'artist': 'Celine Dion', 'album': 'All Come Back'}

# let's add an optional parameter to our album function

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('Johny', 'Halliday', age=75)
print(musician)
# {'first': 'Johny', 'last': 'Halliday', 'age': 75}

def make_album(artist_name, album_title, number_song=None):
    """Returning album and artist information"""
    album = {'artist': artist_name.title(), 'album': album_title.title()}
    if number_song:
        album['number_song'] = number_song
    return album
album_detail = make_album('johnny haliday', 'allume le feu', number_song=15)
print(album_detail)
# {'artist': 'Johnny Haliday', 'album': 'Allume Le Feu', 'number_song': 15}

while True:
    print("\nEnter an artist's name:")
    a_name = input("Artist Name:")
    if a_name == 'q':
        break
    print("\nEnter album title:")
    a_title = input("Album Title:")
    if a_title == 'q':
        break
    artist_album_detail = make_album(a_name.title(), a_title.title())
    print(f"{artist_album_detail}")

# Enter an artist's name:
# Artist Name: Johny
#
# Enter album title:
# Album Title: allume le feu
# {'artist': ' Johny', 'album': ' Allume Le Feu'}
# Enter an artist's name:
# Artist Name:q
# Process finished with exit code 0

# Modifying a list in a Function
"""CASE STUDY"""
"""Let's consider a company that creates 3D printed models of designs that users submit.
Design that need to be printed are stored in a list, and after being printed they're
moved to a separate list."""

# Start with the design that need to be print
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []  # an empty list

# Simulate printing design until none are left.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")

    # Move each design to completed_models after printing.
    completed_models.append(current_design)

    # Display all completed models.
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# Printing model: dodecahedron
#
# The following models have been printed:
# dodecahedron
# Printing model: robot pendant
#
# The following models have been printed:
# dodecahedron
# robot pendant
# Printing model: phone case
#
# The following models have been printed:
# dodecahedron
# robot pendant
# phone case

# let's reorganize this code by writing function
# we will write 2 functions:

# the 1st function will handle printing the designs
def print_models(unprinted_designs, completed_models):
    # Simulate printing design until none are left.
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")

        # Move each design to completed_models after printing.
        completed_models.append(current_design)


# the 2nd function will summarize the prints
def show_completed_models(completed_models):
    # Display all the models that were printed.
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# look at to understand what our program is doing.
# Start with the design that need to be print
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []  # an empty completed models list

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Printing model: dodecahedron
# Printing model: robot pendant
# Printing model: phone case
#
# The following models have been printed:
# dodecahedron
# robot pendant
# phone case

"""PRACTICING"""
"""make a list of short text messages. Pass the list to a function which print each text message"""
# our message list
short_messages = ['hello world', 'how are you?', 'I like python programming ']

# messages printing function
def show_messages(messages):
    for message in messages:
        print(message)
show_messages(short_messages)
# hello world
# how are you?
# I like python programming

"""Write a function send_message that prints each text message and
 moves each message to a new list called sent_messages as it's printed"""

# in this case I can use the pop function and also the append function
def send_messages(messages, sent_messages):
    for message in messages:
        print(message)
    # moving each text message
    while messages:
        text_message = messages.pop()
        print(f"Text Message:{text_message}")
        sent_messages.append(text_message)

short_messages = ['hello world', 'how are you?', 'I like python programming ']
sent_messages = []
send_messages(short_messages, sent_messages)
# Text Message:I like python programming
# Text Message:how are you?
# Text Message:hello world

# we do not know the sent messages. So we will need to create an other function to handle sent messages

# in this case I can use the pop function and also the append function
def send_messages(messages, sent_messages):
    for message in messages:
        print(message)
    # moving each text message
    while messages:
        text_message = messages.pop()
        print(f"Text Message:{text_message}")
        sent_messages.append(text_message)

# create an other function to handle sent messages
def show_sent_message(sent_messages):
    """Show all sent messages"""
    print("\nThese are the printed messages.")
    for sent_message in sent_messages:
        print(sent_message)

"""In real world , we got this"""
# list of short message
short_messages = ['hello world', 'how are you?', 'I like python programming ']
sent_messages = []  # empty list message

send_messages(short_messages, sent_messages)
show_sent_message(sent_messages)

# so now we got this result.
# Text Message:I like python programming
# Text Message:how are you?
# Text Message:hello world
#
# These are the printed messages.
# I like python programming
# how are you?
# hello world

send_messages(short_messages[:], sent_messages)
print_models(short_messages[:], sent_messages)
print(sent_messages)

# list of sent_message
# ['I like python programming ', 'how are you?', 'hello world']

# Arbitrary keyword arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about the user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# let's see how it works
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

# ----------------------------------------------------------------
pizza.make_pizza(12, 'pepperoni')
pizza.make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')

# Making a 12-inch pizza with the following toppings:
# - pepperoni
#
# Making a 16-inch pizza with the following toppings:
# - mushrooms
# - green peppers
# - extra cheese


"""Clean up Whitespace"""
def clean_space(s):
    s = s.replace('\r', '')
    s = s.replace('\t', '')
    s = s.replace('\f', '')
    return s

my_space = 'hello     world   \n'
print(clean_space(my_space))


# Writing a function that accept sny number of argument
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

op = avg(1, 2)
print(op)  # 1.5 and len(rest) = 2

op2 = avg(1, 2, 3, 4)
print(op2)  # 2.5 and len(rest) = 4