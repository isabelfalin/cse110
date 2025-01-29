
# What is the age of the first rider? 12
# What is the height of the first rider? 46
# Is there a second rider (yes/no)? no
# Sorry, you may not ride.
rider_age1 = int(input("What is the age of the first rider? "))
rider_height1 = float(input("WHat is the height of the first rider? "))
rider_age2 = int(input("What is the age of the second rider? "))
rider_height2 = float(input("WHat is the height of the second rider? "))

second_rider_question = input("Is there a second rider (yes/no)? ")

if second_rider_question == True:
    print("You can ride!")