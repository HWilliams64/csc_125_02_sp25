my_grocery_list = ["grapes", "eggs", "meat", "cheese"]
# Access
first_item = my_grocery_list[0]
print(f"The first item in the list is {first_item}")
last_item = my_grocery_list[-1]
print(f"The last item in the list is {last_item}")

# Slicing
my_grocery_list = ["grapes", "eggs", "meat", "cheese"]

# [start:stop:step]
# stop value is exclusive
first_two_items = my_grocery_list[:2:] # [0:2:1]
print(f"The first two items are {first_two_items}")

# [::-1]
reversed_list = my_grocery_list[::-1]
print(f"The reversed list is {reversed_list}")

# ever other item
every_other_item = my_grocery_list[::2]
print(f"Every other item is {every_other_item}")

# Adding an item
my_grocery_list.append("ice cream") # adds and item to the end
my_grocery_list.append("ice cream")
print(f"The updated list is {my_grocery_list}")

my_grocery_list.insert(0, "milk") # inserts an item at a specific index
print(f"The updated list is {my_grocery_list}")

# I want a particular value to appear first
# what ever the user types in should appear first if already in the list
user_selected_value = input("Enter a value to move to the front of the list: ")

# First check if the user selected value is already in the list
if user_selected_value in my_grocery_list:
    # Get the index of the user selected value
    #user_selected_value_index = my_grocery_list.index(user_selected_value)

    # Remove the user selected value from the list
    my_grocery_list.remove(user_selected_value)

    # Remove the user selected value by index
    #del my_grocery_list[user_selected_value_index]

    # Insert the user selected value at the beginning of the list
    my_grocery_list.insert(0, user_selected_value)

print(f"The updated list is {my_grocery_list}")