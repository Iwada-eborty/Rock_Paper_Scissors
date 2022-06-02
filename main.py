"""Code for  the rock, paper, scissors game"""
#import random module
import random

#print multiline instruction
print('A brief summary:\n'
     + 'If the two players choose the same character it is a tie, and the game repeats\n'
     +  'Rock beats Scissors\n'
      +  'Paper beats Rock\n'
      + 'Scissors beats Paper\n')

while True:
    user_action = input('Enter a choice (R, P, S): ')

#Create a list of the possible options 
    possible_options = ['R', 'P', 'S']

#print an error if user input is invalid
    while user_action not in possible_options:
        user_action = input("That is not a valid choice. Please try again: ")
  
#assign a random play to the computer
    computer_action = random.choice(possible_options)

#printing both player's moves
    print(f"\nPlayer {user_action}: CPU {computer_action}.\n")

#checking both player's moves
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "R":
        if computer_action == "S":
            print("Winner!")
        else:
            print("You lose!")
    elif user_action == "P":
        if computer_action == "R":
            print("Winner!")
        else:
            print("You lose!")
    elif user_action == "S":
        if computer_action == "P":
            print("Winner!")
        else:
            print("You lose!")
            
        play_again = input('Play again? (Y/N): ')
        if play_again != 'y':
            break    




  