import random

# initialize scores
user_score = 0
computer_score = 0

# game loop
while True:
    # prompt user for choice
    user_choice = input("Choose rock, paper, or scissors: ")

    # generate computer choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # determine winner
    if user_choice == computer_choice:
        result = "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = "win"
        user_score += 1
    else:
        result = "lose"
        computer_score += 1

    # display result
    print(f"You chose {user_choice}, computer chose {computer_choice}. You {result}!")

    # ask to play again
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

# display final scores
print(f"Final score: You {user_score}, computer {computer_score}")
