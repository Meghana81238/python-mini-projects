import game_art as g
import random as r

words=['apple','potato','beautiful','mango','orange','student','teacher']
chosen_word=r.choice(words)
display=[]
for i in chosen_word:
    display+='_'
lives=6
print("let's play hangman!!")

print(f"you have only {lives} lives so try to guess the word within {lives} attempts! good luck!")
print(display)
game_over=False
while not game_over:
    guess=input("guess a letter:").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if guess==letter:
            display[position]=guess
    print(display) 
    if guess not in chosen_word:
        lives-=1
        print(f"you guessed {guess} that is not present in the word. so you lose a life")  
        #print(display)
        if lives==0:
            game_over=True
            print("you are out of lives ...game over!!")
    if '_' not in display:
        game_over=True
        print("congradulations... you win!!")      
    print(g.hangman_stages[6-lives])




