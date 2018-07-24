"""
CP1404/CP5632 Practical - Suggested Solution
Car Driving Simulator
"""
from prac_06.car import Car

MENU = "Menu:\nd) drive\nr) refuel\nq) quit"


def main():
    """Car simulator program, demonstrating use of Car class."""
    print("Let's drive!")
    name = input("Enter your car name: ")
    # create a Car instance with initial fuel of 100 and user-provided name
    car = Car(name, 100)
    print(car)
    print(MENU)
    choice = input("Enter your choice: ").lower()
    while choice != "q":
        if choice == "d":
            distance_to_drive = int(
                input("How many km do you wish to drive? "))
            while distance_to_drive < 0:
                print("Distance must be >= 0")
                distance_to_drive = int(
                    input("How many km do you wish to drive? "))
            distance_driven = car.drive(distance_to_drive)
            print("The car drove {}km".format(distance_driven), end="")
            if car.fuel == 0:
                print(" and ran out of fuel", end="")
            print(".")
        elif choice == "r":
            fuel_to_add = int(input(
                "How many units of fuel do you want to add to the car? "))
            while fuel_to_add < 0:
                print("Fuel amount must be >= 0")
                fuel_to_add = int(input(
                    "How many units of fuel do you want to add to the car? "))
            car.add_fuel(fuel_to_add)
            print("Added {} units of fuel.".format(fuel_to_add))
        else:
            print("Invalid choice")
        print()
        print(car)
        print(MENU)
        choice = input("Enter your choice: ").lower()
    print("\nGood bye {}'s driver.".format(car.name))


main()
