can_ride = True
rider_age1 = int(input("What is the age of the first rider? "))
rider_height1 = float(input("WHat is the height of the first rider? "))

#stretch 2
if rider_age1 >= 12 and rider_age1 <= 17:
    passport1 = input("Do you have a golden passport? ")
    if passport1 == "yes":
        rider_age1 = 18

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
    
    #stretch 2
    if rider_age2 >= 12 and rider_age1 <= 17:
        passport2 = input("Do you have a golden passport? ")
        if passport2 == "yes":
            rider_age2 = 18

    if rider_height2 < 36 or rider_height1 < 36:
        can_ride = False
    if rider_age2 < 18 and rider_age1 < 18:
        #strecth 3
        if (rider_age1 >= 16 and rider_age2 >= 14) or (rider_age1 >= 14 and rider_age2 >= 16):
            can_ride = True
        #stretch 1
        elif rider_age1 > 12 and rider_age2 > 12 and rider_height1 > 52 and rider_height2 > 52:
            can_ride = True
        else:
            can_ride = False

if can_ride:
    print("You can ride!!!")
else:
    print("You can't ride :( ")