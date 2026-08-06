import random

# List of potential secret words
fruits_list = ["apple", "banana", "grape", "orange", "mango"]

# Randomly choose a secret word
secret_word = random.choice(fruits_list)

# Task 3
def check_guess(guess): # Step 1
    guess = guess.lower() # Step 2
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():  # Step 1
    while True:
        guess = input("Guess a letter: ")  # Step 2
        if guess.isalpha() and len(guess) == 1:
            check_guess(guess)  # Step 3
            break  # Break the loop after a valid guess
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

ask_for_input()  # Step 4
# End of Task 3