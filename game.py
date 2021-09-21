import random

#Welcome
print("Rock, Paper, Scissors, Shoot!")
print("Welcome", player_name, "to my Rock-Paper-Scissors game ...")

#User Choice
user_choice = input("Please choose either 'rock', paper' or scissors:'")

if user_choice in ['rock', 'paper', 'scissors']:
    print("You chose:" , user_choice)
else:
    print("Please try again. Choose either rock, paper, or scissors")
    quit()

#Computer Choice at Random
options = ['rock', 'paper', 'scissors']

computer_choice = random.choice(options)
print("The computer chose:" , computer_choice)


#Determining the Winner
if(computer_choice == 'rock' and user_choice == 'scissors'):
    print("Oh, the computer won. It's ok")
elif(computer_choice == 'rock' and user_choice == 'paper'):
    print("You won!")
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