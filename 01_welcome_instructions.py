"""Welcome Screen and Instructions for Burger Menu Combos"""


from easygui import *


def welcome():
    print("#### WELCOME TO BURGER MENU COMBO MANAGER ####")
    msg = f"Welcome to Burger Menu Combo Manager.\n\nWould you like to see " \
          f"the instructions?"
    choice = ynbox(msg, "Welcome")
    if choice:
        instructions()


def instructions():
    msg1 = f"This program allows you to store and manage combos in the " \
           f"menu.\n\n" \
           f"You may EDIT or DELETE combos, and can PRINT combos or the " \
           f"full menu to the Python Console."
    msg2 = f"To EDIT or DELETE combos, first select SEARCH, choose a combo, " \
           f"and you will then be prompted to interact with it."
    msg3 = f"To PRINT a combo, SEARCH for that combo and it will be " \
           f"printed.\n\n" \
           f"To PRINT the menu, select PRINT MENU"
    msg4 = f"Your preset combos of 'Value', 'Cheezy', and 'Super' have " \
           f"already been hardcoded in."

    pages = (msg1, msg2, msg3, msg4)

    print("#### INSTRUCTIONS ####")
    for i in pages:
        print(i, "\n")
        msgbox(i, "Instructions")


welcome()
