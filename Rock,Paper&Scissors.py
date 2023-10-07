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

game = [rock, paper, scissors]

print("Welcome to the famous Rock, Paper & Scissors Game")
user = int(input("Choose your choice. 0 for Rock, 1 for Paper and 2 for Scissors\n"))

if user >= 3 or user < 0:
    print("You have chosen the wrong choice")
else:
    print("You chose:")
    print(game[user])
    computer = random.randint(0, 2)
    print("computer chose:")
    print(game[computer])
    if user == 0 and computer == 2:
        print("You win!")
    elif user == computer:
        print("It's a draw")
    elif computer == 0 and user == 2:
        print("You lose")
    elif user > computer:
        print("You win!")
    elif computer > user:
        print("You lose")