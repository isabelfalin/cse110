cars = 7
people = 80
people_per_car = people / cars

#This is without rounding
print(f"There are {people_per_car} poeple in each car")

#This is with rounding to one
print(f"There are {people_per_car:.1f} people in each car.")

#This is with rounding to two
print(f"There are {people_per_car:.2f} people in each car.")

#This is with rounding to three
print(f"There are {people_per_car:.3f} people in each car.")

#When there is no 'f' after the nymber it will just count the total digits 
#Not the digits after the decimal.

#If you use 'e' it turns the display into scientific notation.
