import random
world_list=["ardvark","baboon","camel"]
size=len(world_list)
chosen_word = world_list[random.randint(0,size-1)]

guess = input("Guess a letter: ")
guess = guess.lower()
# for i in range(0,len(chosen_word)):
#     if guess in chosen_word[i]:
#         print("Right")
#     else:
#         print("Wrong")
print(chosen_word)
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")