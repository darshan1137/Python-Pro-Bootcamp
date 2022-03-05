import random
from tkinter import N
word_list = ["monkey", "baby", "leaf", "tree"]

word = random.choice(word_list)
print(word)

display = []
for char in word:
    char = "_"
    display += char

print(display)


end_of_game = False

while not end_of_game:
    guess = input("Guess a Letter:").lower()    

    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
            display[position] =letter

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Won")