# state_names.py

STATE_ABBREVIATIONS = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "WA": "Western Australia",
    "SA": "South Australia",
    "ACT": "Australian Capital Territory",
    "NT": "Northern Territory"
}

user_input = input("Enter short state (e.g., QLD): ").upper()

if user_input in STATE_ABBREVIATIONS:
    print(f"{user_input} is {STATE_ABBREVIATIONS[user_input]}")
else:
    print("Invalid short state")

