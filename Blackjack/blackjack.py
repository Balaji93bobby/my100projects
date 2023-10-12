import random
from blackjack_art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    """takes a list of cards and return the score of calculated cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) < 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return("Draw")
    elif computer_score == 0:
        return("Lose, Opponent has a blackjack")
    elif user_score == 0:
        return("You win, You have a blackjack")
    elif user_score > 21:
        return("You lose, You have a deal more than 21")
    elif computer_score > 21:
        return("You win, Opponent has a deal more than 21")
    elif user_score > computer_score:
        return("You win")
    else:
        return("You lose")

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    for i in range(2):
        computer_cards.append(deal_card())
        user_cards.append(deal_card())
    print(user_cards)
    print(computer_cards)
    if_game_over = False
    while not if_game_over:


        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards : {user_cards}")
        print(f"Computer second card : {computer_cards[0]}")




        if user_score == 0 or computer_score == 0 or user_score > 21:
            if_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card  or type 'n' to deal : ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                if_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":

  play_game()