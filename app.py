import heapq, csv
from collections import OrderedDict
from random import randint, choice

# calling our modules(because all my modules are in separate folder)
from modules.car import Car


# drawing a Shape
# print("   /|")
# print("  / |")
# print(" /  |")
# print("/   |")

# variables & data type
name = "John"
age = 32
ismale = False
phrase = "Dex"
num = 5
print("There once was a man named " + name + ",")
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])  # getting the 1st caracter
print(phrase.index("x"))  # find a specific position
print(phrase.replace("Dex", "iTube"))
print(str(num))  # convert number to string
print(pow(4, 6))
print(round(3.2))

name = input("Enter your name: ")

# -------------------
myint = 7
print(myint)

myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

mystring = "Don't worry about apostrophes"
print(mystring)

# create a string, an integer, and a floating point number
mystring: str = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

remainder = 11 % 3
print(remainder)  # print 2

squared = 7 ** 2  # print 49
cubed = 2 ** 3  # print 8
print(squared)
print(cubed)

# Python also supports multiplying strings to form a string with a repeating sequence

loto: str = "hello" * 10
print(loto)  # hellohellohellohellohellohellohellohellohellohello

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)

# implemented a queue that sort item by given priority and always return
# item with highest priority on each pop operation
class PriorityQueue:
    def __init__(self):
        # creating a list of queue and index
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # The priority value is negated to get the queue to sort items from highest to lower priority
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name =name
    def __repr__(self):
        return 'Item({!r}'.format(self.name)

# here is how it works

q = PriorityQueue()
q.push(('banana'), 1)
q.push(('plantain'), 5)
q.push(('orange'), 4)
q.push(('candy'), 1)

print(q.pop())  # will print plantain as it has the highest priority
print(q.pop())  # will print orange as highest priority in the list
print(q.pop())  # will print banana as inserted in the queue
print(q.pop())  # will print candy as inserted in the queue

# ordered a dictionary when iterating or serializing #
d = OrderedDict()
d['banana'] = 1
d['plantain'] = 2
d['orange'] = 3
d['candy'] = 4
for key in d:
    print(key, d[key])

# print the dictionary in ordered
# banana 1
# plantain 2
# orange 3
# candy 4

# Calculating with dictionary
prices = {
    'Apple': 45.23,
    'Amazon': 120.23,
    'Google': 110.23,
    'Facebook': 109.23,
}

# let find the minimum and maximum price and stock name using zip
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)  # (45.23, 'Apple')

max_price = max(zip(prices.values(), prices.keys()))
print(max_price)  # (120.23, 'Amazon')

# sorted out price
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)  # 45.23, 'Apple'), (109.23, 'Facebook'), (110.23, 'Google'), (120.23, 'Amazon')]



# unordered list
items = [6, 7, 8, 9, 10, 11, 12, 13, 4, 2, 1, 4]
def find_item(item, itemlist):
    for i in range(0, len(items)):
        if item == itemlist[i]:
            return i
    return None

print(find_item(87, items))
print(find_item(12, items))
print(find_item(4, items))

message = "Hello Paul!"
message = "Hello Christina"
print(message)

fullname = "paul brou"
print(fullname.title())
print(fullname.upper())
print(fullname.lower())

first_name = "paul"
last_name = "brou"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print(message)

language = 'python '
language = language.rstrip()
print(language) # print ' python'

language = ' python'
language = language.lstrip()
print(language)  # print 'python '

language = ' python '
language = language.strip()
print(language)  # print 'python'

name = "Justin"
print(f"Hello {name}, would you like to learn something new today?")

name = "apollo"
print(name.lower())
print(name.upper())
print(name.title())

quote = "My Dad said, 'A person should always learn to be proeficient' "
print(quote)

famous_person = "Albert Einstein"
message = f"{famous_person} once said,'A person who never made a mistake never tried anything new'"
print(message)

new_name = ' youyou '
print("\t", new_name)
print("\n", new_name)

new_name = new_name.lstrip()
print(new_name)  # 'youyou '

new_name = new_name.rstrip()
print(new_name)  # ' youyou'

new_name = new_name.strip()
print(new_name)  # 'youyou'

# List
bicycle = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycle)  # ['trek', 'cannondale', 'redline', 'specialized']

# accessing element
print(bicycle[0].title())  # trek

print(bicycle[0].title())  # Trek

# accessing the last element
print(bicycle[-1])  # specialized

cars = ['audi', 'bmw', 'subaru', 'toyota', 'honda', 'hyundai', 'ford', 'mercedes']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# Audi
# BMW
# Subaru
# Toyota
# Honda
# Hyundai
# Ford
# Mercedes
cars = ['audi', 'bmw', 'subaru', 'toyota', 'honda', 'hyundai', 'ford', 'mercedes']
element = 'peugeot'
for car in cars:
    if element not in cars:
        print(f"{car.title()}, you can post it.")
# Audi, you can post it.
# Bmw, you can post it.
# Subaru, you can post it.
# Toyota, you can post it.
# Honda, you can post it.
# Hyundai, you can post it.
# Ford, you can post it.
# Mercedes, you can post it.

# Admission for anyone under age 4 is free.
# Admission for anyone between the ages of  4 and 18 is $25.
# Admission for anyone age 18 or older is $40.

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")
# if age = 70, admission cost is $20.

# the if-else chain
point = [5, 10, 15]
alien_color = 'red'
if alien_color == 'green':
    print(f"Your earned {point} points.")
else:
    print(f"your earned {point[1]} points.")

# the if -elif-else
if alien_color == 'green':
    print(f"Your earned {point[0]} points.")
elif alien_color == 'yellow':
    print(f"your earned {point[1]} points.")
else:
    print(f"Your earned {point[2]} points.")


new_car = Car('honda', 'accord', '2004', 21674, 'v4', 'gasoline', 'SALVR2BG1FH041029',
              MajorOptions='Leather Seats, Sunroof/Moonroof, Navigation System')
