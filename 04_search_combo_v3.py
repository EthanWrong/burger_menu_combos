"""04 Search for combo meals
Code that will search menu for a combo and return that combo for further use
Trial 1: Buttons
"""

from easygui import *


def search(menu):
    combos = list(menu.keys())  # Get list of all combo names
    selected_combo = buttonbox("Please pick a combo", "Search Combo",
                               combos + ["Cancel"])

    if selected_combo == "Cancel":
        print("return", None)
        return None

    # Display details
    print(f"* {selected_combo} *")
    for item in menu[selected_combo]:
        print(f"-{item[0]} - ${item[1]:.2f}")

    # Return combo name
    print("return", selected_combo)
    return selected_combo


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
