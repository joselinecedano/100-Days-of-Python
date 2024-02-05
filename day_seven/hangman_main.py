'''
This is a game called Hangman. The player is presented with a series of blanks that represent the letters in a word. The player guesses a letter and if that letter is in the word, the blanks are replaced with the letter. If the letter is not in the word, the player loses a life. The player wins if they guess all the letters in the word before they run out of lives.
'''

import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Print Ascii Art Hangman Logo
print(hangman_art.logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print("Yay! You guessed a letter!\n")

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f"Ooops ... Try again!\nLives left: {lives}\n")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Print the stages of the hangman
    print(hangman_art.stages[lives])



# Returns the following:
'''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
Guess a letter: j
Yay! You guessed a letter!

j _ _ _ _ _

  +---+
  |   |
      |
      |
      |
      |
=========

Guess a letter: o
Ooops ... Try again!
Lives left: 5

j _ _ _ _ _

  +---+
  |   |
  O   |
      |
      |
      |
=========

Guess a letter: k
Ooops ... Try again!
Lives left: 4

j _ _ _ _ _

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

Guess a letter: a
Yay! You guessed a letter!

j _ _ _ a _

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

Guess a letter: s
Yay! You guessed a letter!

j _ _ s a _

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

Guess a letter: p
Ooops ... Try again!
Lives left: 3

j _ _ s a _

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
Guess a letter: r
Ooops ... Try again!
Lives left: 2

j _ _ s a _

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

Guess a letter: e
Ooops ... Try again!
Lives left: 1

j _ _ s a _

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========

Guess a letter: w
Yay! You guessed a letter!

j _ _ s a w

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========

Guess a letter: i
Yay! You guessed a letter!

j i _ s a w

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========

Guess a letter: g
Yay! You guessed a letter!

j i g s a w
You win.

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
'''