import random

def play():
    user = input("What do you choose?'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie!'


    # rock > scissors, scissors > paper, paper > rock
    if is_win(user, computer):
        return 'You won!'

    if is_win(computer, user):
        return 'You lost.'

def is_win(player, opponent):
    # return true if the player wins
    if (player == 'r' and opponent =='s') or (player == 's' and opponent =='p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())