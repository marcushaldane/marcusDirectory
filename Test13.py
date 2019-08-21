# Hangman game
import random

def stringToList(inputString):
    returnList = []
    for i in inputString:
        returnList.append(i)
    return returnList

def listToString(inputList):
    returnString = ""
    for i in inputList:
        returnString += i
    return returnString

def reversUL(inputChar):
    returnChar = ''
    if (inputChar.isupper() == True): returnChar = inputChar.lower()
    else: returnChar = inputChar.upper()
    return returnChar

list = ["Explosion", "Hangman", "Marcus", "Random", "Variable", "Boolean", "Asphalt", "Colorado", "Interger", "Grandparent", "String", "Greatness", "Skittles", "Duetschland", "Minnesota", "International"]
randWord = list[random.randint(0,len(list)-1)]

# creating the hiddenword
randWordLength = len(randWord)
hiddenWord = ""
for i in range(0,randWordLength):
    hiddenWord += "_"

score = 5
revealedWord = hiddenWord
while(revealedWord != randWord and score > 0):
    print(revealedWord)
    playerInput = input("Guess a letter: ")
    index = -1
    wrongGuess = True
    print("++++++++++++++++++++++++++++++++++++++")
    for i in randWord:
        index += 1
        if (i == playerInput or reversUL(i) == playerInput):
            revealedList = stringToList(revealedWord)
            revealedList[index] = i
            revealedWord = listToString(revealedList)
            wrongGuess = False
    if (wrongGuess == True):
        score -= 1
        print("The character %s does not exist." % playerInput, "\nScore: %d" % score)


# gameflow
if (revealedWord == randWord):
    print("Congradulations you guessed %s" % randWord)
else: print("You failed to correctly guess %s" % randWord)
