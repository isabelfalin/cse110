# #Makeake an initializing variable. Example is below:

# number = 0

# #The computer will continue to run the program until it is no longer true
# #It will keep looping as long as the number is less than or equal to 10
# while number <= 10:
#     number = int(input("Give me a numbet greater than 10: "))

# print("Finished with loop")

# #start with the number 1 
# number = 1
# #It will keep looping as long as the number is less than or equal to 5
# while number <= 5:
# #display the number
#     print(f"The number is {number}")
# #this adds 1 to the number each time until it reaches 5
#     number = number + 1 
# #the loop is done
# print("Finished with the loop")

# #Initialize a variable beofre you use it in a loop otherwise the computer won't start the loops
# #for numbers it is usally 0 or -1

# number = -1

# message = ""

# #The loop won't start
# message = "howdy"
# while message == "":
#     message = input("Tell me your message: ")
# print(f"Your message is {message}")

# #The loop will start
# message = input("Tell me your message: ")
# while message == "":
#     message = input("Your message can't be blank. What's your message? ")
# print(f"Your message is {message}")


# Use a while loop to ask the user for a positive number (>= 0). Continue asking as long as the number is negative, 
# then display the number. For example:

number = int(input("Please onter a positive integer (>=0): "))

while number < 0:
    print("This is not a positive integer. Please try aagin.")
    number = int(input("Please onter a positive integer (>=0): "))
print(f"The number is: {number}")

 
# Use a while loop, to simulate a child asking their parent for a piece of candy. Have the program keep 
# looping until the user answers "yes", then have the program output "Thank you." For example:

candy = input("May I have a piece of candy? ")

while candy.lower() == "no":
    candy = input("May I have a piece of candy? ")

print("Thank you!")