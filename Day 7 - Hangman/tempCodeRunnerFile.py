    guess = input("Guess a Letter:").lower()    

    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
            display[position] =letter

    print(display)