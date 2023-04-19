"""Code that accepts an already chosen combo from the menu, and deletes it
Trial 2: NO / yes to give user warning"""

from easygui import *


def delete(menu, selected_combo):
    menu_temp = menu.copy()
    msg = f"Are you sure you want to delete the *{selected_combo}* Combo?"
    choice = buttonbox(msg, "Delete Combo", choices=["NO", "Yes"])

    if choice == "Yes":  # if yes
        del menu_temp[selected_combo]
        msgbox(f"*{selected_combo}* has been deleted from the menu.",
               "Delete Combo")

    else:
        msgbox(f"No combos have been deleted from the menu.", "Delete Combo")

    return menu_temp


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
chosen_combo = "Value"
new_menu = delete(burger_combo_menu, chosen_combo)
print(new_menu)
