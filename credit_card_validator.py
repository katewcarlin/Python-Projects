# Python Credit Card Validator

from re import X


sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Step 1: User input for credit card number. 

card_number = input("Enter a card number here: ")
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
card_number = card_number[::-1]

# Step 2: Add all digits from right to left. 

for x in card_number[::2]:
    sum_odd_digits += int(x)

# Step 3: Double every second digit from right to left. 

for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 + (x % 10 ))
    else:
        sum_even_digits += x

# Step 4: 

total = sum_odd_digits + sum_even_digits

# Step 5:

if total % 10 == 0:
    print("CARD NUMBER IS VALID")
else:
    print("CARD NUMBER IS INVALID")
