import random
import requests

class Hangman:
    def __init__(self, app_id, app_key, num_lives=5):
        """
        Initializes the Hangman game with a randomly chosen word and the number of lives.
        
        Args:
        app_id (str): Oxford Dictionaries API app ID.
        app_key (str): Oxford Dictionaries API app key.
        num_lives (int): Number of lives the player has.
        """
        self.app_id = app_id
        self.app_key = app_key
        self.num_lives = num_lives
        self.word, self.word_data = self.get_random_word()
        if not self.word:
            print("Could not fetch a word. Please check the API request or try again later.")
            return

        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        print(f"\nThe word has {len(self.word)} characters: {' '.join(self.word_guessed)}")

    def get_random_word(self):
        """
        Fetches a random word that starts with "A" from the Oxford Dictionaries API and its data.
        
        Returns:
        tuple: A tuple containing the word and a dictionary of its data.
        """
        # Simplified approach: Manually select a random word that starts with "A"
        predefined_words = ["apple", "anchor", "ask", "ability", "angle"]
        word = random.choice(predefined_words)
        word_data = self.fetch_word_data(word)
        return word, word_data

    def fetch_word_data(self, word):
        """
        Fetches data for the word from the Oxford Dictionaries API.
        
        Args:
        word (str): The word to fetch data for.
        
        Returns:
        dict: A dictionary containing the word's data.
        """
        endpoint = "entries"
        language_code = "en-gb"  # Sandbox environment typically uses en-gb
        url = f"https://od-api-sandbox.oxforddictionaries.com/api/v2/{endpoint}/{language_code}/{word.lower()}?fields=definitions,domains,etymologies,pronunciations,synonyms"
        r = requests.get(url, headers={"app_id": self.app_id, "app_key": self.app_key})
        
        if r.status_code == 200:
            data = r.json()
            lexical_entries = data['results'][0]['lexicalEntries'][0]
            definitions = ", ".join([sense['definitions'][0] for sense in lexical_entries['entries'][0]['senses']])
            domains = ", ".join(lexical_entries.get('domains', ['N/A']))
            etymologies = ", ".join(lexical_entries.get('entries', [{}])[0].get('etymologies', ['N/A']))
            pronunciations = ", ".join([pron['phoneticSpelling'] for pron in lexical_entries.get('pronunciations', [])])
            synonyms = ", ".join([syn['text'] for syn in lexical_entries['entries'][0].get('senses', [{}])[0].get('synonyms', [])])
            
            return {
                "definitions": definitions,
                "domains": domains,
                "etymologies": etymologies,
                "pronunciations": pronunciations,
                "synonyms": synonyms
            }
        else:
            print(f"Failed to fetch word data: {r.status_code}")
            return {}

    def _update_word_guessed(self, guess):
        for index, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[index] = guess
        self.num_letters -= 1

    def _handle_correct_guess(self, guess):
        self._update_word_guessed(guess)
        print(f"Good guess! {guess} is in the word.")
        print(f"\nThe word has {len(self.word)} characters: {' '.join(self.word_guessed)}")

    def _handle_incorrect_guess(self, guess):
        self.num_lives -= 1
        print(f"Sorry, {guess} is not in the word.")
        print(f"You have {self.num_lives} lives left.")

    def _is_valid_guess(self, guess):
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid letter. Please, enter a single alphabetical character.")
            return False
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
            return False
        return True

    def _check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            self._handle_correct_guess(guess)
        else:
            self._handle_incorrect_guess(guess)

    def ask_for_input(self):
        while True:
            guess = input("Please guess a letter: ").lower()
            if self._is_valid_guess(guess):
                self._check_guess(guess)
                self.list_of_guesses.append(guess)
                break

    def print_word_data(self):
        """
        Prints the word data including definitions, etymologies, pronunciations, etc.
        """
        print(f"\nThe word was: {self.word}")
        for key, value in self.word_data.items():
            print(f"{key.capitalize()}: {value}")

def play_game(app_id, app_key):
    print("Starting the game...")
    num_lives = 5
    game = Hangman(app_id, app_key, num_lives)

    if not game.word:
        print("Game cannot start without a valid word.")
        return

    while True:
        if game.num_lives == 0:
            print("You lost!")
            game.print_word_data()
            break
        elif '_' not in game.word_guessed:
            print("Congratulations! You won the game!")
            game.print_word_data()
            break
        else:
            game.ask_for_input()

# Replace with your actual app_id and app_key
app_id = "MY_ID"
app_key = "MY_KEY"
play_game(app_id, app_key)