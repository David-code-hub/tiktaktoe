import random

#generate number
randomNum = 0
guessing = True
stillguessing = False
def generateRandom():
    global randomNum
    randomNum = random.randint(1,10)
    # return randomNum

def generateNumber():
    try:
        global randomNum,stillguessing,guessing
        if stillguessing == False:
            generateRandom()
            stillguessing = True
        else:
            pass
        guess =  int(input('Guess the number : '))
        if guess > randomNum:
            print('Too high')
        elif guess < randomNum:
            print('Too low')
        elif guess == randomNum:
            stillguessing = False
            guessing = False
            print('You got it right!')
    except ValueError:
        print('Error with your input value!')

while guessing:
    generateNumber()