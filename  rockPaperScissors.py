import random


def rockPaperScissors(user_input,comp):
    # draws
    if(user_input == "rock") & (comp == "rock"):
        print("The computer chose rock. Rock versus rock, ends in a draw.")
    elif((user_input == "paper") & (comp == "paper")):
        print(" The computer chose paper. Paper versus paper, ends in a draw.")
    elif(( user_input == "scissors") & (comp == "scissors")):
        print("The computer chose scissors. Scissors versus scissors, ends in a draw.")
    # Comp wins
    elif((user_input == "rock") &(comp =="paper")):
        print("The computer chose paper. Rock versus paper, computer wins")
    elif(( user_input == "paper") & ( comp == "scissors")):
        print("The computer chose paper. Paper versus scissors, computer wins") 
    elif((user_input == "scissors") & ( comp == "rock")):
        print("The computer chose rock. Scissors versus rcok, computer wins")
    # User wins
    elif((user_input == "paper") & ( comp == "rock")):
        print("The computer chose rock. Paper versus rock, you win! ")
    elif((user_input == "rock") & ( comp == "scissors")):
        print(" The computer chose scissors. Rock versus scissors, you win! ")
    elif((user_input == "scissors") & ( comp == "paper")):
        print(" The computer chose paper. Scissors versus paper, you win! ")

rock = "rock"
paper = "paper"
scissors = "scissors"

list = [rock, paper, scissors]

computer = random.choice(list)

user = input("Rock. Paper. Scissors. Shoot!: ")

rockPaperScissors(user, computer) 
prompt = input ("would you like to play Rock, Paper, Scissors? Y/N: ")

prompt = prompt.upper()

while prompt == 'Y': 
    user_input = input ("Rock, Paper, Scissors. Shoot!: ")
    rockPaperScissors(user_input, computer)
    print()
    prompt = input ("Would you like to play another round Y/N: ")