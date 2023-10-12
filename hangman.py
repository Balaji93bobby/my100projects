#Step 5

import random
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
used_letters = []
end_of_game = False
lives = 6


from hangman_art import logo
print(logo)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    print(f"You had already used these letters{used_letters}")
    guess = input("Guess a letter: ").lower()
    clear()

    if guess in display:
        print(f"You've already guessed {guess}")
        used_letters.append(guess)

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:

        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        used_letters.append(guess)
        print(f"You had already used these letters{used_letters}")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose.\nThe choosen word is {chosen_word}")


    print(f"{' '.join(display)}")


    if "_" not in display:
        end_of_game = True
        print("You win.")

    from hangman_art import stages
    print(stages[lives])