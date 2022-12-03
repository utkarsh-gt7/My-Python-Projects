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


player_sign=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if player_sign==0:
    print(rock,"Player Sign")
elif player_sign==1:
    print(paper,"Player Sign")
elif player_sign==2:
    print(scissors,"Player Sign")

computer_choices=[rock,paper,scissors]
computer_choice_index=random.randint(0,2)
computer_sign=(computer_choices[computer_choice_index])
print(computer_sign,"Computer Sign")

if (player_sign==0 and computer_sign==rock) or (player_sign==1 and computer_sign==paper) or (player_sign==2 and computer_sign==scissors):
    print("Draw")
elif player_sign==0 and computer_sign==scissors:
    print("Player Won")
elif player_sign==1 and computer_sign==rock:
    print("Player Won")
elif player_sign==2 and computer_sign==paper:
    print("Player Won")
elif player_sign==1 and computer_sign==scissors:
    print("Computer Won")
elif player_sign==0 and computer_sign==paper:
    print("Computer Won")
elif player_sign==2 and computer_sign==rock:
    print("Computer Won")
else:
    print("No declaration")
