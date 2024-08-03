import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initialszes the Hangman game with a list of possible words and the number of lives.
        
        Args:
        word_list (list): List of words for the Hangman game.
        num_lives (int): Number of lives the player has.
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def _update_word_guessed(self, guess):
        """
        Updates the word guessed list with the correctly guessed letter.
        
        Args:
        guess (str): The correctly guessed letter.
        """
        for index, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[index] = guess
        self.num_letters -= 1

    def _handle_correct_guess(self, guess):
        """
        Handles the logic when the player guesses a correct letter.
        
        Args:
        guess (str): The correctly guessed letter.
        """
        print(f"Good guess! {guess} is in the word.")
        self._update_word_guessed(guess)

    def _handle_incorrect_guess(self, guess):
        """
        Handles the logic when the player guesses an incorrect letter.
        
        Args:
        guess (str): The incorrectly guessed letter.
        """
        self.num_lives -= 1
        print(f"Sorry, {guess} is not in the word.")
        print(f"You have {self.num_lives} lives left.")

    def _is_valid_guess(self, guess):
        """
        Validates the player's guess.
        
        Args:
        guess (str): The player's guessed letter.
        
        Returns:
        bool: True if the guess is valid, False otherwise.
        """
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid letter. Please, enter a single alphabetical character.")
            return False
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
            return False
        return True

    def _check_guess(self, guess):
        """
        Checks if the guessed letter is in the word.
        
        Args:
        guess (str): The player's guessed letter.
        """
        guess = guess.lower()
        if guess in self.word:
            self._handle_correct_guess(guess)
        else:
            self._handle_incorrect_guess(guess)

    def ask_for_input(self):
        """
        Continuously prompts the player to guess a letter until a valid guess is made.
        """
        while True:
            guess = input("Please guess a letter: ").lower()
            if self._is_valid_guess(guess):
                self._check_guess(guess)
                self.list_of_guesses.append(guess)
                break