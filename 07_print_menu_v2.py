"""Code that prints the menu to the console
Now added a separate print_combo function, which will allow me to use this
in other parts of the code to easily print a combo e.g. in search, edit,
and add"""


from easygui import *

def print_combo(combo, combo_name):

    # find total price of combo
    total_price = 0
    for item in combo:
        total_price += item[1]

    # Display Results
    print(f"* {combo_name.upper()} * - ${total_price:.2f}")
    for item in combo:
        print(f"  {item[0]} - ${item[1]:.2f}")

    print()


def print_menu(menu):

    print("#### BURGER COMBO MENU ####")
    print()

    for combo in menu:
        print_combo(menu[combo], combo)

    msgbox("Menu has been printed to Python Console.")


# Data storage
burger_combo_menu = {
    "Value": [
        ["Beef burger", 5.69],
        ["Fries", 1.00],
        ["Fizzy drink", 1.00]
    ],
    "Cheezy": [
        ["Cheeseburger", 6.69],
        ["Fries", 1.00],
        ["Fizzy drink", 1.00]
    ],
    "Super": [
        ["Cheeseburger", 6.69],
        ["Large fries", 2.00],
        ["Smoothie", 2.00]
    ],
}

print_menu(burger_combo_menu)
