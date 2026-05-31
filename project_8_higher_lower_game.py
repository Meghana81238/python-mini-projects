import game_database
import game_art
import random
import os

print(game_art.game_logo)

score=0
def display_accountinfo(account):
    name=account['name']
    description=account["description"]
    country=account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess,follower_1,follower_2):
    if follower_1>follower_2:
        if guess==1:
            return True
        else:
            return False
    else:
        if guess==2:
            return True
        else:
            return False    

score=0
account2=random.choice(game_database.data)
continue_flag=True
while continue_flag:
    account1=account2
    account2=random.choice(game_database.data)


    while account1==account2:
        account2=random.choice(game_database.data)
    print(f"compare1:{display_accountinfo(account1)}") 
    print(game_art.vs)   
    print(f"compare2:{display_accountinfo(account2)}")
    guess=int(input("who has more followers? type 1 or 2"))
    follower_1=account1["follower_count"]
    follower_2=account2["follower_count"]

    is_correct=check_answer(guess,follower_1,follower_2)

    os.system('cls')

    print(game_art.game_logo)

    if is_correct:
        score+=1
        print(f"you are right your current score is :{score}")
    else:
        print(f"you are wrong...your final score is {score}")  
        continue_flag=False  




