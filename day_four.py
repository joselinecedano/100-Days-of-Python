'''
This is a simple rock, paper, scissors game. The user is prompted to choose between rock, paper, or scissors. The computer will then randomly choose one of the three options. The user's choice and the computer's choice will be printed to the console. The winner will be determined based on the following rules:
- Rock wins against scissors
- Scissors win against paper
- Paper wins against rock
'''
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to Rock, Paper, Scissors! : Python Edition\n")
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2) # randomly choose between 0, 1, or 2 for rock, paper, or scissors

if choice == 0: # if user chooses rock
  print(rock)
  if computer_choice == 0: 
    print("Computer chose:\n" + rock + "\nIt's a draw!")
  elif computer_choice == 1:
    print("Computer chose:\n" + paper + "\nYou lose!")
  else:
    print("Computer chose:\n" + scissors + "\nYou win!")
elif choice == 1: # if user chooses paper
  print(paper)
  if computer_choice == 0:
    print("Computer chose:\n" + rock + "\nYou win!")
  elif computer_choice == 1:
    print("Computer chose:\n" + paper + "\nIt's a draw!")
  else:
    print("Computer chose:\n" + scissors + "\nYou lose!")
elif choice == 2: # if user chooses scissors
  print(scissors)
  if computer_choice == 0:
    print("Computer chose:\n" + rock + "\nYou lose!")
  elif computer_choice == 1:
    print("Computer chose:\n" + paper + "\nYou win!")
  else:
    print("Computer chose:\n" + scissors + "\nIt's a draw!")
else: 
  print("You typed an invalid number, you lose!")


# Output:
  '''
  Welcme to the Rock, Paper, Scissors! : Python Edition
What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.
1

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

Computer chose:

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

You win!
  '''