"""Full code combining all components"""

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
        return get_new_name(msg, title)
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


def main(menu):
    choice = buttonbox("What next?", "Burger Menu Combo Manager",
                       choices=["New Combo", "Search for Combo",
                                "Print Menu",
                                "Exit"])
    if choice == "New Combo":

        menu = create(menu)
        return main(menu)

    elif choice == "Search for Combo":

        combo = search(menu)
        choice = buttonbox(f"What would you like to do with *{combo}* ?",
                           f"Interact with {combo}",
                           choices=["Edit", "Delete"])
        if choice == "Edit":
            menu = edit(menu, combo)
            return main(menu)
        elif choice == "Delete":
            menu = delete(menu, combo)
            return main(menu)

    elif choice == "Print Menu":

        print_menu(burger_combo_menu)
        return main(menu)

    elif choice == "Exit":

        choice = buttonbox("Are you sure you want to exit? "
                           "You will not be able to make further changes",
                           "Exit Burger Menu Combo Manager",
                           choices=["NO", "Yes"])
        if choice == "NO":
            pass
        elif choice == "Yes":
            msgbox("Your menu has been stored in variable 'burger_combo_menu'")
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

welcome()
burger_combo_menu = main(burger_combo_menu)