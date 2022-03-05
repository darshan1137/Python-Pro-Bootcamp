import random
word_list = ["monkey", "baby", "leaf", "tree"]

word = random.choice(word_list)

guess = input("Guess a Letter:").lower()

for letter in word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")