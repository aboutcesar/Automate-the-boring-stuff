# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random, sys

wins = 0
loss = 0
tie = 0

while True:
    print("Enter Rock, Paper, Scissors or Quit")
    user_input = input()
    print("you chose " + str(user_input))
    if user_input == "quit":
        sys.exit()
    while True:
        possible_combos = ['rock', 'paper', 'scissors']

        # computer generated choice
        com_Choice = random.choice(possible_combos)
        print('the comuper choose ' + str(com_Choice))

        #tie
        if user_input == com_Choice:
            tie += 1
            print('It is a tie')
        #Chose paper
        elif user_input == 'paper':
            if com_Choice == 'rock':
                wins += 1
                print('you win')
            else:
                print('you loose')
                loss += 1
        #Choose rock
        elif user_input == 'rock':
            if com_Choice == 'scissors':
                wins += 1
                print('you win')
            else:
                loss += 1
                print('you loose')


        #chose scissors

        elif user_input == "scissors":
            if com_Choice == 'rock':
                loss += 1
                print('you lose')
            else:
                win +=1
                print('you win')

        break