import random
world_list=["ardvark","baboon","camel"]
size=len(world_list)
chosen_word = world_list[random.randint(0,size-1)]
#chosen_word = random.choice(world_list) pode ser feito assim tambem
guess = input("Guess a letter: ").lower()

# for i in range(0,len(chosen_word)):
#     if guess in chosen_word[i]:
#         print("Right") 
#     else:
#         print("Wrong") 
# pode ser feito desta forma acima, ou da forma abaixo
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")