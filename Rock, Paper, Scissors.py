import random

def play():
    user = input("What do you choose? type 'rock', 'paper', or 'scissors'\n")
    computer = random.choice(['rock', 'paper', 'scissors'])

    if user == computer:
        print("The computer chose " + computer,".")
        return 'It\'s a tie!'


    # rock > scissors, scissors > paper, paper > rock
    if is_win(user, computer):
        print("The computer chose " + computer,".")
        return 'You won!'

    if is_win(computer, user):
        print("The computer chose " + computer,".")
        return 'You lost.'

def is_win(player, opponent):
    # return true if the player wins
    if (player == 'rock' and opponent =='scissors') or (player == 'scissors' and opponent =='paper') \
        or (player == 'paper' and opponent == 'rock'):
        return True

print(play())
