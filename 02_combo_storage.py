"""02 Store existing combo meals
Code that can store combo meals, items, and prices."""

# Trial 1: Store inner values as dictionaries
combos_dict = {
    "Value": {
        "Beef burger": 5.69,
        "Fries": 1.00,
        "Fizzy drink": 1.00
    },
    "Cheezy": {
        "Cheeseburger": 6.69,
        "Fries": 1.00,
        "Fizzy drink": 1.00
    },
    "Super": {
        "Cheeseburger": 6.69,
        "Large fries": 2.00,
        "Smoothie": 2.00
    }
}
print("\nCombos Dict", combos_dict)

# Trial 2: Store inner values as lists
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
print("\nCombos List", combos_list)

# Trial 1: Read all details from dictionary/dictionary
print("\nTrial 1 READ")
for combo_name in combos_dict:

    combo_menu = combos_dict[combo_name]
    for combo_item in combo_menu:
        item_price = combo_menu[combo_item]
        print(combo_name, combo_item, item_price)


# Trial 2: Read all details from dictionary/list
print("\nTrial 2 READ")
for combo_name in combos_list:

    combo_menu = combos_list[combo_name]
    for combo_item in combo_menu:
        print(combo_name, combo_item[0], combo_item[1])


# Trial 1: Write a new price to an item in dictionary/dictionary
print("\nTrial 1 WRITE")
selected_combo = "Value"  # this would be player input
selected_item = "Fries"  # this would be player input

if selected_item in combos_dict[selected_combo]:

    combos_dict[selected_combo].pop(selected_item)
    new_item = "New item name"
    combos_dict[selected_combo][new_item] = 16.00

print(combos_dict[selected_combo])

# Trial 2: Writ ea new price to an item in dictionary/list
print("\nTrial 2 WRITE")
selected_combo = "Value"  # this would be player input
selected_item = "Fries"  # this would be player input

for combo_item in combos_list:
    print()  # FIGURE OUT HOW TO CHECK IF ITEM IS IN MENU FOR LIST

if selected_item in combos_list[selected_combo][0]:

    combos_list[selected_combo][0] = "New item name"
    combos_list[selected_combo][1] = 16.00

print(combos_list[selected_combo])
