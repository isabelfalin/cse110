account_list = []
money_list = []

account = None
sum = 0

while account != "quit":
    account = input("What is the name of your account? ")
    if account != "quit":
        money = float(input("What is the balance? "))
        account_list.append(account)
        money_list.append(money)
print()
print(f"Account information:")

for index in range(len(account_list)):
    account = account_list[index]
    money = money_list[index]
    print(f"{index}. {account} - ${money:.2f}")

for money in money_list:
    sum += money

print()
print(f"Total: ${sum:.2f}")

print(f"The average is: ${sum / len(money_list):.2f}")
print(f"Highest balance: {account} - ${max(money_list):.2f}")
print()

answer = "yes"

while answer.lower() == "yes":
    print()
    answer = input("Do you want to update an account? ")
    if answer == "yes":
        change = int(input("What account index do you want to update? "))
        new_amount = float(input("What is the new amount? "))
        money_list[change] = new_amount

    print()
    print(f"Account information:")

    for index in range(len(account_list)):
        account = account_list[index]
        money = money_list[index]
        print(f"{index}. {account} - ${money:.2f}")












#     Total: $384.89
# Average: $128.30
# Highest balance: savings - $392.99

# Do you want to update an account? yes
# What account index do you want to update? 0
# What is the new amount? 200






    