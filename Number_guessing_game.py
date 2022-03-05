import random


art = '''
   _____                                _     _                _   _                       _                   
  / ____|                              | |   | |              | \ | |                     | |                  
 | |  __   _   _    ___   ___   ___    | |_  | |__     ___    |  \| |  _   _   _ __ ___   | |__     ___   _ __ 
 | | |_ | | | | |  / _ \ / __| / __|   | __| | '_ \   / _ \   | . ` | | | | | | '_ ` _ \  | '_ \   / _ \ | '__|
 | |__| | | |_| | |  __/ \__ \ \__ \   | |_  | | | | |  __/   | |\  | | |_| | | | | | | | | |_) | |  __/ | |   
  \_____|  \__,_|  \___| |___/ |___/    \__| |_| |_|  \___|   |_| \_|  \__,_| |_| |_| |_| |_.__/   \___| |_|   
                                                                                                               
                                                                                                               
'''
number = random.randint(1, 101)
no_of_guess = 0
end_of_game = False
print(art)

while not end_of_game:
    guess = int(input("Guess the Number: "))
    
    if guess == number:
        no_of_guess += 1
        end_of_game = True
        print(f"You guessed the correct Number in {no_of_guess} guesses")

    elif guess > number:
        no_of_guess += 1
        print("The Number is smaller than guess Number")

    elif guess < number:
        no_of_guess += 1
        print("The Number is greater than guess Number")


