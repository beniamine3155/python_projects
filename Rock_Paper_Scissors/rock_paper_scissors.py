import random # import random module for computer choice

user_wins = 0 
computer_wins = 0

options = ['rock','paper','scissors'] # list of possible choices

while True:
    user_choice = input("Type Rock/Paper/Scissors to play or Q to quit: ").lower()
    if user_choice == "q":
        break

    if user_choice not in options: # check if user input is valid
        continue

    random_index = random.randint(0,2) # generate random index for computer choice
    computer_choice = options[random_index] # assign computer choice to random index
    print(f"Computer choice is {computer_choice}")

    if user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        user_wins += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
        user_wins += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        user_wins += 1
    else:
        print("You lose!")
        computer_wins += 1

print(f"You won {user_wins} times")
print(f"Computer won {computer_wins} times")
print("TaTa\n")
