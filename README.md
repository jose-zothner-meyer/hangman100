# Hangman Game
#### Under develpment. <br> Updated: 02/07/2024

## Overview
<p>Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within X amount of attempts.</p>

<div style="display: flex; flex-direction: row;">
    <img src="./images/hangman_lost.png" alt="Hangman lost Image" style="width: 45%; margin-right: 5%;">
    <img src="./images/hangman_won.png" alt="Hangman won Image" style="width: 45%;">
</div>

<div style="text-align: right; font-size: small;">
    <p><i>Source: DALL-E by OpenAI</i></p>
</div>
<br>
<p>This is an implementation of the Hangman game, where the computer thinks of a random word and the player/user tries to guess it.</p>

## Credits
As an analogy, imagine the english alphabet: I began my coding journey at ‘M,’ skipping the first twelve letters.
<br>
The knowledge contained in this repository was primarily taught by <a href='https://www.theaicore.com' > AiCore</a>, and I am immensely grateful to them for their teaching and support in my continous professional development.

## Table of contents
1. [Overview](#overview)
2. [Milestones](#milestones)
    - [2.1: Set up the environment](#21-set-up-the-environment)
      - [2.1.1 OS Terminal](#211-os-terminal)
      - [2.1.2 Conda Virtual Environment](#212-conda-virtual-environment)
      - [2.1.3 Git](#213-git)
      - [2.1.4 GitHub](#214-github)
    - [2.2: Create the variables for the game](#22-create-the-variable-for-the-game)
      - [2.2.1 Define the list of possible words](#221-define-the-list-of-possible-words)
      - [2.2.2 Choose a random word from the list](#222-choose-a-random-word-from-the-list)
      - [2.2.3 Ask the player/user for an input](#223-ask-the-playeruser-for-an-input)
      - [2.2.4 Check that the input is a single character](#224-check-that-the-input-is-a-single-character)
      - [2.2.5 Start documenting my experience](#225-start-documenting-my-experience)
      - [2.2.6 Update the latest code changes to GitHub](#226-update-the-latest-code-changes-to-github)
      - [2.2.7 Refactor and optimise current code](#227-refactor-and-optimise-current-code)
    - [2.3: Check if the guessed character is in the word](#23-check-if-the-guessed-character-is-in-the-word)
      - [2.3.1 Implement the function to check the guessed character](#231-implement-the-function-to-check-the-guessed-character)
      - [2.3.2 Implement the function to ask for user input](#232-implement-the-function-to-ask-for-user-input)
    - [2.4: Create the Game class](#24-create-the-game-class)
      - [2.4.1 Define the \_\_init_\_ method](#241-define-the-__init__-method)
      - [2.4.2 Implement the function to check the guessed character](#242-implement-the-function-to-check-the-guessed-character)
      - [2.4.3 Implement the function to ask for user input](#243-implement-the-function-to-ask-for-user-input)
      - [2.4.4 Refactor and optimise current code](#244-refactor-and-optimise-current-code)
    - [2.5: Putting it all together](#25-putting-it-all-together)
      - [2.5.1 Subchapter One](#251-subchapter-one)
      - [2.5.2 Subchapter Two](#252-subchapter-two)
3. [Installation](#installation-instructions)
4. [Usage](#usage-instructions)
5. [File Structure](#file-structure)
6. [License Information](#license-information)
7. [Demonstrated Skills](#demonstrated-skills)

## Milestones
This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. In order to achieve developing this game, I categorised it in milestones, which each has a specific subset of chapters.

### 2.1: Set up the environment
The first step in setting up the environment was to navigate and create a new directory on my local machine using the OS terminal.

#### 2.1.1 OS Terminal
<p>This was done with the following commands:</p>

```
cd /path/to/parent-directory
mkdir hangman
cd hangman
```

#### 2.1.2 Conda Virtual Environment
Next, I created and initialized a new Conda virtual environment. This helps manage dependencies and keep them isolated from other projects. I also needed to download essential packages, such as _Python_ and _random_.

```
# Create a new Conda environment with Python
conda create -n hangman python=3.8

# Activate the  created environment
conda activate hangman

# Install the random module
conda install random
```

#### 2.1.3 Git
To manage the project’s version control, I initialized a Git repository, cloned the GitHub repository, and performed some basic Git operations.

```
# Initialize a new Git repository
git init

# Clone the existing GitHub repository
git clone https://github.com/your-username/repository.git

# Navigate into the cloned repository
cd hangman

# Check the current status of the repository
git status

# Add all changes to staging
git add .

# Commit the changes with a message
git commit -m "Initial commit: Add cloned repo Hangman."

# Create a new branch for development
git branch -M main
```

#### 2.1.4 GitHub
Finally, once I want to push the local repository to GitHub, to keep it backed up and share it with others, I write the following commands:

```
# Set the remote origin to the GitHub repository
git remote add origin https://github.com/your-username/hangman-project.git

# Push the changes to the remote repository
git push -u origin main
```

### 2.2: Create the variables for the game

#### 2.2.1 Define the list of possible words
<p>Created a file named _milestone_2.py_.<br>This file will contain the code for the first milestone.
In Python, lists are used to store multiple data in a single variable. In this task, I am going to create a list of words.</p>

Steps:
- Created a list containing the names of my five (5) favorite fruits.
- Assigned the list to a variable called word_list
- Printed out the created list to the standard output/terminal

#### 2.2.2 Choose a random word from the list
To accomplish this task, I needed to use the `random` module.<br>
The random module is one of Python’s built-in modules.
It has a _choice_ method which returns a random item from a given sequence.

Steps:
- Wrote `import random` on the first line of my Python code
- Created the `random.choice` method and passed the _word_list_ variable into the choice method
- Assigned the randomly generated word to a variable called _word_
- Printed out word to the standard output. Ran the code several times and observed the words printed out after each run.

#### 2.2.3 Ask the player/user for an input
As you now know, the `print()` function in Python displays output on the screen. Conversely, Python has an `input()` function that takes input from the screen. Note that the input function returns the user input in the form of a string.

Steps:
- Using the `input` function, I asked the user to enter a single letter.
- Assigned the input to a variable called _guess_.

#### 2.2.4 Check that the input is a single character
Usually, when taking input from users, it is best to validate that the input makes sense.
For example, we may want to ensure that only a single letter is entered and that only alphabetical characters are provided by the user.<br>
To do this, create conditional checks that must be passed before the input can be accepted.

Steps:
- Created an `if` statement that checks if the length, `len(variable)`, of the input is equal to 1 AND the input is alphabetical.
- In the body of the `if` statement, printed a message that says “Good guess!”.
- Created an `else` block that prints “Oops! That is not a valid input.” if the preceding conditions are not met.

#### 2.2.5 Start documenting my experience
Added documentation to my GitHub <b>README.md</b> file.<br> I referred to the relevant material from <b>AiCore</b> for this task.
As per the course's suggestion, my README file should contain certain specific information for the reader's understanding and guidance.

#### 2.2.6 Update the latest code changes to GitHub
Updated my GitHub repository with the latest code changes from my local machine. Started by staging the modifications and creating a commit. Then, pushed the changes to my GitHub repository.

```
# 1. Stage all the changes
git add .

# 2. Commit the changes with a descriptive message
git commit -m "Add code for creating variables and user input validation"

# Push the changes to the remote repository (the first push needs to be in this format)
git push -u origin main

# Once that is done you can simply push it (after part 1 and 2 of the process) by following this command:
git push
```

#### 2.2.7 Refactor and optimise current code
As my tutors say: "Refactoring will be a continuous and constant process, but this is the time to really scrutinise your code."

### 2.3: Check if the guessed character is in the word
In this milestone I am checking if the guessede letter is in the randomly chosen word.

#### 2.3.1 Implement the function to check the guessed character
<p>Created a file named _milestone_3.py_ and updated the existing code.<br>
The aim is to create a function that checks `if` the guessed character is in the _secret word_.</p>

Steps:
- Created a function named `check_guess` that takes `guess` as a parameter.
- Converted the `guess` to lowercase to ensure consistency.
- Used an `if` statement to check if the `guess` is in the `secret_word`.
- If the `guess` is in the `secret_word`, printed a message saying "Good guess! {guess} is in the word."
- Otherwise, printed a message saying "Sorry, {guess} is not in the word. Try again."

#### 2.3.2 Implement the function to ask for user input
<p>The next step is to create a function that asks the player for input and validates the input.</p>

Steps:
- Created a function named `ask_for_input`.
- Used a `while True` loop to continuously ask the user for a guess until a valid input is provided.
- Inside the loop, used the `input` function to ask the player to "Guess a letter".
- Checked if the input is a single alphabetical character.
- If the input is valid, called the `check_guess` function and passed the input.
- Used `break` to exit the loop after a valid guess.
- If the input is invalid, printed "Invalid letter. Please, enter a single alphabetical character."


### 2.4: Create the Game class
Creating the class **Game**: 

#### 2.4.1 Define the `__init__` method
Steps:
- Created a class called `Hangman`.
- Defined an `__init__` method to initialize the attributes of the class.
- Passed `word_list` and `num_lives` as parameters to the `__init__` method, with `num_lives` having a default value of 5.
- Initialized the following attributes:
  - `word`: The word to be guessed, picked randomly from the `word_list`.
  - `word_guessed`: A list of underscores representing the letters of the word not yet guessed.
  - `num_letters`: The number of unique letters in the word that have not been guessed yet.
  - `num_lives`: The number of lives the player has at the start of the game.
  - `word_list`: The list of words.
  - `list_of_guesses`: A list of the guesses that have already been tried.

#### 2.4.2 Implement the function to check the guessed character
Steps:
- Created a method called check_guess that takes guess as a parameter.
- Converted the guessed letter to lowercase.
- Created an `if` statement to check if the guess is in the word.
  - <b>If the guess is in the word</b>:
    - Printed a message saying “Good guess! {guess} is in the word.”
    - Created a for-loop to loop through each letter in the word and replace the corresponding underscore in word_guessed with the guessed letter.
    - Reduced `num_letters` by 1.
  - <b>Else</b>:
	- Reduced `num_lives` by 1.
	- Printed a message saying “Sorry, {guess} is not in the word.”
	- Printed another message saying “You have {num_lives} lives left.”

### 2.4.3 Implement the function to ask for user input
Steps:

- Created a method called `ask_for_input`.
- Used a `while True` loop to continually ask the user for input until a valid guess is made.
- Asked the user to guess a letter and assigned it to a variable called _guess_.
- Created an if statement to check if the guess is not a single alphabetical character (`not guess.isalpha() or len(guess) != 1`).

### 2.4.4 Refactor and optimise current code
The new and optimised code version can be found in the milestones folder of this repository, being called [_milestone_4_optimised.py_](./milestones/milestone_4_optmised.py), while the old one being: [_milestone_4.py_](./milestones/milestone_4.py).<br>
My personal suggestion is opening both on different windows to see and follow the changes that were made.

- **Meaningful naming**:
    - Renamed methods to be more descriptive.
    - e.g.: `update_word_guessed`, `handle_correct_guess`, `handle_incorrect_guess`.

- **Elimination of code duplication**:
    - Refactored the code to eliminate duplicated logic by introducing helper methods (`update_word_guessed`, `handle_correct_guess`, `handle_incorrect_guess`).

- **Single responsibility principle**:
    - Ensured that each method focuses on a specific task.
    - Example: `handle_correct_guess` handles the logic for a correct guess, `handle_incorrect_guess` takes care of the logic for an incorrect guess, and `is_valid_guess` validates the guess.

- **Access Modifiers**:
    - Made helper methods private (using a single underscore) to indicate that they are intended for internal use within the class.

- **Minimal use of `self`**:
    - Significantly optimized this version of the code from my previous version, ensuring `self` is only used for instance variables.

- **Consistent docstrings**:
    - Added docstrings to all methods to explain their purpose, parameters, and return values, following the integrated development environments (IDEs) structure format.

###
Content here

###
Content here

### 2.5: Putting it all together
Content here...

#### 2.5.1 Subchapter One
Content here...

#### 2.5.2 Subchapter Two
Content here...

## Installation Instructions
Content here...

## Usage Instructions
Content here...

## File Structure
Content here...

## License Information
Content here...

## Demonstrated Skills
Content here...