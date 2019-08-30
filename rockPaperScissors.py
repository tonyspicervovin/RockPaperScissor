from random import randint
print('Welcome to Rock Paper Scissors')
print('Rules are rock beats scissors, paper covers rock, and scissors cut paper and the same is a tie!') #explaining rules of game
acceptableAnswers = ['Rock', 'Paper', 'Scissors']  #Creating acceptable answers


def getAnswer():
    while True:
        player = input("Choose Rock, Paper or Scissors: ")
        if player in acceptableAnswers:
            return player
        else:
            print("Please choose Rock, Paper or Scissors ")
      #Asking user for answer, continuing to ask until I get a good answer, than returning answer
def getComputer():
    randChoice = randint(1,3)
    if randChoice == 1:
        computer = 'Rock'
    elif randChoice == 2:
        computer = 'Paper'
    else:
        computer = 'Scissors'
    return computer
    #Generating number 1-3, than assigning that to an answer and returning
def whoWins(player,computer):
    print('Computer chose', computer)
    print(player, 'vs', computer)
    if player == computer:
        print('DRAW!')
    elif player == 'Rock' and computer == 'Scissors' or player == 'Paper' and computer == 'Rock' or player == 'Scissors' and computer == 'Paper':
        print('Player Wins!')
    elif computer == 'Rock' and player == 'Scissors' or computer == 'Paper' and player == 'Rock' or computer == 'Scissors' and player == 'Paper':
        print('Computer Wins!')
    #printing computers answer, and than users and computers, than deciding who wins based on rules
player = getAnswer()
computer = getComputer()
whoWins(player, computer)











