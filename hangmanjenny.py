import random 
import hangman1
import word_file
#word_list=["apple", "beautiful", "potato")
lives=6
chosen_word=random. choice(word_file.words)
print(chosen_word)
display=[]
for i in range(len(chosen_word)): #0 2 2 3 4 5 RaPPLe
    display += "_"
print (display)
game_over=False
while not game_over:
    guessed_letter=input("Guess a letter: "). lower () 
    
    for position in range(len(chosen_word)):#0 2 2 5
        letter = chosen_word [position]
    if letter==guessed_letter: #P F= X
        display[position]= guessed_letter
    print (display)
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print ("You lose! 1")
    if'_'not in display:
        game_over=True
        print("you win!!")
    print(hangman1.stages[lives])