# Please select one of the following: 
# 1. Add item
# 2. View cart
# 3. Remove item
# 4. Compute total
# 5. Quit
# Please enter an action: 1
# What item would you like to add? bed
# 'bed' has been added to the cart.

# Please enter an action: 2
# The contents of the shopping cart are:
# bed
# chair
# blanket


answer = None
shopping_cart = []
price_list = []

while answer != 5:
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. quit")

    answer = int(input("Please enter an action: "))
    if answer == 1:
        item = input("What item would you like to add? ")
        shopping_cart.append(item)
        price = float(input(f"What is the price of '{item}'? "))
        price_list.append(price)
        print(f"'{item}' has been added to the cart.")
        
    elif answer == 2:
        print("The contents of the shopping cart are:")
        for index in range(len(shopping_cart)):
            item = shopping_cart[index]
            price = price_list[index]
            print(f"{index + 1}. {item} - ${price:.2f}")

    elif answer == 3:
        removal_answer = int(input("Which item would you like to remove? "))
        item = shopping_cart.pop(removal_answer - 1)
        price = price_list.pop(removal_answer - 1)
        print("Item removed.")
    elif answer == 4:
        total = 0
        for price in price_list:
            total += price
        amount = len(shopping_cart)
        item_text = "items"
        if amount == 1:
            item_text = "item"
        print(f"The total price of the {amount} {item_text} in the shopping cart is ${total:.2f}")
    elif answer == 5:
        print("Thank you. Goodbye.")