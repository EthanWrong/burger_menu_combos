"""05 Edit Combo
Code that allows user to edit an existing combo
"""

from easygui import *


def edit(menu, selected_combo):
    combo_items = menu[selected_combo]
    choices = []
    for item in combo_items:
        choices.append(f"{item[0]}/${item[1]:.2f}")

    while True:
        to_edit = buttonbox(f"{selected_combo}\n\nSelect an item to edit",
                            f"Edit {selected_combo}", choices=choices+["Exit"])
        if to_edit == "Exit":
            break
        else:  # edit item
            pass




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

edit(burger_combo_menu, "Super")
