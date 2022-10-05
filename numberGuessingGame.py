import numpy as np
import random as rp


def hintOne(randomNum):
  if randomNum < numberGuess:
    print(f'HINT 1: The secret number is less than {numberGuess}\n')
  else:
    print(f'HINT 1: The secret number is greater than {numberGuess}\n')

def hintTwo(randomNum): #need to makea a for loop divisible by i
  dList = []
  for i in range(2,int(randomNum/2)):
    if randomNum%i == 0:
      dList.append(i)
      
  randomDivisor = rp.choice(dList)
  print(f'HINT 2: The secret number is divisible by {randomDivisor}\n')


  
    
def hintThree(randomNum): 
  multiples = []
  for i in range(2,10):
    multipleNumber = i*randomNum
    multiples.append(multipleNumber)
    
  randomMultiple = rp.choice(multiples)
  print(f'HINT 3: The secret number can divide {randomMultiple}\n')
  
def hintFour(randomNum):
  '''
  1. Divide by 10 and take int of it
  2. Add 1 to int and keep both numbers
  3. multiply both by 10
  4. print the range
  '''
  lowerNum = int(randomNum/10)
  higherNum = lowerNum + 1
  lowerRange = lowerNum * 10
  higherRange = higherNum * 10
  print(f'HINT 4: The number is between the ranges of {lowerRange} and {higherRange}\n')
  print("FINAL ATTEMPT\n")




print("Hello!\nWelcome to the number guesing game!\nYou have 5 attempts to guess the correct number!\n\n")
score = 0

randomNum = np.random.randint(1,99)
numberGuess = 0



while score < 5:
  numberGuess = int(input("Guess a number between 1 and 100: "))
  if numberGuess != randomNum:
    print("This is not the right number. Try again\n")
    score = score + 1
    if score == 1:
      hintOne(randomNum)
    elif score == 2:
      hintTwo(randomNum)
    elif score == 3:
      hintThree(randomNum)
    elif score == 4:
      hintFour(randomNum)
  
  else:
    print(f'Congratulations! you guessed the right number in {score} tries')
    break
if score == 5:
  print(f'Sorry, you could not guess the number. The right number is {randomNum}')