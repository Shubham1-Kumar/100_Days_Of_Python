import random
from random import randint
from traceback import format_list
from game_data import data
from art import logo,vs

def Higher_Lower(game_data):
    print(logo)
    score = 0
    flag = True
    while flag:
        A = random.choice(data)
        B = random.choice(data)
        print("Compare A :", A['name'], "a", A['description'], "from", A['country'])
        print(vs)
        print("Against B :", B['name'], "a", B['description'], "from", B['country'])

        response = input("Who has more follower chore either 'A' or 'B' ").lower()
        if A['follower_count'] > B['follower_count'] and response == 'a':
            score += 1
            print("Your are correct and your current score is : ", score)
        elif B['follower_count'] > A['follower_count'] and response == 'b':
            score += 1
            print("Your are correct and your current score is : ", score)
        elif B['follower_count'] == A['follower_count']:
            print("Its a Draw")
            print("Your current score is : ", score)
        else:
            print("You are wrong", "Your current score is :", score)
            flag = False

Higher_Lower(game_data=data)
