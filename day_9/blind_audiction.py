import os # as duas funcoes abaixo sao usadas para limpar o console, para que o proximo apostador nao veja a aposta antiga
import time
from art import logo

print(logo)
print("Welcome to the secret auction program.")
flag = True

dictionary = {}
while flag ==True:
    flag_2 = True
  
    name = input("What is your name? ")
    bid = int(input("What`s your bid? "))
    dictionary[name]= bid
    while flag_2==True:

        x = input("Are there any other bidders? Type 'yes' or 'no' ")
        if x == "no":
            flag = False
            flag_2 = False
        elif x != "yes" and x != "no":
            print("type 'yes' or 'no' !!")
        else:
            time.sleep(1)
            os.system('cls')
            flag_2 = False
        







biggest_bid = 0
winner = ""
for i in dictionary:
  
    if dictionary[i] > biggest_bid:
        biggest_bid = dictionary[i]
        winner = i

print(f" The winner is {winner} with a bid of ${biggest_bid}.")


