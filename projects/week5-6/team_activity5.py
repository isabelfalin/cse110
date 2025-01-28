a = 90
b = 80
c = 70
d = 60
f = 50

percentage = int(input("What is your grade percentage? "))

# if percentage >= a:
#     print("Your leter grade is A")
# elif percentage >= b:
#     print("Your letter grade is B")
# elif percentage >= c:
#     print("Your letter grade is C")
# elif percentage >= d:
#     print("Your letter grade is D")
# elif percentage >= f:
#     print("Your letter grade is an F")

letter = ""
unit_place = percentage % 10 
modifier = ""

if percentage >= a:
    letter = "A"
elif percentage >= b:
    letter = "B"
elif percentage >= c:
    letter = "C"
elif percentage >= d:
    letter = "D"
elif percentage >= f:
    letter = "F"

if unit_place >= 7 and letter != "A":
    modifier = "+"
elif unit_place <= 3 and letter != "F":
    modifier = "-"

print(f"Your grade is a {letter}{modifier}")

if percentage >= c:
    print("Good job! You passed!!")
else:
    print("You failed the course. Try again.")
