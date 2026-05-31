import random
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5


    
def difficulty_level(level):
    if level=='easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS
        
def check_answer(guess,answer,attempt):
    if guess < answer:
        print("your guess is too low")
        return attempt -1
    elif guess > answer:
        print("your guess is too high") 
        return attempt -1  
    else:
        print(f"your guess is right...the number was {guess}")
    
    
def game():
    print("let me think of a number between 1 to 50")
    answer=random.randint(1,50)
    level=input("enter the difficulty level.. type 'hard' or 'easy' ")
    guess=0
    attempt=difficulty_level(level)
    while guess != answer:
        print(f"you have {attempt} attempts to guess a number")
        guess=int(input("guess a number:"))
        attempt=check_answer(guess,answer,attempt)
        
        if attempt==0:
            print("you are out of guesses ..you lose!")
            return
        elif guess !=answer:
            print("guess again")
            
game()