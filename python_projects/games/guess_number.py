import random


# This is a guess number game
secret_number = random.randint(1, 20)
print("Enter a number between 1 and 20.")

# Ask the player to guess 6 times
for guessTaken in range(1, 7):
    print('Enter a number:')
    guess = int(input())

    if guess < secret_number:
        print("Your guess is too low")
    elif guess > secret_number:
        print("Your number is too high!")
    else:
        break

    if guess == secret_number:
        print("Great job! You guess the correct number in " + str(guessTaken) + "guess!")
    else:
        print("You miss it! The number was " + str(secret_number))

# Enter a number between 1 and 20.
# Enter a number:
# 3
# Your guess is too low
# You miss it! The number was 14
# Enter a number:
# 5
# Your guess is too low
# You miss it! The number was 14
# Enter a number:
# 9
# Your guess is too low
# You miss it! The number was 14
# Enter a number:
# 14