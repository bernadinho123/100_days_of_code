from art import logo
import random
import os # as duas funcoes abaixo sao usadas para limpar o console, para que o proximo apostador nao veja a aposta antiga
import time
flag1 = True
def ace(list):
    x =0
    k = 0
    for i in list:
        if i == 11:
            k+=1
    if k>1:
           for i in list:
               if i == 11:
                  x = list.index(i)
           list[x] = 1     

while flag1 == True:

    play =  input("Do you want to play BlackJack? Type 'y' or 'n' : ")
    if play == 'y':
        time.sleep(1)
        os.system('cls')
        print(logo)
        cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
        list_computer = []
        list_player = []
        list_computer.append(random.choice(cards))
        list_computer.append(random.choice(cards))
        list_player.append(random.choice(cards))
        list_player.append(random.choice(cards))
        ace(list_computer)
        ace(list_player)
        soma1= list_player[0]+ list_player[1]
        soma1_computer = list_computer[0] + list_computer[1]

        print(f" Your cards:{list_player},current score:{soma1}")
        print(f" Computer`s first card : {list_computer[0]}")
        continue_playing = input(" Type 'y' to get another card, type 'n' to pass: ")
        if continue_playing == 'y':
          

            if (soma1_computer) < 16 :
                list_computer.append(random.choice(cards))
                soma1_computer = soma1_computer + list_computer[2]
            list_player.append(random.choice(cards))
            soma1 = soma1 + list_player[2]
            ace(list_computer)
            ace(list_player)
            if soma1_computer == 21:
                 print(f" Your cards:{list_player},current score: {soma1}")
                 print(f" Computer`s first card : {list_computer[0]}")
                 print(f"Your final hand: {list_player}, final score: {soma1}")
                 print(f"Computer`s final hand: {list_computer}, final score: {soma1_computer}")
                 print("You Lose 🥲")
            if (soma1)==( soma1_computer):
                 print(f" Your cards:{list_player},current score: {soma1}")
                 print(f" Computer`s first card : {list_computer[0]}")
                 print(f"Your final hand: {list_player}, final score: {soma1}")
                 print(f"Computer`s final hand: {list_computer}, final score: {soma1_computer}")
                 print("DRAW!")

            elif soma1>21 or  soma1_computer>soma1 :
                 print(f" Your cards:{list_player},current score: {soma1}")
                 print(f" Computer`s first card : {list_computer[0]}")
                 print(f"Your final hand: {list_player}, final score: {soma1}")
                 print(f"Computer`s final hand: {list_computer}, final score: {soma1_computer}")
                 print("You Lose 🥲")
            elif soma1<= 21 or soma1> soma1_computer :
                 print(f" Your cards:{list_player},current score: {soma1}")
                 print(f" Computer`s first card : {list_computer[0]}")
                 print(f"Your final hand: {list_player}, final score: {soma1}")
                 print(f"Computer`s final hand: {list_computer}, final score: {soma1_computer}")
                 print("You WIN 😊")
        else:
            
            if (soma1_computer) < 16 :
                list_computer.append(random.choice(cards))
                soma1_computer = soma1_computer + list_computer[2]
                ace(list_computer)
                ace(list_player)
            if soma1_computer == 21:
                 print(f" Your cards:{list_player},current score: {soma1}")
                 print(f" Computer`s first card : {list_computer[0]}")
                 print(f"Your final hand: {list_player}, final score: {soma1}")
                 print(f"Computer`s final hand: {list_computer}, final score: {soma1_computer}")
                 print("You Lose 🥲")
            if (soma1)==( soma1_computer):
                 print(f" Your cards:{list_player},current score: {soma1}")
                 print(f" Computer`s first card : {list_computer[0]}")
                 print(f"Your final hand: {list_player}, final score: {soma1}")
                 print(f"Computer`s final hand: {list_computer}, final score: {soma1_computer}")
                 print("DRAW!")

            elif soma1>21 or  soma1_computer>soma1 :
                 print(f" Your cards:{list_player},current score:{soma1}")
                 print(f" Computer`s first card : {list_computer[0]}")
                 print(f"Your final hand: {list_player}, final score: {soma1}")
                 print(f"Computer`s final hand: {list_computer}, final score: {soma1_computer}")
                 print("You Lose 🥲")
            elif soma1<= 21 or soma1> soma1_computer :
                 print(f" Your cards:{list_player},current score:{soma1}")
                 print(f" Computer`s first card : {list_computer[0]}")
                 print(f"Your final hand: {list_player}, final score: {soma1}")
                 print(f"Computer`s final hand: {list_computer}, final score: {soma1_computer}")
                 print("You WIN 😊")
            



     

    elif play == 'n':
        flag1 = False
    else:
        print("TYPE 'y' or 'n' !!")