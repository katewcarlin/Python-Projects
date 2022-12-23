# In-n-Out Menu Program


menu = {"double-double": 4.25,
        "cheeseburger": 2.95,
        "hamburger": 2.65,
        "french fries": 1.95,
        "milkshake": 2.55,
        "small beverage": 1.65,
        "medium beverage": 1.75,
        "large beverage": 1.95,
        "extra large beverage": 2.15,
        "milk": .99,
        "hot cocoa": 1.75,
        "coffee": 1.25}

cart = []
total = 0
print("\n~~~ In-n-Out Menu ~~~\n")
for key, value in menu.items():
    print(f"{key:25}: ${value:.2f}")

print("\n~~~~~ Since 1948 ~~~~~~\n")

while True:
    order = input("Select an item (press q to quit): ").lower()
    if order == "q":
        break
    elif menu.get(order) is not None:
        cart.append(order)

print("\n~~~ Checkout ~~~\n")
print("Your order today: ")
for order in cart:
    total += menu.get(order) 
    print(order, end="\n")

print()
print(f"Your total is ${total:.2f}, thanks for stopping by!")
