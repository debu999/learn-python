from pprint import pp
import random

choice_computer = random.choice(["scissors", "paper", "rock"])
computer_choice = "scissors"
user_choice = input("Do you want rock, paper, or scissors?\n")
pp({"choice_computer": choice_computer, "user_choice": user_choice})
if choice_computer == user_choice:
    pp("TIE")
elif user_choice == "rock" and choice_computer == "scissors":
    pp("WIN")
elif user_choice == "paper" and choice_computer == "rock":
    pp("WIN")
elif user_choice == "scissors" and choice_computer == "paper":
    pp("WIN")
else:
    pp("You lose, computer wins :)")
