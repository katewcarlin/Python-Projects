# Python Madlibs Intro

print("Welcome to Madlibs.py, let's tell a story!")
print("This story is called 'The Magic Computers'!")
print("Input different types of words to create a wacky tale.")

# Madlibs inputs

name = input("First, what is your name? ")

noun = input("Type in a noun: ")

pnoun_1 = input("Type in a plural noun: ")

pt_verb_1 = input("Type in a verb (present tense): ")

pt_verb_2 = input("Type in a second verb (present tense): ")

adjective_1 = input("Type in an adjective: ")

adjective_2 = input("Type in second adjective: ")

pnoun_2 = input("Type in a second plural noun: ")

adjective_3 = input("Type in a third adjective: ")



# Printed Story

print("The Magic Computers - by", name)

print("Today, every student has a computer small enough to fit into their", noun + ".")

print("A student can solve any math problem by simply pressing the computer's little", pnoun_1 + ".")

print("Computers can add, multiply, divide, and", pt_verb_1 + ".")

print("They can also", pt_verb_2, "better than a human.")

print("Some computers are", adjective_1 + ".")

print("Others have a/an", adjective_2, "screen that shows all kinds of", pnoun_2, "and", adjective_3, "figures.")

quit()
