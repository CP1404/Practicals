"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))


    # Create a new Car object called "limo" that is initialised with 100 units of fuel.
    print("="*50)
    print("~~ Limo ~~")
    limo = Car(100)

    # Add 20 more units of fuel to this new car object using the add method.
    limo.add_fuel(20)

    # Print the amount of fuel in the car.
    print("fuel = ")

    # Attempt to drive the car 115 km using the drive method.
    limo.drive(115)
    distance_driven = limo.drive(115)
    # Print the car's odometer reading.
    print(f"Odometer: {limo.odometer} (after driving {distance_driven} km)")

    # Now add the __str__ method to the Car class in car.py.
    print(limo)

    # Now add a name field to the Car class (in car.py), and adjust the __init__ and __str__ methods to set and display this respectively. Make the str method return the car's name instead of just "Car".
    # Now add names (literals) to the constructors where you create Car objects in the used_cars.py program.
    # Test your work and make sure you can now make and view named cars.

    print("="*50)
    print("~~ New Car ~~")

    Audi = Car("Audi RS7",400)
    Audi.drive(120)
    print(Audi)


if __name__ == '__main__':
    main()
