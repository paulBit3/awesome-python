# let's import our pizza module
from pizza import make_pizza

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# iterate ad print ut 1,2,3
for x in mylist:
    print(x)


# adding number and strings to the correct lists using the "append" list method
numbers = []
strings = []
names = ["Paul", "John", "Eric"]

# add the numbers 1,2, 3 to the "numbers" list
numbers.append(1)
numbers.append(2)
numbers.append(3)

# he words 'hello' and 'world' to the strings variable.
strings.append('hello')
strings.append('world')

second_name = names[1]

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

# using operators with lists
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers

print(all_numbers)

# create two lists called x_list and y_list, which contain 10 instances of the variables x and y
x = "hello"
y = "world"

x_list = [x] * 10
y_list = [y] * 10

# create a list called big_list, which contains the variables x and y,
# 10 times each, by concatenating the two lists
big_list = x_list + y_list
print("x_list contains %d objects" % len(x_list))  # x_list contains 10 objects
print("y_list contains %d objects" % len(y_list))  # y_list contains 10 objects
print("big_list contains %d objects" % len(big_list))  # big_list contains 20 objects

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if y_list.count(y) == 10 and big_list.count(y) == 10:
    print("Great!")


names = ['Angle', 'Pablo', 'Myriam', 'Serge', 'Justin', 'Charles', 'Westley']
print(names[0])  # Angle
print(names[1])  # Pablo
print(names[2])  # Myriam
print(names[3])  # Serge
print(names[4])  # Justin
print(names[5])  # Charles
print(names[6])  # Westley

# let greet people
print(f"Hi {names[0]}")
print(f"Hello {names[1]}")
print(f"Hi, how are you {names[2]}?")
print(f"Hi Mrs {names[3]}!")
print(f"Good morning Mrs {names[4]}!")
print(f"Good afternoon {names[5]}")
print(f"Good evening {names[6]}")

# my transportation
hangout = ['Honda', 'Toyota', 'Uber', 'Lyft']
print(hangout[0])  # Honda
print(f"I would like to go out with a black {hangout[1]} Uber's car !")
# I would like to go out with a black Toyota Uber's car !

names.append('Paul')
print(names)  # ['Angle', 'Pablo', 'Myriam', 'Serge', 'Justin', 'Charles', 'Westley', 'Paul']

names.insert(1, 'Eliane')
print(names)  # ['Angle', 'Eliane', 'Pablo', 'Myriam', 'Serge', 'Justin', 'Charles', 'Westley', 'Paul']

# let's pop from the list

popped_names = names.pop()
print(names)  # 'Angle', 'Eliane', 'Pablo', 'Myriam', 'Serge', 'Justin', 'Charles', 'Westley', 'Paul']
print(popped_names)  # Paul

last_value = names.pop()
print(f"The last name is {last_value.title()}.")  # The last name is Westley.

# guest list
guests = ['Arnold', 'Peter', 'Jessica']
print(f"Welcome {guests[0]}! I organise a dinner and you are invited.") # Welcome Arnold! I organise a dinner and you are invited.
print(f"Welcome {guests[1]}! I organise a dinner and you are invited.")  # Welcome Peter! I organise a dinner and you are invited.
print(f"Welcome {guests[2]}! I organise a dinner and you are invited.")  # Welcome Jessica! I organise a dinner and you are invited.

# changing guest list
# one of my guest cannot make it
print(f"{guests[1]} could not make it")  # Peter could not make it
del guests[1]
# so I remove it in my list and add an other guest
guests.insert(1, 'Angelina')
print(guests)  # ['Arnold', 'Angelina', 'Jessica']

print(f"Welcome {guests[0]}! I organise a dinner and you are invited.") # Welcome Arnold! I organise a dinner and you are invited.
print(f"Welcome {guests[1]}! I organise a dinner and you are invited.")  # Welcome Angelina! I organise a dinner and you are invited.
print(f"Welcome {guests[2]}! I organise a dinner and you are invited.")  # Welcome Jessica! I organise a dinner and you are invited.

# more guests
# I want to invite 3 more people to my dinner
# I will use the insert method to add one guest in
# the beginning, one guest in the middle and one guest at the end using append
guests.insert(0, 'Matt')
guests.insert(2, 'Patrick')
guests.append('lova')
print(guests)  # ['Matt', 'Arnold', 'Patrick', 'Angelina', 'Jessica', 'lova']
print(f"Welcome {guests[0]}! I organise a dinner and you are invited.") # Welcome Matt! I organise a dinner and you are invited.
print(f"Welcome {guests[1]}! I organise a dinner and you are invited.")  # Welcome Arnold! I organise a dinner and you are invited.
print(f"Welcome {guests[2]}! I organise a dinner and you are invited.")  # Welcome Patrick! I organise a dinner and you are invited.
print(f"Welcome {guests[3]}! I organise a dinner and you are invited.") # Welcome Angelina! I organise a dinner and you are invited.
print(f"Welcome {guests[4]}! I organise a dinner and you are invited.")  # Welcome Jessica! I organise a dinner and you are invited.
print(f"Welcome {guests[5].title()}! I organise a dinner and you are invited.")  # Welcome Lova! I organise a dinner and you are invited.

