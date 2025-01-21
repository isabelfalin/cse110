color = input("Please type your favorite color: ")

print()
print(f"Your favorite color is: {color}!!")

print()
animal = input("Please state you're favorite animal: ")

print()
print(f"Your favorite animal is a(n): {animal} :D")

answer = input(f"Do you like {color} {animal}s? ")

print()
if answer == "yes":
    print("Oh good! I like them too!")
elif answer == "maybe":
    print("Give me a better answer!")
else:
    print("Repent, and try again.")
