

numbers = []
sum = 0
the_number = None

while the_number != 0:
    the_number = int(input("Enter a list of numbers, type 0 when finished: "))
    if the_number != 0:
        numbers.append(the_number)
   
for number in numbers:
    sum += number

print(f"The sum is: {sum}")

print(f"The average is: {sum / len(numbers)}")

print(f"The highest number is: {max(numbers)}")

positives = [item for item in numbers if item > 0]

print(f"The smallest postive number is: {min(positives)}")

sorted_numbers = sorted(numbers)
for number in sorted_numbers:
    print(number)