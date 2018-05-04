"""
CP1404/CP5632 Practical - Suggested Solution
UnreliableCar class, derived from Car
"""

from random import randint
from prac_08.car import Car


class UnreliableCar(Car):
    """An unreliable version of a car."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car, only sometimes, based on reliability."""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        # Either way, we want to call the parent class's drive method (maybe driving 0)
        distance_driven = super().drive(distance)
        return distance_driven
