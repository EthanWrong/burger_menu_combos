"""Code that prints the menu to the console"""


def print_menu(menu):

    print("#### BURGER COMBO MENU ####")
    print()

    for combo in menu:

        # make variable names a bit easier to read and understand
        combo_name = combo
        combo_contents = menu[combo]

        # find total price of combo
        total_price = 0
        for item in combo_contents:
            total_price += item[1]

        # Display Results
        print(f"* {combo_name.upper()} * - ${total_price:.2f}")
        for item in combo_contents:
            print(f"  {item[0]} - ${item[1]:.2f}")

        print()


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
