import random 

choice = int(input("Enter your Choice:\n Type 1 for Rock\n Type 2 for Paper\n Type 3 for Scissors\n "))
if choice == 1:
    choice = "rock"
    print("Your Choice is rock")
elif choice ==2:
    choice = "paper"
    print("Your Choice is papers")
elif choice == 3:
    choice = "scissors"
    print("Your Choice is scissors")
else:
    print("Invalid Input")

bot= random.choice(["rock", "paper", "scissors"])

print("Opponent Chooses: " + bot)

if choice == bot:
    print("Match Tied")

if choice == "rock":
    if bot == "scissors":
        print("You Won")
    elif bot == "paper":
        print("You Lost") 

if choice == "scissors":
    if bot == "rock":
        print("You Lost")
    elif bot == "paper":
        print("You Won") 

if choice == "paper":
    if bot == "scissors":
        print("You Lost")
    elif bot == "rock":
        print("You Won") 