import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choice = int(input(" What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if choice > 2:
    print("invalid number!")
else:
    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    else:
        print(scissors)

    print("computer chose:")
    computer_choice = [rock,paper,scissors]
    size = len(computer_choice) -1
    computer_random = random.randint(0,size)
    computer = computer_choice[computer_random]
    print(computer)
    if choice == 0:
        if computer == rock:
            print("Draw")
        elif computer == paper:
            print("You lose")
        elif computer == scissors:
            print("You win")
    elif choice == 1:
        if computer == rock:
            print("You win")
        elif computer == paper:
            print("Draw")
        elif computer == scissors:
            print("You lose")
    else:
        if computer == rock:
            print("You lose")
        elif computer == paper:
            print("You Win")
        elif computer == scissors:
            print("Draw")






