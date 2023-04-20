"""Code that will allow the user to create a new combo, then choose to
edit, save, or cancel"""

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

            # Display details
            print(f"* {selected_combo} *")
            for item in combo_temp:
                print(f"-{item[0]} - ${item[1]:.2f}")
            print()

            return menu
        elif selected_item == "Cancel":
            return menu
        else:
            # display attributes of item to choose, output selected attribute
            selected_attribute = choose_attribute(selected_item,
                                                  selected_combo)

            # allow user to re-enter attribute, output new item
            item_temp = set_attribute(selected_item, selected_attribute)

            # set new item in combo temp
            for i, item in enumerate(combo_temp):
                if item[0] == selected_item[0]:
                    combo_temp[i] = item_temp


def get_new_name(msg, title):
    new_name = enterbox(msg, title)
    if not new_name:
        msgbox("Please enter a valid name", title)
        return get_new_name()
    return new_name


def create(menu):
    msgbox("For the purposes of this program, you will be limited to 3 items "
           "in each combo.", "Create Combo")

    new_combo_name = get_new_name("Enter a name for the combo",
                                  "Set New Combo Name")

    combo_temp = []
    for i in range(0, 3):
        new_name = get_new_name(f"Enter name of combo item {i + 1}",
                                "Add Item to New Combo")
        new_price = get_new_price()
        combo_temp.append([new_name, new_price])

    # Display details
    print(f"* {new_combo_name} *")
    for item in combo_temp:
        print(f"-{item[0]} - ${item[1]:.2f}")
    print()

    return add(menu, combo_temp, new_combo_name)


def add(menu, combo, combo_name):
    # create a temporary menu with only new combo in it
    menu_temp = {
        combo_name: combo
    }

    while True:
        choice = buttonbox("Combo details have been printed to console.\n\n"
                           "Click 'Save' to add combo to the menu.",
                           "Create Combo",
                           choices=["Edit", "Save", "Cancel"])

        if choice == "Edit":
            menu_temp = edit(menu_temp, combo_name)

        elif choice == "Save":
            menu.update(menu_temp)
            return menu

        elif choice == "Cancel":

            choice = buttonbox(f"Are you sure? All of *{combo_name}* will be "
                               f"deleted.", "Cancel Creation",
                               choices=["NO", "Yes"])
            if choice == "Yes":
                return menu  # unchanged menu


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

burger_combo_menu = create(burger_combo_menu)

print(burger_combo_menu)
