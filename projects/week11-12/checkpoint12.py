people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_age = 10000000
youngest_name = None

# Iterate through the list and display each string to the screen.
print()
for person in people:
    split_person = person.split()
    name = split_person[0]
    age = int(split_person[1])
    print(f"{name}, {age} ")

    if age < youngest_age:
        youngest_age = age
        youngest_name = name
print()
print(f"The youngest person is {youngest_name}, they are {youngest_age} years old.")



# Split the string into a name and age and print them to the screen.

# Find the age that is the youngest.

# Keep track of the name of the person that is the youngest.