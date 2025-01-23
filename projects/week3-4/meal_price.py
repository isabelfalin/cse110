child_meal = float(input("What is the price of the child's meal? "))
adult_meal = float(input("What is the price of the adult's meal? "))
print()
number_child = int(input("How many children are there? "))
number_adult = int(input("How many adults are there? "))
print()
tax_rate = int(input("What is the sales tax rate? "))
print()
drink_price = float(input("What is the price of the drink? "))
drink = int(input("How many drinks are there? "))
print()
pie_price = int(input("What is the price of the pie? "))
pie_number = int(input("How many pies are there? "))
print()

subtoal1 = (number_child * child_meal)
subtotal2 =(number_adult * adult_meal)
subtotal = (subtoal1 + subtotal2 )

drink_total = (drink_price * drink)
pie_total = (pie_price * pie_number)
specialty_total = (drink_total + pie_total)

sales_tax = (specialty_total * subtotal * tax_rate / 100)

total_price = (specialty_total + subtotal + sales_tax)

print(f"Subtotal: ${subtotal + specialty_total}")
print(f"Sales tax: ${sales_tax}")
print(f"Total: ${total_price}")
print()

pay_amount = float(input("What is the payment amount? "))

change = (pay_amount - total_price )
print(f"Change: ${change:.2f}")