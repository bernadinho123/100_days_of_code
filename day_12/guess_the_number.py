import random
from art import logo


flag = True
while flag == True:
    print(logo)
    print("Welcome to the Number Guessing Game!")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = 0 
    if level == 'easy':
        attempts = 10
        number = random.randint(1,100)
        while attempts >=1:
            print(F"You have {attempts} remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess == number:
                print(f"You got it! The answer was {number}.")
                attempts = 0
            elif guess > number :
                attempts -=1
                if attempts != 0:
                    print("Too High\nGuess again")
                else:
                    print("You`ve run out of guesses.You lose!") 
            else:
                attempts -=1
                if attempts != 0:
                    print("Too Low\nGuess again")
                else:
                    print("You`ve run out of guesses.You lose!") 
    elif level == 'hard':
        attempts = 5 
        number = random.randint(1,100)
        while attempts >=1:
            print(F"You have {attempts} remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess == number:
                print(f"You got it! The answer was {number}.")
                attempts = 0
            elif guess > number :
                attempts -=1
                if attempts != 0:
                    print("Too High\nGuess again")
                else:
                    print("You`ve run out of guesses.You lose!") 
            else:
                attempts -=1
                if attempts != 0:
                    print("Too Low\nGuess again")
                else:
                    print("You`ve run out of guesses.You lose!") 
              
    else:
        print("Type again ! U gotta chose 'easy' or 'hard'!")