print(new_car.get_descriptive())
new_car.read_odometer()
new_car.odometer_reading = 45
new_car.read_odometer()

new_car.update_odometer(50)
new_car.read_odometer()
# 2004 Honda Accord 21674V4 Gasoline Salvr2Bg1Fh041029
# {'Majoroptions': 'Leather Seats, Sunroof/Moonroof, Navigation System'}
# This car has 0 miles on it.
# This car has 45 miles on it.
# This car has 50 miles on it.


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Printing a random number between 1 and the number of side the die has"""
        random_number = randint(1, self.sides)
        return random_number

my_roll_die = Die()
print(my_roll_die.roll_die())
# 5
# 4
# 2
# 4
# ...6

# Lottery
lottery = [0, 1, 2, 5, 4, 8, 7, 9, 3, 'A', 'G', 'P', 'O', 'Z']
"""Let's select numbers or letter the list and print them"""
first_loto = choice(lottery)
print(first_loto)
print(first_loto)
print(first_loto)
print(first_loto)
print(f"Any ticket matching {first_loto }, wins a prize")
# P
# P
# P
# P
# 4
# 4
# 4
# 4
# 4
# 0
# 0
# 0
# 0
# Any ticket matching these 0, wins a prize

# let's  make a list or tuple that pull numbers until a ticket win
lottery = [0, 1, 2, 5, 4, 8, 7, 9, 3, 'A', 'G', 'P', 'O', 'Z']
my_ticket = [0, 1, 0, 5, 0, 8, 8, 9, 3, 'A', 'G', 'Q']
while my_ticket:
    ticket_number = my_ticket.pop()
    print(f"Your play ticket number is: {ticket_number}")

    # Let's append the number into our lottery list
    lottery.append(ticket_number)
    print("\nThe following is your result:")

    # trying using list comprehension here
    for i, j in zip(my_ticket, lottery):
        if i == j:
            # Sort the list in ascending order
            # lottery.sort()
            print(f"You win!")
            # print(f"Your lucky number was: {lottery[j]}")


# Your play ticket number is: Q
#
# The following is your result:
# You win!
# Your lucky number was: 0
# You win!
# Your lucky number was: 1
# You win!
# Your lucky number was: 8
# You win!
# Your lucky number was: 3
# You win!
# Your lucky number was: A
# You win!
# Your lucky number was: 5
# You win!


# Reading and writing CSV Data

with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        print(row)

