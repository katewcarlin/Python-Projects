print("Welcome to the Cal Sports Quiz!")
print("Test your Golden Bear knowledge here!")

playing = input("Would you like to play? ")

if playing.lower() != "yes":
    quit()

print("Ok! Let's start the quiz! And go bears!")
score = 0

answer = input("When was UC Berkeley Founded? ")
if answer.lower() == "1868":
    print("Correct!")
    score += 1
else: 
    print("Sorry, that's incorrect.")
    print("The correct answer is 1868.")

answer = input("What is the name of the Cal mascot? ")
if answer.lower() == "oski":
    print("Correct!")
    score += 1
else:
    print("Sorry, that's incorrect.")
    print("The correct answer is Oski.")

answer = input("What was the name of the 2022 Cal Quarterback? ")
if answer.lower() == "jack plummer":
    print("Correct!")
    score += 1
else:
    print("Sorry,that's incorrect.")
    print("The correct answer is Jack Plummer.")

answer = input("What was the final score of the 2020 Big Game? ")
if answer.lower() == "24-23":
    print("Correct!")
    score += 1
else:
    print("Sorry, that's incorrect.")
    print("The correct answer is 24-23. Fun fact: Stanford won this time.")

answer = input("Who was the 2021-2022 PAC-12 Freshman of the Year in Women's Basketball? ")
if answer.lower() == "jayda curry":
    print("Correct!")
    print("Fun Fact: Jayda was the PAC-12 Freshman of the week FIVE TIMES!")
    score += 1
else:
    print("Sorry, that's incorrect")
    print("The correct answer is Jayda Curry.")
    print("Fun Fact: Jayda was the PAC-12 Freshman of the week FIVE TIMES!")

print("You got " + str(score) + " questions correct!")
print(str((score)/5 *100) + "% of your answers were correct!")