# shrinking guest list to only invite  2 people
print("I can just invite 2 people for the dinner!")
# print(guests[1])
remove_guests = guests.pop(1)
print(remove_guests)
print(f"I'm, so sorry {remove_guests}, I can't invite you for dinner")
# I'm, so sorry Arnold, I can't invite you for dinner
# ['Matt', 'Patrick', 'Angelina', 'Jessica', 'lova']

remove_guests = guests.pop(2)
print(f"I'm, so sorry {remove_guests}, I can't invite you for dinner")
# I'm, so sorry Angelina, I can't invite you for dinner
# ['Matt', 'Patrick', 'Jessica', 'lova']

remove_guests = guests.pop(2)
print(f"I'm, so sorry {remove_guests}, I can't invite you for dinner")
# I'm, so sorry Jessica, I can't invite you for dinner
# ['Matt', 'Patrick', 'lova']

remove_guests = guests.pop(1)
print(f"I'm, so sorry {remove_guests}, I can't invite you for dinner")
# I'm, so sorry Patrick, I can't invite you for dinner
# ['Matt', 'lova']
print(guests)

# inform the 2 people still on the list
print(f"Hi {guests[0]}, you 're still invited")  # Hi Matt, you 're still invited
print(f"Hi {guests[1].title()}, you 're still invited")  # Hi Lova, you 're still invited

# making sure I have an empty list
del guests[0]
print(guests)  # ['lova']
del guests[0]
print(guests)  # an empty list

# let sort the guests names
guests.sort()
print(guests)  # ['Matt', 'lova']

name_list = ['Angle', 'Eliane', 'Pablo', 'Myriam', 'Serge', 'Justin', 'Charles', 'Westley', 'Paul']
name_list.sort()
print(name_list)  # ['Angle', 'Charles', 'Eliane', 'Justin', 'Myriam', 'Pablo', 'Paul', 'Serge', 'Westley']
print("\nHere is the guest sorted list:")
print(sorted(name_list))  # ['Angle', 'Charles', 'Eliane', 'Justin', 'Myriam', 'Pablo', 'Paul', 'Serge', 'Westley']

# list in reverse order
name_list.reverse()
print(name_list)  # ['Westley', 'Serge', 'Paul', 'Pablo', 'Myriam', 'Justin', 'Eliane', 'Charles', 'Angle']

# find the lenght
length =len(name_list)
print(length)  # 9

locations_list = ['Monaco', 'Miami', 'Bahamas', 'Cote Azure']
print(sorted(locations_list))
print(locations_list)
locations_list.reverse()
print(locations_list)
locations_list.reverse()
print(locations_list)
locations_list.sort()
print(locations_list)
print(len(guests))

for location in locations_list:
    print(f"{location.title()}, that was a great place!")
    print(f"I can't wait to visit {location} again.\n")

    # Bahamas, that was a great place!
    # I can't wait to visit Bahamas again.
    #
    # Cote Azure, that was a great place!
    # I can't wait to visit Cote Azure again.
    #
    # Miami, that was a great place!
    # I can't wait to visit Miami again.
    #
    # Monaco, that was a great place!
    # I can't wait to visit Monaco again.

pizza_lists = ['Peperoni', 'Sausage', 'Veggie', 'Cheese']
for pizza in pizza_lists:
    print(f"I like {pizza} pizza!")
print(f"I like when my pizza is well done.")
print(f"I really love pizza! ")

animals_lists = ['Giraffe', 'Dog', 'elephant', 'Lion', 'Cat']
for animal in animals_lists:
    print(f"A {animal} can be Human's friend!")
print(f"Any of these animals could be a good friend!")
# A Giraffe can be Human's friend!
# A Dog can be Human's friend!
# A elephant can be Human's friend!
# A Lion can be Human's friend!
# A Cat can be Human's friend!
# Any of these animals could be a good friend!

for value in range(1, 5):
    print(value)
numbers = list(range(1, 5))
print(numbers)  # a list of numbers [1, 2, 3, 4]

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)  # we append each new value of square
print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# let's write this code more concisely.
# we can omit the temporary variable square for more efficient approach
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# let find the max, min and sum of the squares list
print(min(squares))  # 1
print(max(squares))  # 100
print(sum(squares))  # 385

