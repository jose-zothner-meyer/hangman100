# Hangman Game
#### Under develpment. <br> Updated: 01/07/2024

## Overview
<p>Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within X amount of attempts.</p>

![Hangman Image](./images/hangman.png)
<br><br>
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
      - [2.3.1 Subchapter One](#231-subchapter-one)
      - [2.3.2 Subchapter Two](#232-subchapter-two)
    - [2.4: Create the Game class](#24-create-the-game-class)
      - [2.4.1 Subchapter One](#241-subchapter-one)
      - [2.4.2 Subchapter Two](#242-subchapter-two)
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
- wrote `import random` on the first line of my Python code
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
# Stage all the changes
git add .

# Commit the changes with a descriptive message
git commit -m "Add code for creating variables and user input validation"

# Push the changes to the remote repository
git push origin main
```

#### 2.2.7 Refactor and optimise current code
Content here...

### 2.3: Check if the guessed character is in the word
Content here...

#### 2.3.1 Subchapter One
Content here...

#### 2.3.2 Subchapter Two
Content here...

### 2.4: Create the Game class
Content here...

#### 2.4.1 Subchapter One
Content here...

#### 2.4.2 Subchapter Two
Content here...

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