import random

user_wins = 0
computer_wins = 0 

def is_win(player, opponent):
    # return true if the player wins
    if (player == 'rock' and opponent =='scissors') or (player == 'scissors' and opponent =='paper') \
        or (player == 'paper' and opponent == 'rock'):
        return True

while True:
    user = input("What do you choose? type 'rock', 'paper', or 'scissors', or type 'q' to quit.\n").lower()
    if user == "q":
        print("Okay, bye for now!")
        quit()
    computer = random.choice(['rock', 'paper', 'scissors'])
        
    if user == computer:
        print("The computer chose " + computer + ".")
        print('It\'s a tie!')
        print("Your wins:", user_wins, "Computer wins:", computer_wins)
    
    if is_win(computer, user):
        print("The computer chose " + computer + ".")
        print('You lost.')
        computer_wins += 1
        print("Your wins:", user_wins, "Computer wins:", computer_wins)
    
    # rock > scissors, scissors > paper, paper > rock
    if is_win(user, computer):
        print("The computer chose " + computer + ".")
        print('You won!')
        user_wins += 1
        print("Your wins:", user_wins, "Computer wins:", computer_wins)
        
    again = input("Would you like to play again? Type 'Yes' or 'No' ").lower()
    if again == "no":
        print("Final Score, you won", user_wins, "times, and the Computer won", computer_wins, "times.")
        print("Thanks for playing, see you soon!")
        quit()
    if again == "yes":
        print("Booyah, let's play again!")

