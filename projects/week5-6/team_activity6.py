can_ride = True
rider_age1 = int(input("What is the age of the first rider? "))
rider_height1 = float(input("WHat is the height of the first rider? "))

second_rider_question = input("Is there a second rider (yes/no)? ")
if second_rider_question == "no":
    #single rider rules
    if rider_height1 < 36:
        can_ride = False
    if rider_age1 < 18 or rider_height1 < 62:
        can_ride = False

else:
    rider_age2 = int(input("What is the age of the second rider? "))
    rider_height2 = float(input("WHat is the height of the second rider? "))
    #double rider rules
    if rider_height2 < 36 or rider_height1 < 36:
        can_ride = False
    if rider_age2 < 18 and rider_age1 < 18:
        can_ride = False

if can_ride:
    print("You can ride!!!")
else:
    print("You can't ride :( ")