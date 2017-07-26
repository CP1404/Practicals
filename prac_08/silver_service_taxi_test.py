"""
CP1404/CP5632 Practical - Suggested Solution
SilverServiceTaxi class tests
"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())

main()
