import random

options = ("rock", "paper", "scissors")
print("Rock Paper Scissors!")
games = int(input("How many games you want to play?: "))
check = 0

while check <= games:
    cpu_selection = random.choice(options)
    
    user_selection = input("Select an option: rock, paper, scissors:").lower()


    print(f"User selected: {user_selection}")
    print(f"CPU selected: {cpu_selection}")

    if user_selection not in options:
        print("Please select a valid option!")
    elif user_selection == "rock" and cpu_selection == "scissors":
        print(f"You won! Game {check+1}")
        check += 1
    elif user_selection == "paper" and cpu_selection == "rock":
        print(f"You won! Game {check+1}")
        check += 1
    elif user_selection == "scissors" and cpu_selection == "paper":
        print(f"You won! Game {check+1}")
        check += 1
    else:
        print(f"CPU Wins! Game {check+1}")
        check += 1
