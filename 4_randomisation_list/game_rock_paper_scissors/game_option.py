import random


# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")



choices = int(input(
    "What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors: "))
choices_computer = random.randint(0, 2)

game_choice_ascii = [rock, paper, scissors]

if choices == 0 :
    print(f"\nYour choice: {game_choice_ascii[0]}")
elif choices == 1:
    print(f"\nYour choice: {game_choice_ascii[1]}")
elif choices == 2:
    print(f"\nYour choice: {game_choice_ascii[2]}")
else:
    print("\nERROR\n")


if choices_computer == 0 :
    print(f"\nComputer chose: {game_choice_ascii[0]}")
elif choices_computer == 1:
    print(f"\nComputer chose: {game_choice_ascii[1]}")
elif choices_computer == 2:
    print(f"\nComputer chose: {game_choice_ascii[2]}")
else:
    print("\nERROR\n")


if choices_computer == 0 and choices == 1: 
    print("You Win!\n")
elif choices == 0 and choices_computer == 2:
    print("You Win!\n")
elif choices == 2 and choices_computer == 1:    
    print("You Win!\n")
elif choices_computer == choices:
    print("It's a Draw!\n")
else:
    print("You Lose!\n")


