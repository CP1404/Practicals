"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


score = float(input("Enter score: "))
if score >=90 and score <=100:
    print("Excellent")
elif score >= 50 and score <=100:
        print("Passable")
elif score < 50 and score >=0:
        print("Bad")
else:
    print("Invalid score")
