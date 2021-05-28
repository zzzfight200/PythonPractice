import random
words = ["python","programing","treasure","creative","medium","horror"]
#words = ["horror"]
ChosenOne = random.choice(words)
length = len(ChosenOne)
Guesses = ""
turns = 7
print("It's time to play hangman!")
print("Guess the word!","_"*length)
while turns>0:
    failed = 0
    GuessLetter = input("\nGuess a letter:")
    Guesses = Guesses + GuessLetter
    for char in ChosenOne:
        if char in Guesses:
            print(char,end="")
        else:
            print("_",end="")
            failed = failed + 1
    if failed == 0:
        print("\nYou Win!")
        break
    if GuessLetter not in ChosenOne:
        turns = turns-1
        print("\nWrong!")
        print("you have",+turns,"changes to try" )
        if turns == 0:
            print("\nSorry,You Lose!")

