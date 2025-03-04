my_grocery_list = ["grapes", "eggs", "meat",
                   "cheese", "cheese", "cheese", "eggs"]

while True:
    user_selected_value = input(
        "Enter a value you want to replace: ")
    user_replacement_value = input(
        "Enter a replacement value: ")

    print(f"Before: {my_grocery_list}")
    # Count the occurrences of the user-selected value in the list
    total_occurrences = my_grocery_list.count(user_selected_value)

    # For each occurrence
    for _ in range(total_occurrences):
        # Find the location of the user-selected value in the list
        index_to_replace = my_grocery_list.index(user_selected_value)

        # Replace the value at the found location with the user-replacement value
        my_grocery_list[index_to_replace] = user_replacement_value
        
    print(f"After:  {my_grocery_list}")
