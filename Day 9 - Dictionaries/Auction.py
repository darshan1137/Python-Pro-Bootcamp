end_of_game = False


bidders = {}

while end_of_game is False:
    name = input("Enter the Name of the Bidder: ")
    bid = int(input("Enter your Bid: $"))
    bidders[name] = bid
    check = input("Are there more Bidders (Type yes or no): ").lower()
    if check == "yes":
        end_of_game = False
    else:
        end_of_game = True

main_high = 0
win = ""

for i in bidders:
    high = bidders[i]
    if high > main_high:
        main_high = high
        win = i
        
    

print(f"{win} won with ${main_high} bid")
    
