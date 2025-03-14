import random
from game_data import data
from art import logo, vs

def get_card(cards: list[dict]):
    card = random.choice(cards)
    return card

def high_or_low():
    score = 0
    first_card = get_card(data)

    game = True

    while game:
        print(logo)
        print(f"Your current score is : {score}")
        second_card = get_card(data)
        print(f"Compare A: {first_card['name']}, a {first_card['description']}, from {first_card['country']}.")
        print(vs)
        print(f"Compare B: {second_card['name']}, a {second_card['description']}, from {second_card['country']}.")

        answer = input("Who has more followers? Type 'A' or 'B': ")

        if answer == 'A' and first_card['follower_count'] > second_card['follower_count']:
            score += 1

        elif answer == 'B' and first_card['follower_count'] < second_card['follower_count']:
            score +=1
            first_card = second_card

        else:
            print(f"Sorry that's wrong. Your final score is {score}")
            break

high_or_low()