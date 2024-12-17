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

import random

#user input
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
#computer choice
computer_choice = random.randint(0, 2)
#print user choice
if user_choice == 0:
  print(rock)
elif user_choice == 1:
  print(paper)
elif user_choice == 2:
  print(scissors)
else:
  print("Invalid input")
#print computer choice
print("Computer chose:")
if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
elif computer_choice == 2:
    print(scissors)
#determine winner
if user_choice == computer_choice:
  print("It's a tie!")
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif user_choice == 1 and computer_choice == 0:
  print("You win!")
elif user_choice == 2 and computer_choice == 1:
  print("You win!")
else:
  print("You lose!")
