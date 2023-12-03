import random
world_list=["ardvark","baboon","camel"]
size=len(world_list)
chosen_word = world_list[random.randint(0,size-1)]
#chosen_word = random.choice(world_list) pode ser feito assim tambem
guess = input("Guess a letter: ").lower()
display = []
for i in range(0,len(chosen_word)):
    display.append("_")
    if chosen_word[i] == guess:
        display[i] = guess
        
print(chosen_word)
    
print(display)
print(str(display))

# for letter in chosen_word:
#     if letter == guess:
#         display.insert()
        
#     else:
#         print("Wrong")