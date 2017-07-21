"""
CP1404/CP5632 - Practical - Suggested Solution
Sales bonus program
"""

sales = float(input("Enter sales: $"))
if sales < 1000:
    bonus = sales * 0.1
else:
    bonus = sales * 0.15
print("Bonus is $", bonus, sep='')


# Version 2 with loop
# Note the boundary condition (0 is valid sales) and general structure
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print("Bonus is $", bonus, sep='')
    sales = float(input("Enter sales: $"))
