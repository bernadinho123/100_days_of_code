import random
from art import logo
from art import vs
from game_data import data
import os # as duas funcoes abaixo sao usadas para limpar o console, para que o proximo apostador nao veja a aposta antiga
import time
def generate_random(data):
    i= random.choice(data)
    return i



def format_A (list):
    print(f"Compare A: {list['name']}, a {list['description']}, from {list['country']}.")

def format_B (list):
    print(f"Against B: {list['name']}, a {list['description']}, from {list['country']}.")

flag = True



A =generate_random(data)
B = generate_random(data)
score = 0
while flag ==True:
    print(logo)
    format_A(A)
    print(vs)
    format_B(B)
    question = input("Who has more followers? Type 'A' or 'B': ")
    if question == 'A':
        if A['follower_count'] > B['follower_count']:
            score +=1
            print(f"You are right, current score: {score}")
            time.sleep(2)
            os.system('cls')
            B = generate_random(data)

        elif A['follower_count'] < B['follower_count']:
             print(f"Sorry, thas is wrong , final score: {score}")
             flag = False
    elif question == 'B':
        if B['follower_count'] > A['follower_count']:
            score +=1
            print(f"You are right, current score: {score}")
            time.sleep(2)
            os.system('cls')
            A = B
            B = generate_random(data)

        elif B['follower_count'] < A['follower_count']:
             print(f"Sorry, thas is wrong , final score: {score}")
             flag = False







