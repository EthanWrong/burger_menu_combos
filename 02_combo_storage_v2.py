"""02 Store existing combo meals
Code that can store combo meals, items, and prices.
"""

# Data storage
combos_list = {
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


# Example code for reading data
print("\nTrial 2 READ")
for combo_name in combos_list:

    combo_menu = combos_list[combo_name]
    for combo_item in combo_menu:
        print(combo_name, combo_item[0], combo_item[1])


# Example code for replacing the name and price of an item in the combo
print("\nTrial 2 WRITE")
selected_combo = "Value"  # this would be player input
selected_item = "Fries"  # this would be player input

for item_position, combo_item in enumerate(combos_list[selected_combo]):
    if combo_item[0] == selected_item:
        combos_list[selected_combo][item_position][0] = "New item name"
        combos_list[selected_combo][item_position][1] = 16.00

print(combos_list[selected_combo])
