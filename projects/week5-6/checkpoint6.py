print("Please enter a number 1-10 for each question ")

large = int(input("How large is your loan? "))
credit = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
down_payment = int(input("How large is your down payment? "))

choice = False

if large >= 5:
    if credit >= 7 and income >= 7:
        choice = True
    elif (credit >= 7 or income >= 7) and down_payment >= 5:
        choice = True
else:
    if credit < 4:
        choice = False
    else:
        if income >= 7 or down_payment >= 7:
            choice = True
        elif income >= 4 and down_payment >= 4:
            choice = True

if choice == True:
    print("Yes")
else:
    print("No")

