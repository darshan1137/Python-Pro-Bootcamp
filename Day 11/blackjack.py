import random

end = False
rear_end = False

user_cards = []
computer_cards = []

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    new_card = int(random.choice(cards))
    return new_card

def calculate(card_range):
    if sum(card_range) == 21 and len(card_range) == 2:
        return 0

    if 11 in card_range and sum(card_range) > 21:
        card_range.remove(11)
        card_range.append(1
    )
    total= sum(card_range)
    return total


def compare (user_score, computer_score):
    if user_score > computer_score and computer_score > 21:
        print("You went over. You lose")


    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You Lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You Win"
    else:
        return "You Lose" 


for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())

while not end:
    user_score = calculate(user_cards)
    computer_score = calculate(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]} ")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        end = True

    else:
        condition = input("Type 'y' to get another card or 'n' to pass: ")
        if condition == 'y':
            user_cards.append(deal_cards())
        else:
            end = True


while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_cards())
    computer_score = calculate(computer_cards)

print(f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
print(compare(user_score, computer_score))
