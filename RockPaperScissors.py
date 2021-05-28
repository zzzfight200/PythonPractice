import random
ComputerScore = 0
PlayerScore = 0
while True:
    Choice = input("Choose Rock Paper or Scissors!").capitalize()
    Computer = random.choice(["Scissors", "Rock", "Paper"])
    CaseSample = Choice + Computer
    def RockScissors():
        print("Your Choice is Rock and Computer's Choice is Scissors")
        print("You Win!")
        global PlayerScore
        PlayerScore+=1
        print("Player score is %d and computer’score is %d \n" %(PlayerScore,ComputerScore))

    def RockRock():
        print("Your Choice is Rock and Computer's Choice is Rock")
        print("tie!")
        print("Player score is %d and computer score is %d \n" %(PlayerScore, ComputerScore))

    def RockPaper():
        print("Your Choice is Rock and Computer's Choice is Paper")
        print("You Lose!")
        global ComputerScore
        ComputerScore+=1
        print("Player score is %d and computer score is %d \n" %(PlayerScore, ComputerScore))

    def PaperScissors():
        print("Your Choice is Paper and Computer's Choice is Scissors")
        print("You Lose!")
        global ComputerScore
        ComputerScore += 1
        print("Player score is %d and computer score is %d \n" %(PlayerScore, ComputerScore))

    def PaperRock():
        print("Your Choice is Paper and Computer's Choice is Rock")
        print("You Win!")
        global PlayerScore
        PlayerScore += 1
        print("Player score is %d and computer score is %d \n" %(PlayerScore, ComputerScore))

    def PaperPaper():
        print("Your Choice is Paper and Computer's Choice is Paper")
        print("tie!")
        print("Player score is %d and computer score is %d \n" %(PlayerScore, ComputerScore))

    def ScissorsScissors():
        print("Your Choice is Scissors and Computer's Choice is Scissors")
        print("tie!")
        print("Player score is %d and computer score is %d \n" %(PlayerScore, ComputerScore))

    def ScissorsRock():
        print("Your Choice is Scissors and Computer's Choice is Rock")
        print("You Lose!")
        global ComputerScore
        ComputerScore += 1
        print("Player score is %d and computer score is %d \n" % (PlayerScore, ComputerScore))

    def ScissorsPaper():
        print("Your Choice is Scissors and Computer's Choice is Paper")
        print("You Win!")
        global PlayerScore
        PlayerScore += 1
        print("Player score is %d and computer score is %d \n" % (PlayerScore, ComputerScore))

    def default():
        print("Not This One,Check Your Spelling!\n")
    switch = {
        "RockScissors": RockScissors,
        "RockRock": RockRock,
        "RockPaper": RockPaper,
        "PaperScissors": PaperScissors,
        "PaperRock": PaperRock,
        "PaperPaper": PaperPaper,
        "ScissorsScissors": ScissorsScissors,
        "ScissorsRock": ScissorsRock,
        "ScissorsPaper": ScissorsPaper
    }
    switch.get(CaseSample, default)()
    # print(Choice,Computer)

