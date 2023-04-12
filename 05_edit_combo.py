"""05 Edit Combo
Code that allows user to edit an existing combo
"""

from easygui import *


def choose_item(combo):
    items = []
    for item in combo:
        items.append(f"{item[0]} ${item[1]:.2f}")
    items += ["Save", "Cancel"]

    msg = f"COMBO NAME.....tk"

    chosen_item_text = buttonbox("Choose item", choices=items)

    if chosen_item_text in ("Save", "Cancel"):
        return chosen_item_text

    # code that converts item from its text form "name $0.00" to code form
    # this will not work if multiple items have same name within combo
    chosen_item_name = chosen_item_text.split("$")[0].strip()

    for item in combo:
        if item[0] == chosen_item_name:
            chosen_item = item

    return chosen_item


def get_new_price():
    try:
        new_price = float(enterbox("Enter new price").strip("$"))
    except ValueError:
        msgbox("Please enter a valid number")
        return get_new_price()
    return new_price


def choose_attribute(item):
    attributes = item
    attributes[1] = f"${attributes[1]:.2f}"  # format float as a currency str

    attribute = buttonbox("Choose attribute", choices=item)

    attributes[1] = float(attributes[1].strip("$"))  # format back to float

    return attribute


def set_attribute(combo, item, attribute):
    item_temp = item.copy()

    # if price selected
    if attribute[0] == "$":
        new_price = get_new_price()
        item_temp[1] = new_price

    # if name selected
    else:
        new_name = enterbox("Enter new name")
        item_temp[0] = new_name

    return item_temp


def edit(menu, selected_combo):
    # create a copy of the selected combo
    combo_temp = menu[selected_combo].copy()

    while True:
        # display possible items to choose, output selected item
        selected_item = choose_item(combo_temp)
        if selected_item == "Save":
            menu[selected_combo] = combo_temp
            return menu
        elif selected_item == "Cancel":
            print("cancel", menu)
            return menu
        else:
            # display attributes of item to choose, output selected attribute
            selected_attribute = choose_attribute(selected_item)

            # allow user to re-enter attribute, output new item
            item_temp = set_attribute(combo_temp, selected_item,
                                      selected_attribute)

            # set new item in combo temp
            for i, item in enumerate(combo_temp):
                if item[0] == selected_item[0]:
                    combo_temp[i] = item_temp


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

chosen_combo = "Value"  # placeholder input
new_menu = edit(burger_combo_menu, chosen_combo)
print(new_menu)
