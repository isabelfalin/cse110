fahrenheit = float(input("What is the temperature in Fahrenheit? "))

celsius = round((fahrenheit - 32) * 5 / 9, 1)
print()
print(f"{fahrenheit} degrees F = {celsius} degrees C")