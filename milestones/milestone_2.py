# Write import random on the line. Note: To import a module, you have to use the import keyword at the top of the file.
import random

# Create a list containing the names of your 5 favorite fruits.
fruit_list = ['Apple', 'Banana', 'Orange', 'Tomato', 'Mango']

# Print out the newly created list to the standard output (screen).
print(fruit_list)

# Function to get a random fruit from the list
def get_random_fruit(fruits):
    return random.choice(fruits)

# Get a random fruit and assing it to a variable
random_fruit = get_random_fruit(fruits)

# Print out word to the standard output. Run the code several times and observe the words printed out after each run.
print(random_fruit)

# Function to validate the user's guess
def validate_guess(guess):
    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")

# Get user's guess
user_guess = input("Enter a single letter: ")

# Validate the user's guess
validate_guess(user_guess)