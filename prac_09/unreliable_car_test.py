"""
CP1404/CP5632 Practical - Suggested Solution
UnreliableCar class tests

The point to an UnreliableCar is that it randomly does not always drive.
So, these tests run several times in order to see that randomness.
We expect the good car (high reliability) to drive more often than the bad car.
"""

from prac_09.unreliable_car import UnreliableCar


def main():
    """Test some UnreliableCars."""

    # create cars with different reliabilities
    good_car = UnreliableCar("Mostly Good", 100, 90)
    bad_car = UnreliableCar("Dodgy", 100, 9)

    # attempt to drive the cars many times
    # output what distance they drove
    for i in range(1, 12):
        print(f"Attempting to drive {i}km:")
        print(f"{good_car.name:12} drove {good_car.drive(i):2}km")
        print(f"{bad_car.name:12} drove {bad_car.drive(i):2}km")

    # print the final states of the cars
    print(good_car)
    print(bad_car)


main()
