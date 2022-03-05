import random
import hangman_art
import hangman_words


word_list = ["monkey", "baby", "leaf", "tree"]

no_of_lives = 6

stage = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word = random.choice(hangman_words.word_list)
#print(word)

from hangman_art import logo

print(logo)

display = []
for char in word:
    char = "_"
    display += char

print(display)


end_of_game = False

while not end_of_game:
    guess = input("Guess a Letter:").lower()    


    if guess in display:
        print("You have already guessed the Word")
    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
            display[position] =letter

    if guess not in word:
        print("You have guessed a incorrect letter, You lose a Life")
        no_of_lives -= 1
    if no_of_lives == 0:
        end_of_game = True
        print("You Lost")

    print(display)
    attempts = 6
    if "_" not in display:
        end_of_game = True
        print("You Won")


    print(stage[no_of_lives])