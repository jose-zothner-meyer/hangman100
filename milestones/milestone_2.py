# Write import random on the line. Note: To import a module, you have to use the import keyword at the top of the file.
import random

# Create a list containing the names of your 5 favorite fruits.
fruits = ['Apple', 'Banana', 'Orange', 'Tomato', 'Mango']
# Assign this list to a variable called word_list.
word_list = fruits
# Print out the newly created list to the standard output (screen).
print(word_list)

# Assign the randomly generated word to a variable called word.
word = random.choice(word_list)
# Print out word to the standard output. Run the code several times and observe the words printed out after each run.
print(word)

guess = input()
# Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.
if len(guess) is 1 and str.isalpha(guess):
# In the body of the if statement, print a message that says "Good guess!".
    print("Good Guess!")
# Create an else block that prints "Oops! That is not a valid input." if the preceding conditions are not met.
else:
    print("Ooops! That is not a valid input.")