import random

#Welcome
print("Rock, Paper, Scissors, Shoot!")
print("Welcome 'Player One' to my Rock-Paper_Scissors game ...")

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
if(computer_choice == 'rock' and user_choice == 'scissors'):
    print("You won!")
elif(computer_choice == 'rock' and user_choice == 'paper'):
    print("Oh, the computer won. It's ok.")
elif(computer_choice == 'rock' and user_choice == 'rock'):
    print("It's a tie!")
elif(computer_choice == 'paper' and user_choice == 'scissors'):
    print("You won!")
elif(computer_choice == 'paper' and user_choice == 'paper'):
    print("It's a tie!")
elif(computer_choice == 'paper' and user_choice == 'rock'):
    print("Oh, the computer won. It's ok.")
elif(computer_choice == 'scissors' and user_choice == 'scissors'):
    print("It's a tie!")
elif(computer_choice == 'scissors' and user_choice == 'paper'):
    print("Oh, the computer won. It's ok.")                        
else:
    print("You won!")    

#Goodbye
print("Thanks for playing. Please play again!")
