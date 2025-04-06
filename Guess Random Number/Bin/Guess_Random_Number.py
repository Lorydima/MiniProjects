# Guess Random Number Source Code Date: 04/04/2025 Developer: LDM Dev.

'''
This is a simple number guessing game where the user has to guess a random number between 1 and 5. The user has 3 attempts to guess the number.
'''

# Library for Game Dev.
from colorama import *
import random
import time

# Intro Graph
def intro_graph():
    intro_graph = '''
----------------------------------------------
*                                            *
*          GUESS RANDOM NUMBER GAME          *
*                                            *
----------------------------------------------

----------------------------------------------
Hi user! Welcome to the Guess Random Number Game.
In this game, you have to guess a random 
number between 1 and 5.
You have 3 attempts to guess the number.
So let's start the game!
---------------------------------------------
'''
    print(Fore.YELLOW + intro_graph + Fore.RESET)
    time.sleep(2)
    generate_random_number()

# Generate Random Number Function
def generate_random_number():
    print(Fore.BLUE + '\nGenerating a random number between 1 and 5.' + Fore.RESET)
    random_number = random.randint(1, 5)
    time.sleep(1)
    print(Fore.GREEN + 'Random number generated!' + Fore.RESET)
    check_user_guess(random_number)

# Check User Guess Function
def check_user_guess(random_number):
    attempts = 3
    while attempts > 0:
        try:
            user_guess = int(input(Fore.CYAN + f'\nYou have {attempts} attempts left. Enter your guess: ' + Fore.RESET))
            if user_guess < 1 or user_guess > 5:
                print(Fore.RED + 'Error: Please enter a number between 1 and 5.' + Fore.RESET)
                continue
            if user_guess == random_number:
                print(Fore.GREEN + 'Congratulations! You guessed the number!' + Fore.RESET)
                print(Fore.YELLOW + 'Thanks for playing!' + Fore.RESET)
                time.sleep(3)
                exit()
            elif user_guess > random_number:
                print(Fore.RED + 'Too high! Try again.' + Fore.RESET)
            else:
                print(Fore.RED + 'Wrong Number. Try Again' + Fore.RESET)
            attempts -= 1
        except ValueError:
            print(Fore.RED + 'Error: Please enter a valid number.' + Fore.RESET)
    
    print(Fore.RED + '\nYou have used all your attempts. Better luck next time!' + Fore.RESET)
    print(Fore.BLUE + f'The correct number was: {random_number}' + Fore.RESET)
    print(Fore.YELLOW + 'Thanks for playing!' + Fore.RESET)
    time.sleep(3)
    exit()

# Start Game Function
intro_graph()