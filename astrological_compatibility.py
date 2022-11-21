# This is a text application that when a sign is inputted, their most compatible/least compatible/sister sign will show. 

# setup variables

p = "Pisces"
s = "Scorpio"
a = "Aquarius"
g = "Gemini"
c = "Capricorn"
l = "Leo"
C = "Cancer"
L = "Libra"
v = "Virgo"
t = "Taurus"
S = "Saggitarius"
A = "Aries"

compatible = "You are most compatible with:"
not_compatible = "You are least compatible with:"
complementary = "Your complementary signs are:"
sister_sign = "Your sister sign is:"

# Operations

print("Welcome to the horoscope matchmaking application!")
print("Are you ready to see which sign you're most and least compatible with?")
print("Let's get started!")

while True:
    horoscope = input("What's your sign? ").lower()

    if horoscope == 'aries':
            print(compatible, l,"and", S)
            print(not_compatible, v,"and", s)
            print(complementary, g,"and", a)
            print(sister_sign, L)
    elif horoscope == 'taurus':
            print(compatible, v,"and", c)
            print(not_compatible, L,"and", S)
            print(complementary, C,"and", p)
            print(sister_sign, s)
    elif horoscope == 'gemini':
            print(compatible, L,"and", a)
            print(not_compatible, s,"and", c)
            print(complementary,A,"and", l)
            print(sister_sign,S)
    elif horoscope == 'cancer':
            print(compatible, s,"and", p)
            print(not_compatible, S,"and", a)
            print(complementary, t,"and", v)
            print(sister_sign, c)
    elif horoscope == 'leo':
            print(compatible, A,"and", S)
            print(not_compatible, c,"and", p)
            print(complementary, L,"and", g)
            print(sister_sign, a)
    elif horoscope == 'virgo':
            print(compatible, c,"and", t)
            print(not_compatible, a,"and", A)
            print(complementary, s,"and", C)
            print(sister_sign, p)
    elif horoscope == 'libra':
            print(compatible, g,"and", a)
            print(not_compatible, t,"and", p)
            print(complementary, S,"and", l)
            print(sister_sign, A)
    elif horoscope == 'scorpio':
            print(compatible, C,"and", p)
            print(not_compatible, g,"and", A)
            print(complementary, v,"and", c)
            print(sister_sign, t)
    elif horoscope == 'sagittarius':
            print(compatible, A,"and", l)
            print(not_compatible, t,"and", C)
            print(complementary, L,"and", a)
            print(sister_sign, g)
    elif horoscope == 'capricorn':
            print(compatible, t,"and", v)
            print(not_compatible, g,"and", l)
            print(complementary, p,"and", s)
            print(sister_sign, C)
    elif horoscope == 'aquarius':
            print(compatible, g,"and", L)
            print(not_compatible, C,"and", v)
            print(complementary, A,"and", S)
            print(sister_sign, l)
    elif horoscope == 'pisces':
            print(compatible, C,"and", s)
            print(not_compatible, l,"and", L)
            print(complementary,c, "and", t)
            print(sister_sign,v)
    else:
        print("Please enter in a valid astrological sign. ")
        continue
    
    while True:
        again = input("Would you like to try another sign? ").lower()  

        if again == 'yes':
            print("Alright, let's try this again..")
            break
        
        if again == 'no':
            print("Okay, application ending...")
            quit() 
        else:
            print("Please enter in 'yes' or 'no'. ")
            continue
        
            
        