# ['', 'MSFT', 'Jan 1 2000', '39.81']
# ['', 'MSFT', 'Feb 1 2000', '36.35']
# ['', 'MSFT', 'Mar 1 2000', '43.22']
# ['', 'MSFT', 'Apr 1 2000', '28.37']
# ['', 'MSFT', 'May 1 2000', '25.45']
# ['', 'MSFT', 'Jun 1 2000', '32.54']
# ['', 'MSFT', 'Jul 1 2000', '28.4']
# ['', 'MSFT', 'Aug 1 2000', '28.4']
# ['', 'MSFT', 'Sep 1 2000', '24.53']
# ['', 'MSFT', 'Oct 1 2000', '28.02']
# ['', 'MSFT', 'Nov 1 2000', '23.34']
# ['', 'MSFT', 'Dec 1 2000', '17.65']
# ['', 'MSFT', 'Jan 1 2001', '24.84']
# ['', 'MSFT', 'Feb 1 2001', '24']
# ['', 'MSFT', 'Mar 1 2001', '22.25']
# ['', 'MSFT', 'Apr 1 2001', '27.56']
# ['', 'MSFT', 'May 1 2001', '28.14']
# ['', 'MSFT', 'Jun 1 2001', '29.7']
# ['', 'MSFT', 'Jul 1 2001', '26.93']
# ['', 'MSFT', 'Aug 1 2001', '23.21']
# ['', 'MSFT', 'Sep 1 2001', '20.82']
# ['', 'MSFT', 'Oct 1 2001', '23.65']
# ['', 'MSFT', 'Nov 1 2001', '26.12']
# ['', 'MSFT', 'Dec 1 2001', '26.95']
# ['', 'MSFT', 'Jan 1 2002', '25.92']
# ['', 'MSFT', 'Feb 1 2002', '23.73']
# ['', 'MSFT', 'Mar 1 2002', '24.53']
# ['', 'MSFT', 'Apr 1 2002', '21.26']
# ['', 'MSFT', 'May 1 2002', '20.71']
# ['', 'MSFT', 'Jun 1 2002', '22.25']
# ['', 'MSFT', 'Jul 1 2002', '19.52']
# ['', 'MSFT', 'Aug 1 2002', '19.97']
# ['', 'MSFT', 'Sep 1 2002', '17.79']
# ['', 'MSFT', 'Oct 1 2002', '21.75']
# ['', 'MSFT', 'Nov 1 2002', '23.46']
# ['', 'MSFT', 'Dec 1 2002', '21.03']
# ['', 'MSFT', 'Jan 1 2003', '19.31']
# ['', 'MSFT', 'Feb 1 2003', '19.34']
# ['', 'MSFT', 'Mar 1 2003', '19.76']
# ['', 'MSFT', 'Apr 1 2003', '20.87']
# ['', 'MSFT', 'May 1 2003', '20.09']
# ['', 'MSFT', 'Jun 1 2003', '20.93']
# ['', 'MSFT', 'Jul 1 2003', '21.56']
# ['', 'MSFT', 'Aug 1 2003', '21.65']
# ['', 'MSFT', 'Sep 1 2003', '22.69']
# ['', 'MSFT', 'Oct 1 2003', '21.45']
# ['', 'MSFT', 'Nov 1 2003', '21.1']
# ['', 'MSFT', 'Dec 1 2003', '22.46']
# ['', 'MSFT', 'Jan 1 2004', '22.69']
# ['', 'MSFT', 'Feb 1 2004', '21.77']
# ['', 'MSFT', 'Mar 1 2004', '20.46']
# ['', 'MSFT', 'Apr 1 2004', '21.45']
# ['', 'MSFT', 'May 1 2004', '21.53']
# ['', 'MSFT', 'Jun 1 2004', '23.44']
# ['', 'MSFT', 'Jul 1 2004', '23.38']
# ['', 'MSFT', 'Aug 1 2004', '22.47']
# ['', 'MSFT', 'Sep 1 2004', '22.76']
# ['', 'MSFT', 'Oct 1 2004', '23.02']
# ['', 'MSFT', 'Nov 1 2004', '24.6']
# ['', 'MSFT', 'Dec 1 2004', '24.52']
# ['', 'MSFT', 'Jan 1 2005', '24.11']
# ['', 'MSFT', 'Feb 1 2005', '23.15']
# ['', 'MSFT', 'Mar 1 2005', '22.24']
# ['', 'MSFT', 'Apr 1 2005', '23.28']
# ['', 'MSFT', 'May 1 2005', '23.82']
# ['', 'MSFT', 'Jun 1 2005', '22.93']
# ['', 'MSFT', 'Jul 1 2005', '23.64']
# ['', 'MSFT', 'Aug 1 2005', '25.35']
# ['', 'MSFT', 'Sep 1 2005', '23.83']
# ['', 'MSFT', 'Oct 1 2005', '23.8']
# ['', 'MSFT', 'Nov 1 2005', '25.71']
# ['', 'MSFT', 'Dec 1 2005', '24.29']
# ['', 'MSFT', 'Jan 1 2006', '26.14']
# ['', 'MSFT', 'Feb 1 2006', '25.04']
# ['', 'MSFT', 'Mar 1 2006', '25.36']
# ['', 'MSFT', 'Apr 1 2006', '22.5']
# ['', 'MSFT', 'May 1 2006', '21.19']
# ['', 'MSFT', 'Jun 1 2006', '21.8']
# ['', 'MSFT', 'Jul 1 2006', '22.51']
# ['', 'MSFT', 'Aug 1 2006', '24.13']
# ['', 'MSFT', 'Sep 1 2006', '25.68']
# ['', 'MSFT', 'Oct 1 2006', '26.96']
# ['', 'MSFT', 'Nov 1 2006', '27.66']
# ['', 'MSFT', 'Dec 1 2006', '28.13']
# ['', 'MSFT', 'Jan 1 2007', '29.07']
# ['', 'MSFT', 'Feb 1 2007', '26.63']
# ['', 'MSFT', 'Mar 1 2007', '26.35']
# ['', 'MSFT', 'Apr 1 2007', '28.3']
# ['', 'MSFT', 'May 1 2007', '29.11']
# ['', 'MSFT', 'Jun 1 2007', '27.95']
# ['', 'MSFT', 'Jul 1 2007', '27.5']
# ['', 'MSFT', 'Aug 1 2007', '27.34']
# ['', 'MSFT', 'Sep 1 2007', '28.04']
# ['', 'MSFT', 'Oct 1 2007', '35.03']
# ['', 'MSFT', 'Nov 1 2007', '32.09']
# ['', 'MSFT', 'Dec 1 2007', '34']
# ['', 'MSFT', 'Jan 1 2008', '31.13']
# ['', 'MSFT', 'Feb 1 2008', '26.07']
# ['', 'MSFT', 'Mar 1 2008', '27.21']
# ['', 'MSFT', 'Apr 1 2008', '27.34']
# ['', 'MSFT', 'May 1 2008', '27.25']
# ['', 'MSFT', 'Jun 1 2008', '26.47']
# ['', 'MSFT', 'Jul 1 2008', '24.75']
# ['', 'MSFT', 'Aug 1 2008', '26.36']
# ['', 'MSFT', 'Sep 1 2008', '25.78']
# ['', 'MSFT', 'Oct 1 2008', '21.57']
# ['', 'MSFT', 'Nov 1 2008', '19.66']
# ['', 'MSFT', 'Dec 1 2008', '18.91']
# ['', 'MSFT', 'Jan 1 2009', '16.63']
# ['', 'MSFT', 'Feb 1 2009', '15.81']
# ['', 'MSFT', 'Mar 1 2009', '17.99']
# ['', 'MSFT', 'Apr 1 2009', '19.84']
# ['', 'MSFT', 'May 1 2009', '20.59']
# ['', 'MSFT', 'Jun 1 2009', '23.42']
# ['', 'MSFT', 'Jul 1 2009', '23.18']
# ['', 'MSFT', 'Aug 1 2009', '24.43']
# ['', 'MSFT', 'Sep 1 2009', '25.49']
# ['', 'MSFT', 'Oct 1 2009', '27.48']
# ['', 'MSFT', 'Nov 1 2009', '29.27']
# ['', 'MSFT', 'Dec 1 2009', '30.34']
# ['', 'MSFT', 'Jan 1 2010', '28.05']
# ['', 'MSFT', 'Feb 1 2010', '28.67']
# ['', 'MSFT', 'Mar 1 2010', '28.8']
# ['', 'AMZN', 'Jan 1 2000', '64.56']
# ['', 'AMZN', 'Feb 1 2000', '68.87']
# ['', 'AMZN', 'Mar 1 2000', '67']
# ['', 'AMZN', 'Apr 1 2000', '55.19']
# ['', 'AMZN', 'May 1 2000', '48.31']
# ['', 'AMZN', 'Jun 1 2000', '36.31']
# ['', 'AMZN', 'Jul 1 2000', '30.12']
# ['', 'AMZN', 'Aug 1 2000', '41.5']
# ['', 'AMZN', 'Sep 1 2000', '38.44']
# ['', 'AMZN', 'Oct 1 2000', '36.62']
# ['', 'AMZN', 'Nov 1 2000', '24.69']
# ['', 'AMZN', 'Dec 1 2000', '15.56']
# ['', 'AMZN', 'Jan 1 2001', '17.31']
# ['', 'AMZN', 'Feb 1 2001', '10.19']
# ['', 'AMZN', 'Mar 1 2001', '10.23']
# ['', 'AMZN', 'Apr 1 2001', '15.78']
# ['', 'AMZN', 'May 1 2001', '16.69']
# ['', 'AMZN', 'Jun 1 2001', '14.15']
# ['', 'AMZN', 'Jul 1 2001', '12.49']
# ['', 'AMZN', 'Aug 1 2001', '8.94']
# ['', 'AMZN', 'Sep 1 2001', '5.97']
# ['', 'AMZN', 'Oct 1 2001', '6.98']
# ['', 'AMZN', 'Nov 1 2001', '11.32']
# ['', 'AMZN', 'Dec 1 2001', '10.82']
# ['', 'AMZN', 'Jan 1 2002', '14.19']
# ['', 'AMZN', 'Feb 1 2002', '14.1']
# ['', 'AMZN', 'Mar 1 2002', '14.3']
# ['', 'AMZN', 'Apr 1 2002', '16.69']
# ['', 'AMZN', 'May 1 2002', '18.23']
# ['', 'AMZN', 'Jun 1 2002', '16.25']
# ['', 'AMZN', 'Jul 1 2002', '14.45']
# ['', 'AMZN', 'Aug 1 2002', '14.94']
# ['', 'AMZN', 'Sep 1 2002', '15.93']
# ['', 'AMZN', 'Oct 1 2002', '19.36']
# ['', 'AMZN', 'Nov 1 2002', '23.35']
# ['', 'AMZN', 'Dec 1 2002', '18.89']
# ['', 'AMZN', 'Jan 1 2003', '21.85']
# ['', 'AMZN', 'Feb 1 2003', '22.01']
# ['', 'AMZN', 'Mar 1 2003', '26.03']
# ['', 'AMZN', 'Apr 1 2003', '28.69']
# ['', 'AMZN', 'May 1 2003', '35.89']
# ['', 'AMZN', 'Jun 1 2003', '36.32']
# ['', 'AMZN', 'Jul 1 2003', '41.64']
# ['', 'AMZN', 'Aug 1 2003', '46.32']
# ['', 'AMZN', 'Sep 1 2003', '48.43']
# ['', 'AMZN', 'Oct 1 2003', '54.43']
# ['', 'AMZN', 'Nov 1 2003', '53.97']
# ['', 'AMZN', 'Dec 1 2003', '52.62']
# ['', 'AMZN', 'Jan 1 2004', '50.4']
# ['', 'AMZN', 'Feb 1 2004', '43.01']
# ['', 'AMZN', 'Mar 1 2004', '43.28']
# ['', 'AMZN', 'Apr 1 2004', '43.6']
# ['', 'AMZN', 'May 1 2004', '48.5']
# ['', 'AMZN', 'Jun 1 2004', '54.4']
# ['', 'AMZN', 'Jul 1 2004', '38.92']
# ['', 'AMZN', 'Aug 1 2004', '38.14']
# ['', 'AMZN', 'Sep 1 2004', '40.86']
# ['', 'AMZN', 'Oct 1 2004', '34.13']
# ['', 'AMZN', 'Nov 1 2004', '39.68']
# ['', 'AMZN', 'Dec 1 2004', '44.29']
# ['', 'AMZN', 'Jan 1 2005', '43.22']
# ['', 'AMZN', 'Feb 1 2005', '35.18']
# ['', 'AMZN', 'Mar 1 2005', '34.27']
# ['', 'AMZN', 'Apr 1 2005', '32.36']
# ['', 'AMZN', 'May 1 2005', '35.51']
# ['', 'AMZN', 'Jun 1 2005', '33.09']
# ['', 'AMZN', 'Jul 1 2005', '45.15']
# ['', 'AMZN', 'Aug 1 2005', '42.7']
# ['', 'AMZN', 'Sep 1 2005', '45.3']
# ['', 'AMZN', 'Oct 1 2005', '39.86']
# ['', 'AMZN', 'Nov 1 2005', '48.46']
# ['', 'AMZN', 'Dec 1 2005', '47.15']
# ['', 'AMZN', 'Jan 1 2006', '44.82']
# ['', 'AMZN', 'Feb 1 2006', '37.44']
# ['', 'AMZN', 'Mar 1 2006', '36.53']
# ['', 'AMZN', 'Apr 1 2006', '35.21']
# ['', 'AMZN', 'May 1 2006', '34.61']
# ['', 'AMZN', 'Jun 1 2006', '38.68']
# ['', 'AMZN', 'Jul 1 2006', '26.89']
# ['', 'AMZN', 'Aug 1 2006', '30.83']
# ['', 'AMZN', 'Sep 1 2006', '32.12']
# ['', 'AMZN', 'Oct 1 2006', '38.09']
# ['', 'AMZN', 'Nov 1 2006', '40.34']
# ['', 'AMZN', 'Dec 1 2006', '39.46']
# ['', 'AMZN', 'Jan 1 2007', '37.67']
# ['', 'AMZN', 'Feb 1 2007', '39.14']
# ['', 'AMZN', 'Mar 1 2007', '39.79']
# ['', 'AMZN', 'Apr 1 2007', '61.33']
# ['', 'AMZN', 'May 1 2007', '69.14']
# ['', 'AMZN', 'Jun 1 2007', '68.41']
# ['', 'AMZN', 'Jul 1 2007', '78.54']
# ['', 'AMZN', 'Aug 1 2007', '79.91']
# ['', 'AMZN', 'Sep 1 2007', '93.15']
# ['', 'AMZN', 'Oct 1 2007', '89.15']
# ['', 'AMZN', 'Nov 1 2007', '90.56']
# ['', 'AMZN', 'Dec 1 2007', '92.64']
# ['', 'AMZN', 'Jan 1 2008', '77.7']
# ['', 'AMZN', 'Feb 1 2008', '64.47']
# ['', 'AMZN', 'Mar 1 2008', '71.3']
# ['', 'AMZN', 'Apr 1 2008', '78.63']
# ['', 'AMZN', 'May 1 2008', '81.62']
# ['', 'AMZN', 'Jun 1 2008', '73.33']
# ['', 'AMZN', 'Jul 1 2008', '76.34']
# ['', 'AMZN', 'Aug 1 2008', '80.81']
# ['', 'AMZN', 'Sep 1 2008', '72.76']
# ['', 'AMZN', 'Oct 1 2008', '57.24']
# ['', 'AMZN', 'Nov 1 2008', '42.7']
# ['', 'AMZN', 'Dec 1 2008', '51.28']
# ['', 'AMZN', 'Jan 1 2009', '58.82']
# ['', 'AMZN', 'Feb 1 2009', '64.79']
# ['', 'AMZN', 'Mar 1 2009', '73.44']
# ['', 'AMZN', 'Apr 1 2009', '80.52']
# ['', 'AMZN', 'May 1 2009', '77.99']
# ['', 'AMZN', 'Jun 1 2009', '83.66']
# ['', 'AMZN', 'Jul 1 2009', '85.76']
# ['', 'AMZN', 'Aug 1 2009', '81.19']
# ['', 'AMZN', 'Sep 1 2009', '93.36']
# ['', 'AMZN', 'Oct 1 2009', '118.81']
# ['', 'AMZN', 'Nov 1 2009', '135.91']
# ['', 'AMZN', 'Dec 1 2009', '134.52']
# ['', 'AMZN', 'Jan 1 2010', '125.41']
# ['', 'AMZN', 'Feb 1 2010', '118.4']
# ['', 'AMZN', 'Mar 1 2010', '128.82']
# ['', 'IBM', 'Jan 1 2000', '100.52']
# ['', 'IBM', 'Feb 1 2000', '92.11']
# ['', 'IBM', 'Mar 1 2000', '106.11']
# ['', 'IBM', 'Apr 1 2000', '99.95']
# ['', 'IBM', 'May 1 2000', '96.31']
# ['', 'IBM', 'Jun 1 2000', '98.33']
# ['', 'IBM', 'Jul 1 2000', '100.74']
# ['', 'IBM', 'Aug 1 2000', '118.62']
# ['', 'IBM', 'Sep 1 2000', '101.19']
# ['', 'IBM', 'Oct 1 2000', '88.5']
# ['', 'IBM', 'Nov 1 2000', '84.12']
# ['', 'IBM', 'Dec 1 2000', '76.47']
# ['', 'IBM', 'Jan 1 2001', '100.76']
# ['', 'IBM', 'Feb 1 2001', '89.98']
# ['', 'IBM', 'Mar 1 2001', '86.63']
# ['', 'IBM', 'Apr 1 2001', '103.7']
# ['', 'IBM', 'May 1 2001', '100.82']
# ['', 'IBM', 'Jun 1 2001', '102.35']
# ['', 'IBM', 'Jul 1 2001', '94.87']
# ['', 'IBM', 'Aug 1 2001', '90.25']
# ['', 'IBM', 'Sep 1 2001', '82.82']
# ['', 'IBM', 'Oct 1 2001', '97.58']
# ['', 'IBM', 'Nov 1 2001', '104.5']
# ['', 'IBM', 'Dec 1 2001', '109.36']
# ['', 'IBM', 'Jan 1 2002', '97.54']
# ['', 'IBM', 'Feb 1 2002', '88.82']
# ['', 'IBM', 'Mar 1 2002', '94.15']
# ['', 'IBM', 'Apr 1 2002', '75.82']
# ['', 'IBM', 'May 1 2002', '72.97']
# ['', 'IBM', 'Jun 1 2002', '65.31']
# ['', 'IBM', 'Jul 1 2002', '63.86']
# ['', 'IBM', 'Aug 1 2002', '68.52']
# ['', 'IBM', 'Sep 1 2002', '53.01']
# ['', 'IBM', 'Oct 1 2002', '71.76']
# ['', 'IBM', 'Nov 1 2002', '79.16']
# ['', 'IBM', 'Dec 1 2002', '70.58']
# ['', 'IBM', 'Jan 1 2003', '71.22']
# ['', 'IBM', 'Feb 1 2003', '71.13']
# ['', 'IBM', 'Mar 1 2003', '71.57']
# ['', 'IBM', 'Apr 1 2003', '77.47']
# ['', 'IBM', 'May 1 2003', '80.48']
# ['', 'IBM', 'Jun 1 2003', '75.42']
# ['', 'IBM', 'Jul 1 2003', '74.28']
# ['', 'IBM', 'Aug 1 2003', '75.12']
# ['', 'IBM', 'Sep 1 2003', '80.91']
# ['', 'IBM', 'Oct 1 2003', '81.96']
# ['', 'IBM', 'Nov 1 2003', '83.08']
# ['', 'IBM', 'Dec 1 2003', '85.05']
# ['', 'IBM', 'Jan 1 2004', '91.06']
# ['', 'IBM', 'Feb 1 2004', '88.7']
# ['', 'IBM', 'Mar 1 2004', '84.41']
# ['', 'IBM', 'Apr 1 2004', '81.04']
# ['', 'IBM', 'May 1 2004', '81.59']
# ['', 'IBM', 'Jun 1 2004', '81.19']
# ['', 'IBM', 'Jul 1 2004', '80.19']
# ['', 'IBM', 'Aug 1 2004', '78.17']
# ['', 'IBM', 'Sep 1 2004', '79.13']
# ['', 'IBM', 'Oct 1 2004', '82.84']
# ['', 'IBM', 'Nov 1 2004', '87.15']
# ['', 'IBM', 'Dec 1 2004', '91.16']
# ['', 'IBM', 'Jan 1 2005', '86.39']
# ['', 'IBM', 'Feb 1 2005', '85.78']
# ['', 'IBM', 'Mar 1 2005', '84.66']
# ['', 'IBM', 'Apr 1 2005', '70.77']
# ['', 'IBM', 'May 1 2005', '70.18']
# ['', 'IBM', 'Jun 1 2005', '68.93']
# ['', 'IBM', 'Jul 1 2005', '77.53']
# ['', 'IBM', 'Aug 1 2005', '75.07']
# ['', 'IBM', 'Sep 1 2005', '74.7']
# ['', 'IBM', 'Oct 1 2005', '76.25']
# ['', 'IBM', 'Nov 1 2005', '82.98']
# ['', 'IBM', 'Dec 1 2005', '76.73']
# ['', 'IBM', 'Jan 1 2006', '75.89']
# ['', 'IBM', 'Feb 1 2006', '75.09']
# ['', 'IBM', 'Mar 1 2006', '77.17']
# ['', 'IBM', 'Apr 1 2006', '77.05']
# ['', 'IBM', 'May 1 2006', '75.04']
# ['', 'IBM', 'Jun 1 2006', '72.15']
# ['', 'IBM', 'Jul 1 2006', '72.7']
# ['', 'IBM', 'Aug 1 2006', '76.35']
# ['', 'IBM', 'Sep 1 2006', '77.26']
# ['', 'IBM', 'Oct 1 2006', '87.06']
# ['', 'IBM', 'Nov 1 2006', '86.95']
# ['', 'IBM', 'Dec 1 2006', '91.9']
# ['', 'IBM', 'Jan 1 2007', '93.79']
# ['', 'IBM', 'Feb 1 2007', '88.18']
# ['', 'IBM', 'Mar 1 2007', '89.44']
# ['', 'IBM', 'Apr 1 2007', '96.98']
# ['', 'IBM', 'May 1 2007', '101.54']
# ['', 'IBM', 'Jun 1 2007', '100.25']
# ['', 'IBM', 'Jul 1 2007', '105.4']
# ['', 'IBM', 'Aug 1 2007', '111.54']
# ['', 'IBM', 'Sep 1 2007', '112.6']
# ['', 'IBM', 'Oct 1 2007', '111']
# ['', 'IBM', 'Nov 1 2007', '100.9']
# ['', 'IBM', 'Dec 1 2007', '103.7']
# ['', 'IBM', 'Jan 1 2008', '102.75']
# ['', 'IBM', 'Feb 1 2008', '109.64']
# ['', 'IBM', 'Mar 1 2008', '110.87']
# ['', 'IBM', 'Apr 1 2008', '116.23']
# ['', 'IBM', 'May 1 2008', '125.14']
# ['', 'IBM', 'Jun 1 2008', '114.6']
# ['', 'IBM', 'Jul 1 2008', '123.74']
# ['', 'IBM', 'Aug 1 2008', '118.16']
# ['', 'IBM', 'Sep 1 2008', '113.53']
# ['', 'IBM', 'Oct 1 2008', '90.24']
# ['', 'IBM', 'Nov 1 2008', '79.65']
# ['', 'IBM', 'Dec 1 2008', '82.15']
# ['', 'IBM', 'Jan 1 2009', '89.46']
# ['', 'IBM', 'Feb 1 2009', '90.32']
# ['', 'IBM', 'Mar 1 2009', '95.09']
# ['', 'IBM', 'Apr 1 2009', '101.29']
# ['', 'IBM', 'May 1 2009', '104.85']
# ['', 'IBM', 'Jun 1 2009', '103.01']
# ['', 'IBM', 'Jul 1 2009', '116.34']
# ['', 'IBM', 'Aug 1 2009', '117']
# ['', 'IBM', 'Sep 1 2009', '118.55']
# ['', 'IBM', 'Oct 1 2009', '119.54']
# ['', 'IBM', 'Nov 1 2009', '125.79']
# ['', 'IBM', 'Dec 1 2009', '130.32']
# ['', 'IBM', 'Jan 1 2010', '121.85']
# ['', 'IBM', 'Feb 1 2010', '127.16']
# ['', 'IBM', 'Mar 1 2010', '125.55']
# ['', 'GOOG', 'Aug 1 2004', '102.37']
# ['', 'GOOG', 'Sep 1 2004', '129.6']
# ['', 'GOOG', 'Oct 1 2004', '190.64']
# ['', 'GOOG', 'Nov 1 2004', '181.98']
# ['', 'GOOG', 'Dec 1 2004', '192.79']
# ['', 'GOOG', 'Jan 1 2005', '195.62']
# ['', 'GOOG', 'Feb 1 2005', '187.99']
# ['', 'GOOG', 'Mar 1 2005', '180.51']
# ['', 'GOOG', 'Apr 1 2005', '220']
# ['', 'GOOG', 'May 1 2005', '277.27']
# ['', 'GOOG', 'Jun 1 2005', '294.15']
# ['', 'GOOG', 'Jul 1 2005', '287.76']
# ['', 'GOOG', 'Aug 1 2005', '286']
# ['', 'GOOG', 'Sep 1 2005', '316.46']
# ['', 'GOOG', 'Oct 1 2005', '372.14']
# ['', 'GOOG', 'Nov 1 2005', '404.91']
# ['', 'GOOG', 'Dec 1 2005', '414.86']
# ['', 'GOOG', 'Jan 1 2006', '432.66']
# ['', 'GOOG', 'Feb 1 2006', '362.62']
# ['', 'GOOG', 'Mar 1 2006', '390']
# ['', 'GOOG', 'Apr 1 2006', '417.94']
# ['', 'GOOG', 'May 1 2006', '371.82']
# ['', 'GOOG', 'Jun 1 2006', '419.33']
# ['', 'GOOG', 'Jul 1 2006', '386.6']
# ['', 'GOOG', 'Aug 1 2006', '378.53']
# ['', 'GOOG', 'Sep 1 2006', '401.9']
# ['', 'GOOG', 'Oct 1 2006', '476.39']
# ['', 'GOOG', 'Nov 1 2006', '484.81']
# ['', 'GOOG', 'Dec 1 2006', '460.48']
# ['', 'GOOG', 'Jan 1 2007', '501.5']
# ['', 'GOOG', 'Feb 1 2007', '449.45']
# ['', 'GOOG', 'Mar 1 2007', '458.16']
# ['', 'GOOG', 'Apr 1 2007', '471.38']
# ['', 'GOOG', 'May 1 2007', '497.91']
# ['', 'GOOG', 'Jun 1 2007', '522.7']
# ['', 'GOOG', 'Jul 1 2007', '510']
# ['', 'GOOG', 'Aug 1 2007', '515.25']
# ['', 'GOOG', 'Sep 1 2007', '567.27']
# ['', 'GOOG', 'Oct 1 2007', '707']
# ['', 'GOOG', 'Nov 1 2007', '693']
# ['', 'GOOG', 'Dec 1 2007', '691.48']
# ['', 'GOOG', 'Jan 1 2008', '564.3']
# ['', 'GOOG', 'Feb 1 2008', '471.18']
# ['', 'GOOG', 'Mar 1 2008', '440.47']
# ['', 'GOOG', 'Apr 1 2008', '574.29']
# ['', 'GOOG', 'May 1 2008', '585.8']
# ['', 'GOOG', 'Jun 1 2008', '526.42']
# ['', 'GOOG', 'Jul 1 2008', '473.75']
# ['', 'GOOG', 'Aug 1 2008', '463.29']
# ['', 'GOOG', 'Sep 1 2008', '400.52']
# ['', 'GOOG', 'Oct 1 2008', '359.36']
# ['', 'GOOG', 'Nov 1 2008', '292.96']
# ['', 'GOOG', 'Dec 1 2008', '307.65']
# ['', 'GOOG', 'Jan 1 2009', '338.53']
# ['', 'GOOG', 'Feb 1 2009', '337.99']
# ['', 'GOOG', 'Mar 1 2009', '348.06']
# ['', 'GOOG', 'Apr 1 2009', '395.97']
# ['', 'GOOG', 'May 1 2009', '417.23']
# ['', 'GOOG', 'Jun 1 2009', '421.59']
# ['', 'GOOG', 'Jul 1 2009', '443.05']
# ['', 'GOOG', 'Aug 1 2009', '461.67']
# ['', 'GOOG', 'Sep 1 2009', '495.85']
# ['', 'GOOG', 'Oct 1 2009', '536.12']
# ['', 'GOOG', 'Nov 1 2009', '583']
# ['', 'GOOG', 'Dec 1 2009', '619.98']
# ['', 'GOOG', 'Jan 1 2010', '529.94']
# ['', 'GOOG', 'Feb 1 2010', '526.8']
# ['', 'GOOG', 'Mar 1 2010', '560.19']
# ['', 'AAPL', 'Jan 1 2000', '25.94']
# ['', 'AAPL', 'Feb 1 2000', '28.66']
# ['', 'AAPL', 'Mar 1 2000', '33.95']
# ['', 'AAPL', 'Apr 1 2000', '31.01']
# ['', 'AAPL', 'May 1 2000', '21']
# ['', 'AAPL', 'Jun 1 2000', '26.19']
# ['', 'AAPL', 'Jul 1 2000', '25.41']
# ['', 'AAPL', 'Aug 1 2000', '30.47']
# ['', 'AAPL', 'Sep 1 2000', '12.88']
# ['', 'AAPL', 'Oct 1 2000', '9.78']
# ['', 'AAPL', 'Nov 1 2000', '8.25']
# ['', 'AAPL', 'Dec 1 2000', '7.44']
# ['', 'AAPL', 'Jan 1 2001', '10.81']
# ['', 'AAPL', 'Feb 1 2001', '9.12']
# ['', 'AAPL', 'Mar 1 2001', '11.03']
# ['', 'AAPL', 'Apr 1 2001', '12.74']
# ['', 'AAPL', 'May 1 2001', '9.98']
# ['', 'AAPL', 'Jun 1 2001', '11.62']
# ['', 'AAPL', 'Jul 1 2001', '9.4']
# ['', 'AAPL', 'Aug 1 2001', '9.27']
# ['', 'AAPL', 'Sep 1 2001', '7.76']
# ['', 'AAPL', 'Oct 1 2001', '8.78']
# ['', 'AAPL', 'Nov 1 2001', '10.65']
# ['', 'AAPL', 'Dec 1 2001', '10.95']
# ['', 'AAPL', 'Jan 1 2002', '12.36']
# ['', 'AAPL', 'Feb 1 2002', '10.85']
# ['', 'AAPL', 'Mar 1 2002', '11.84']
# ['', 'AAPL', 'Apr 1 2002', '12.14']
# ['', 'AAPL', 'May 1 2002', '11.65']
# ['', 'AAPL', 'Jun 1 2002', '8.86']
# ['', 'AAPL', 'Jul 1 2002', '7.63']
# ['', 'AAPL', 'Aug 1 2002', '7.38']
# ['', 'AAPL', 'Sep 1 2002', '7.25']
# ['', 'AAPL', 'Oct 1 2002', '8.03']
# ['', 'AAPL', 'Nov 1 2002', '7.75']
# ['', 'AAPL', 'Dec 1 2002', '7.16']
# ['', 'AAPL', 'Jan 1 2003', '7.18']
# ['', 'AAPL', 'Feb 1 2003', '7.51']
# ['', 'AAPL', 'Mar 1 2003', '7.07']
# ['', 'AAPL', 'Apr 1 2003', '7.11']
# ['', 'AAPL', 'May 1 2003', '8.98']
# ['', 'AAPL', 'Jun 1 2003', '9.53']
# ['', 'AAPL', 'Jul 1 2003', '10.54']
# ['', 'AAPL', 'Aug 1 2003', '11.31']
# ['', 'AAPL', 'Sep 1 2003', '10.36']
# ['', 'AAPL', 'Oct 1 2003', '11.44']
# ['', 'AAPL', 'Nov 1 2003', '10.45']
# ['', 'AAPL', 'Dec 1 2003', '10.69']
# ['', 'AAPL', 'Jan 1 2004', '11.28']
# ['', 'AAPL', 'Feb 1 2004', '11.96']
# ['', 'AAPL', 'Mar 1 2004', '13.52']
# ['', 'AAPL', 'Apr 1 2004', '12.89']
# ['', 'AAPL', 'May 1 2004', '14.03']
# ['', 'AAPL', 'Jun 1 2004', '16.27']
# ['', 'AAPL', 'Jul 1 2004', '16.17']
# ['', 'AAPL', 'Aug 1 2004', '17.25']
# ['', 'AAPL', 'Sep 1 2004', '19.38']
# ['', 'AAPL', 'Oct 1 2004', '26.2']
# ['', 'AAPL', 'Nov 1 2004', '33.53']
# ['', 'AAPL', 'Dec 1 2004', '32.2']
# ['', 'AAPL', 'Jan 1 2005', '38.45']
# ['', 'AAPL', 'Feb 1 2005', '44.86']
# ['', 'AAPL', 'Mar 1 2005', '41.67']
# ['', 'AAPL', 'Apr 1 2005', '36.06']
# ['', 'AAPL', 'May 1 2005', '39.76']
# ['', 'AAPL', 'Jun 1 2005', '36.81']
# ['', 'AAPL', 'Jul 1 2005', '42.65']
# ['', 'AAPL', 'Aug 1 2005', '46.89']
# ['', 'AAPL', 'Sep 1 2005', '53.61']
# ['', 'AAPL', 'Oct 1 2005', '57.59']
# ['', 'AAPL', 'Nov 1 2005', '67.82']
# ['', 'AAPL', 'Dec 1 2005', '71.89']
# ['', 'AAPL', 'Jan 1 2006', '75.51']
# ['', 'AAPL', 'Feb 1 2006', '68.49']
# ['', 'AAPL', 'Mar 1 2006', '62.72']
# ['', 'AAPL', 'Apr 1 2006', '70.39']
# ['', 'AAPL', 'May 1 2006', '59.77']
# ['', 'AAPL', 'Jun 1 2006', '57.27']
# ['', 'AAPL', 'Jul 1 2006', '67.96']
# ['', 'AAPL', 'Aug 1 2006', '67.85']
# ['', 'AAPL', 'Sep 1 2006', '76.98']
# ['', 'AAPL', 'Oct 1 2006', '81.08']
# ['', 'AAPL', 'Nov 1 2006', '91.66']
# ['', 'AAPL', 'Dec 1 2006', '84.84']
# ['', 'AAPL', 'Jan 1 2007', '85.73']
# ['', 'AAPL', 'Feb 1 2007', '84.61']
# ['', 'AAPL', 'Mar 1 2007', '92.91']
# ['', 'AAPL', 'Apr 1 2007', '99.8']
# ['', 'AAPL', 'May 1 2007', '121.19']
# ['', 'AAPL', 'Jun 1 2007', '122.04']
# ['', 'AAPL', 'Jul 1 2007', '131.76']
# ['', 'AAPL', 'Aug 1 2007', '138.48']
# ['', 'AAPL', 'Sep 1 2007', '153.47']
# ['', 'AAPL', 'Oct 1 2007', '189.95']
# ['', 'AAPL', 'Nov 1 2007', '182.22']
# ['', 'AAPL', 'Dec 1 2007', '198.08']
# ['', 'AAPL', 'Jan 1 2008', '135.36']
# ['', 'AAPL', 'Feb 1 2008', '125.02']
# ['', 'AAPL', 'Mar 1 2008', '143.5']
# ['', 'AAPL', 'Apr 1 2008', '173.95']
# ['', 'AAPL', 'May 1 2008', '188.75']
# ['', 'AAPL', 'Jun 1 2008', '167.44']
# ['', 'AAPL', 'Jul 1 2008', '158.95']
# ['', 'AAPL', 'Aug 1 2008', '169.53']
# ['', 'AAPL', 'Sep 1 2008', '113.66']
# ['', 'AAPL', 'Oct 1 2008', '107.59']
# ['', 'AAPL', 'Nov 1 2008', '92.67']
# ['', 'AAPL', 'Dec 1 2008', '85.35']
# ['', 'AAPL', 'Jan 1 2009', '90.13']
# ['', 'AAPL', 'Feb 1 2009', '89.31']
# ['', 'AAPL', 'Mar 1 2009', '105.12']
# ['', 'AAPL', 'Apr 1 2009', '125.83']
# ['', 'AAPL', 'May 1 2009', '135.81']
# ['', 'AAPL', 'Jun 1 2009', '142.43']
# ['', 'AAPL', 'Jul 1 2009', '163.39']
# ['', 'AAPL', 'Aug 1 2009', '168.21']
# ['', 'AAPL', 'Sep 1 2009', '185.35']
# ['', 'AAPL', 'Oct 1 2009', '188.5']
# ['', 'AAPL', 'Nov 1 2009', '199.91']
# ['', 'AAPL', 'Dec 1 2009', '210.73']
# ['', 'AAPL', 'Jan 1 2010', '192.06']
# ['', 'AAPL', 'Feb 1 2010', '204.62']
# ['', 'AAPL', 'Mar 1 2010', '223.02']