# list comprehension
squares = [value**2 for value in range(1, 11)]
print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# odd_numbers = [1, 3, 5, 7]
odd_numbers = list(range(1, 20, 2))
print(odd_numbers)
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# list of the first 10 cubes
cubes = []
for value in range(1, 11):
    cubes.append(value ** 3)
print(cubes)
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# list comprehension to generate the 1st 10 cubes
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# let's print the first 3 elements in our cubes
print(cubes[0:3])  # [1, 8, 27]

# the second, third, and fourth items in our cubes
print(cubes[1:4])  # [8, 27, 64]

# the last three element of our cubes
print(cubes[-3:])  # [512, 729, 1000]

# looping
print("Here is the first three numbers on my cubes")
for cube in cubes[:3]:
    print(cube)
# 1 8 27

# copying a list
my_foods = ['pizza', 'gyros', 'falafel', 'cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
#  My favorite foods are:
# ['pizza', 'gyros', 'falafel', 'cake']
#
# My friend's favorite foods are:
# ['pizza', 'gyros', 'falafel', 'cake']

my_foods.append('bracoli')
friend_foods.append('salad')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
#  My favorite foods are:
# ['pizza', 'gyros', 'falafel', 'cake', 'bracoli']
#
# My friend's favorite foods are:
# ['pizza', 'gyros', 'falafel', 'cake', 'salad']
pizzas = ['Peperoni', 'Sausage', 'Veggie', 'Cheese']
friend_pizzas = pizzas[:]
pizzas.append('Hawaiian')
friend_pizzas.append('Margherita')
print("My favorite pizza are:")
for pizza in pizzas:
    print(pizza)
#  My favorite pizza are:
# Peperoni
# Sausage
# Veggie
# Cheese
# Hawaiian
print("My friend favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
#  My friend favorite pizzas are:
# Peperoni
# Sausage
# Veggie
# Cheese
# Margherita


# multiple list
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry we don't have {requested_topping}.")
print("\nFinished making your pizza!")

user_names = ['admin', 'Paul', 'Angela', 'Marian']
for username in user_names:
    if username == 'admin':
        print(f"Hello {username}. would you like to see a status report?")
    elif username == 'Paul':
        print(f"Hello {username}. Thank you for logging again!")
    elif username == 'Angela':
        print(f"Hello {username}. Thank you for logging again!")
    else:
        print(f"hello {user_names[3]}. Thank you for logging again!")
print("You have greeted everybody!")

current_users = ['admin', 'Paul', 'Angela', 'Marian']
new_users = ['Jack', 'Paul', 'Erickson', 'Marian']
for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user}, you will need to enter a new username.")
    elif new_user not in current_users:
        print(f"{new_user} is still available.")
    # Jack is still available.
    # Paul, you will need to enter a new username.
    # Erickson is still available.
    # Marian, you will need to enter a new username

# making sure if 'Jack' has been used 'JACK' should not be accepted
# to do so , we will make a copy of current_user containing the lowercase versions of all the existing users
current_users = ['jack', 'paul', 'angela', 'marian']
new_current_user = current_users[:]
for new_user in new_current_user:
    if new_user in current_users:
        print(f"{new_user.upper()} should not be accepted!")


# ordinal numbers 1st 2nd 3rd, 4th, 5th, 6th, 9th
ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ordinal_position = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th']
for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print(f"{ordinal_number}st")
    elif ordinal_number == 2:
        print(f"{ordinal_number}nd")
    elif ordinal_number == 3:
        print(f"{ordinal_number}rd")
    else:
        print(f"{ordinal_number}th")
# 1st
# 2nd
# 3rd
# 4th
# 5th
# 6th
# 7th
# 8th
# 9th

# ----------------------------------------------------------------
make_pizza(12, 'pepperoni')
make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')

# Making a 12-inch pizza with the following toppings:
# - pepperoni
#
# Making a 16-inch pizza with the following toppings:
# - mushrooms
# - green peppers
# - extra cheese


""" a pet name list"""

#  empty initialized list
petNames = []
while True:
    print("Enter the pet's name " + str(len(petNames) + 1) + " (Or enter nothing to stop:.):")
    name = input()
    if name == '':
        break
    petNames = petNames + [name]  # list concatenation
    print('The pet name are:')
    for name in petNames:
        print("\n " + name)

# Enter the pet's name 1 (Or enter nothing to stop:.):
# wes
# The pet name are:
#
#  wes
# Enter the pet's name 2 (Or enter nothing to stop:.):
# edy
# The pet name are:
#
#  wes
#
#  edy
# Enter the pet's name 3 (Or enter nothing to stop:.):
# Norde
# The pet name are:
#
#  wes
#
#  edy
#
#  Norde