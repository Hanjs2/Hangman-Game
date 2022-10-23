# Hangman Project
import random
# imports larger list of word choices from the word_list file 
from word_list import word_list
# imports items from art.py such as the logo and the stages of hangman
from art import logo
from art import stages

print(logo)
# Randomly choose a word from  word_list and assign it to a variable called chosen_word
chosen_word=random.choice(word_list)
upper_word=chosen_word.upper()

# # Testing code / hint
# print(chosen_word)

display=[]

for word in range(len(chosen_word)):
    display+="_"

end_game=False
# when end of game is true it results to end of program
lives=6
# Creates new variable==to false
while not end_game:
# creates while loop that when the condition is not end_game(False) then loop the entire function
    # Create an input function for the user and assign it to a variable called guess
    guess=input("Guess a Letter: ").lower()
    
    # If the letter is already guessed then print the following statement 
    if guess in display:
        print("You've already guessed this letter. Try again")
   
    for position in range(len(chosen_word)):
        word=chosen_word[position]
        if word==guess:
            display[position]=word
      
    # When a lettere is wrong then lives will be subtracted by 1 and print the following statement below  
    if guess not in chosen_word:
        lives-=1
        print("You guessed a wrong letter so you will now loose a life")
        print(lives)
        # When lives reaches zero then end_game is true and you loose the game
        if lives==0:
            end_game=True
            print("You loose")     
            print(f"The word was {upper_word}")
         
    print(f"{' '.join(display)}")
    # prints display in the form of a string instead of a list of items
    
    # if the display list does not contain anyore blanks then print you win
    if "_" not in display:
        end_game==True
        print("You win")
        break
       
        
    print(stages[lives])
    # prints the stages in correspondance to the number of lives
   

    









   


    
    
    
    




# Create a blank list called display
