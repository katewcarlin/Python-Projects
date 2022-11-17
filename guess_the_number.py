import random

top_of_range = input("Type your Number Range here: ")

print("Okay... I'm thinking of a number between 0 and " + top_of_range,". Can you guess what it is?")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0, game over.")
        quit()
else:
    print("Please type a number next time, game over.")
    quit()

random_number = random.randrange(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make your guess! ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
    
    
    
    if user_guess == random_number:
        print("You guessed it correctly!")
        print("Congratulations, you have won!")
        print("You guessed the number in", guesses, "guesses, nice job!")
        break

    else:
        if user_guess > random_number:
            print("Hmmm.. guess a little lower next time.")
        else:
            print("Maybe try guessing a little higher next time?")

    continue