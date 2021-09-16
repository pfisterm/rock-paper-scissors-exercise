import random


print("Rock, Paper, Scissors, Shoot!")

#User Choice
user_choice = input("Please choose either 'rock', paper' or scissors:'")

if('rock' or 'paper' or 'scissors' in user_choice):
    print(user_choice)
else:
    quit()

#Computer Choice at Random
options = ['rock', 'paper', 'scissors']

computer_choice = random.choice(options)
print(computer_choice)

#Determining the Winner
