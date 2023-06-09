"""04 Search for combo meals
Code that will search menu for a combo and return that combo for further use
Trial 2: Enterbox
"""

from easygui import *


def search(menu):
    while True:
        selected_combo = enterbox("Enter the name of the combo\n\n(Assume "
                                  "Capital Case)", "Search Combo").capitalize()

        if selected_combo in list(menu.keys()):
            break

    # Display details
    print(f"* {selected_combo} *")
    for item in menu[selected_combo]:
        print(f"-{item[0]} - ${item[1]:.2f}")

    # Return combo name
    if selected_combo != "Cancel":
        return selected_combo
    return None


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

search(burger_combo_menu)
