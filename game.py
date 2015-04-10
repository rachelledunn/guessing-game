""" Guessing game! The computer will choose a random number between 1 and 100,
asking the user to guess the number, giving them a hint if it's high or low."""

import random 

print "Howdy, what's your name?"
player_name = raw_input("Type in your name: ")

print "%s, I'm thinking of a number between 1 and 100..." % player_name
print "Try to guess my number!"

random_int = random.randint(0, 101)
player_guess = int(raw_input("Your guess? "))
tries = 0

while random_int != player_guess:
    if player_guess < random_int:
        tries = tries + 1
        print "Your guess is too low, try again."
        player_guess = int(raw_input("Your guess? "))
    if player_guess > random_int:
        tries = tries + 1
        print "Your guess is too high, try again."
        player_guess = int(raw_input("Your guess? "))
    if player_guess == random_int:
        tries = tries + 1
        print "Well done, %s! You found my number %d in %d tries!" % (player_name, random_int, tries)