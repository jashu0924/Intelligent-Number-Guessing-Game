# Import libraries
import random as rp

# Hint One
def hintOne(randomNum, nGuess): 
  '''
  This function returns if the guessed number is less than or greater than the secret random number
  randomNum: A randomly generated secret number to be guessed
  nGuess: First Guess by the user
  '''
  if randomNum < nGuess:
    return(f'HINT 1: The secret number is less than {nGuess}\n')
  else:
    return(f'HINT 1: The secret number is greater than {nGuess}\n')


# Hint Two
def hintTwo(randomNum):
  '''
  This function returns one of the randomly chosen divisor of the secret number
  randomNum: A randomly generated secret number to be guessed
  '''
  # Create empty list to store all the divisors
  dList = []

  # Create for loop to generate and store all divisors except 1.
  for i in range(2,int(randomNum)):
    if randomNum%i == 0:
      dList.append(i)

  # Randomly choosing one of the divsors   
  randomDivisor = rp.choice(dList)
  return(f'HINT 2: The secret number is divisible by {randomDivisor}\n')


# Hint Three 
def hintThree(randomNum):
  '''
  This function returns one of the randomly chosen multiple (from 2 through 10) of the secret number
  randomNum: A randomly generated secret number to be guessed
  '''

  # Creating an empty list to store multiples
  multiples = []
  
  # Generating and storing multiples of the secret number in the range of 2 through 10
  for i in range(2,10):
    multipleNumber = i*randomNum
    multiples.append(multipleNumber)

  # Randomly choosing one of the generated multiples from the list
  randomMultiple = rp.choice(multiples)
  return(f'HINT 3: The secret number can divide {randomMultiple}\n')


# Hint Four
def hintFour(randomNum):
  '''
  This function returns the range of the secret number in 10's.
  Example: "Secret number is 37. The range would be 30-40."
  randomNum: A randomly generated secret number to be guessed
  '''

  # select lower and upper range
  lowerNum = int(randomNum/10)
  higherNum = lowerNum + 1
  lowerRange = lowerNum * 10
  higherRange = higherNum * 10

  return(f'HINT 4: The number is between the ranges of {lowerRange} and {higherRange}\nFINAL ATTEMPT\n')
