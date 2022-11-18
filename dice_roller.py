import random

again = True

while again:
    print("Let's roll some dice!")
    print("You rolled a ", random.randint(1,6),"!")
    another_roll = input("Would you like to roll the dice again? Type 'yes' or 'no ").lower()
    
    if another_roll == "yes":
        continue

    if another_roll == "no":
        print("Thanks for playing!")
        print("Bye for now!")
        break

    else:
        print("Enter in a valid response.")
        another_roll = input("Would you like to roll the dice again? Type 'yes' or 'no ").lower()
