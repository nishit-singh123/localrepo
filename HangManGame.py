import random
import testing
#word_list=['apple','beautiful','potato']
lives=6
chosen_word=random.choice(testing.words)
print(chosen_word)
display=[]
for i in range(len(chosen_word)):
    display+='-'
print(display)
game_over=False
while not game_over:
    guessed_letter=input('Guess a letter:')
    for position in range(len( chosen_word)):
        letter=chosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)        
    if guessed_letter not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print('you lose')

    if '-'not in display:
        game_over=True
        print('you win') 
    
     
   