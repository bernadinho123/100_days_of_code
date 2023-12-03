import random
from hangman_logo import logo
from animals import list
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
lives=6
lives_count = 0
print(logo)

size=len(list)
chosen_word = list[random.randint(0,size-1)]
#chosen_word = random.choice(world_list) pode ser feito assim tambem
display = []
for i in range(0,len(chosen_word)):
    display.append("_")

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print("you have chosen this world before")
    else:
        if guess not in chosen_word:
            print(HANGMANPICS[lives_count])
            lives_count += 1
            lives -= 1

        for i in range(0,len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        print(display)
        if "_" not in display:
            end_of_game = True
            print("you win")
        elif lives < 0:
            end_of_game = True
            print("you lose")

            



