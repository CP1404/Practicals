"""
CP1404/CP5632 - Practical - Suggested Solution
Shop calculator program to determine total (discounted) price
"""

total = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price = float(input("Price of item: "))
    total += price

if total > 100:
    total *= 0.9  # apply 10% discount

print("Total price for ", number_of_items, " items is $", total, sep='')

# with f-string formatting for currency output
print(f"Total price for {number_of_items} items is ${total:.2f}")
