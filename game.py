# import libraries
import numpy as np

# Import utilities
from utilities import hintOne, hintTwo, hintThree, hintFour

# Start of the Program
print("Hello!\nWelcome to the number guesing game!\nYou have 5 attempts to guess the correct number!\n\n")

score = 0 # Initializing Score
randomNum = np.random.randint(1,99) # Randomly choosing an integer between 1 and 99
# numberGuess = 0 # Initializing First Guess

# Loop to give user a maximum of 5 attempts to guess the secret number.
while score < 5:
  # Taking guesses
  numberGuess = int(input("Guess a number between 1 and 100: "))

  if numberGuess != randomNum:
    print("This is not the right number. Try again\n")
    score = score + 1
    if score == 1: # Providing first hint
      print(hintOne(randomNum,numberGuess))
    elif score == 2: # Providing second hint
      print(hintTwo(randomNum))
    elif score == 3: # Providing third hint
      print(hintThree(randomNum))
    elif score == 4: # Providing fourth and final hint
      print(hintFour(randomNum))
  
  else:
    # When user guesses correctly
    print(f'Congratulations! you guessed the right number in {score} tries')
    break

# when user fails to guess in 5 attempts
if score == 5:
  print(f'Sorry, you could not guess the number. The right number is {randomNum}')