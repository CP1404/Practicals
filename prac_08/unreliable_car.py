"""
CP1404/CP5632 Practical - Suggested Solution
UnreliableCar class, derived from Car
"""

from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    """An unreliable version of a car."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car, only sometimes, based on reliability."""
        random_number = randint(1, 100)
        distance_driven = 0
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        return distance_driven
