"""NON-FUNCTIONAL Code that will add a new combo to the menu, and will add new
items to
that combo"""


from easygui import *


# from 05_edit_combo_v2
def choose_item(combo, combo_name):
    items = []
    for item in combo:
        items.append(f"{item[0]} ${item[1]:.2f}")
    items += ["Save", "Cancel"]

    msg = f"Choose item from *{combo_name}* to edit"

    chosen_item_text = buttonbox(msg, "Edit combo", choices=items)

    if chosen_item_text in ("Save", "Cancel"):
        return chosen_item_text

    # code that converts item from its text form "name $0.00" to code form
    # this will not work if multiple items have same name within combo
    chosen_item_name = chosen_item_text.split("$")[0].strip()

    for item in combo:
        if item[0] == chosen_item_name:
            chosen_item = item

    return chosen_item


# from 05_edit_combo_v2
def get_new_price():
    try:
        new_price = enterbox("Enter new price", "Set price").strip("$")

        try:
            new_price = float(new_price)
        except ValueError:  # none-float input given
            msgbox("Please enter a valid number", "Set price")
            return get_new_price()

    except AttributeError:  # no input given

        return None

    return new_price


# from 05_edit_combo_v2
def choose_attribute(item, combo_name):
    attributes = item
    attributes[1] = f"${attributes[1]:.2f}"  # format float as a currency str

    msg = f"Choose attribute from {item[0]} in {combo_name}\n\nName or Price"

    attribute = buttonbox(msg, "Choose attribute", choices=item)

    attributes[1] = float(attributes[1].strip("$"))  # format back to float

    return attribute


# from 05_edit_combo_v2
def set_attribute(item, attribute):
    item_temp = item.copy()

    # if price selected
    if attribute[0] == "$":
        new_price = get_new_price()
        if new_price:  # if not None
            item_temp[1] = new_price

    # if name selected
    else:
        new_name = enterbox("Enter new name", "Set name")
        if new_name:  # if not None
            item_temp[0] = new_name

    return item_temp


# from 05_edit_combo_v2
def edit(menu, selected_combo):
    # create a copy of the selected combo
    combo_temp = menu[selected_combo].copy()

    while True:
        # display possible items to choose, output selected item
        selected_item = choose_item(combo_temp, selected_combo)
        if selected_item == "Save":
            menu[selected_combo] = combo_temp
            return menu
        elif selected_item == "Cancel":
            return menu
        else:
            # display attributes of item to choose, output selected attribute
            selected_attribute = choose_attribute(selected_item, selected_combo)

            # allow user to re-enter attribute, output new item
            item_temp = set_attribute(selected_item, selected_attribute)

            # set new item in combo temp
            for i, item in enumerate(combo_temp):
                if item[0] == selected_item[0]:
                    combo_temp[i] = item_temp


def get_new_name():
    new_name = enterbox("Enter new name", "Set name")
    if not new_name:
        msgbox("Please enter a valid name", "Set name")
        return get_new_name()
    return new_name


def add_item(combo):
    new_name = get_new_name()
    new_price = get_new_price()
    return [new_name, new_price]


def add_combo(menu):
    new_combo_name = enterbox("Enter Combo Name", "Add Combo")

    combo_temp = []

    for i in range(0, 3):
        combo_temp.append(add_item(combo_temp))

    menu[new_combo_name] = combo_temp

    menu = edit(menu, new_combo_name)


    return menu


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

burger_combo_menu = add_combo(burger_combo_menu)

print(burger_combo_menu)
