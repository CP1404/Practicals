"""
CP1404/CP5632 - Practical - Suggested Solution
Menu using the standard while loop pattern
Pseudocode:
    get name
    display menu
    get choice
    while choice != Q
       if choice == H
           display "hello" name
       else if choice == G
           display "goodbye" name
       else
           display invalid message
       display menu
       get choice
    display finished message
"""
MENU_STRING = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Enter name: ")
print(MENU_STRING)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")
    print(MENU_STRING)
    choice = input(">>> ").upper()
print("Finished.")
