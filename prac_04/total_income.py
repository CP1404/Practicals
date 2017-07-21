"""
CP1404/CP5632 Practical - Suggested Solution
Cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(
            input("Enter income for month {}: ".format(number_of_months)))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    """Print report based on incomes."""
    # Note that we do not need to pass in number_of_months
    # because we know the length of the incomes list
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, len(incomes) + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month,
                                                                       income,
                                                                       total))


main()
