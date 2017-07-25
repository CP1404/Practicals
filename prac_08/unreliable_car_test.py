"""
CP1404/CP5632 Practical - Suggested Solution
UnreliableCar class tests

The point to an UnreliableCar is that it randomly does not always drive.
So, these tests run several times in order to see that randomness.
We expect the good car (high reliability) to drive more often than the bad car.
"""

from prac_08.unreliable_car import UnreliableCar


def main():
    """Test some UnreliableCars."""

    # create cars with different reliabilities
    good_car = UnreliableCar("Mostly Good", 100, 90)
    bad_car = UnreliableCar("Dodgy", 100, 9)

    # attempt to drive the cars many times
    # output what distance they drove
    for i in range(1, 12):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(good_car.name, good_car.drive(i)))
        print("{:12} drove {:2}km".format(bad_car.name, bad_car.drive(i)))

    # print the final states of the cars
    print(good_car)
    print(bad_car)
main()
