import math

print("Welcome to the velocity calculator. Please enter the following:")
print()

m = float(input("Mass (in kg): "))
g = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
g2 = float(input("Gravity two (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))

t = float(input("Time (in seconds): "))
p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
A = float(input("Cross sectional area (in m^2): "))
C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

c = (1 / 2 * p * A * C)

print()
print(f"The inner value of c is: {c:.3f}")
vel_part1 = (math.sqrt(m * g / c))
vel_part2 = (1 - math.exp( (-1 * math.sqrt(m * g * c) / m) * t ))
velocity = vel_part1 * vel_part2
print(f"The velocity after {t} seconds is: {velocity:.3f} m/s")
print()
vel_part1 = (math.sqrt(m * g2 / c))
vel_part2 = (1 - math.exp( (-1 * math.sqrt(m * g2 * c) / m) * t ))
velocity = vel_part1 * vel_part2
print(f"The velocity with the 2nd gravity after {t} seconds is: {velocity:.3f} m/s")




