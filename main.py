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

choices = [rock, paper, scissors]

users_pick = int(input("What do you choose?  type 0 for Rock, type 1 for Paper, or 3 for Scissors?\n"))

print (choices[users_pick])

random_pick= random.randint(0, 2)


print(f"The computer chose: \b{choices[random_pick]}")


if users_pick > random_pick:
  if users_pick == 2 and random_pick == 0:
    print("You lose!")
  else:
    print("You win!")
elif users_pick == 0 and random_pick == 2:
  print ("You win!")
elif random_pick == users_pick:
  print("You tied!")
else:
  print("You lose!")
