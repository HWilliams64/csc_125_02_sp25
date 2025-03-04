my_grocery_list = ["grapes", "eggs", "meat", "cheese", "cheese", "cheese", "eggs"]

while True:
    user_selected_value = input("Enter a value to move to the front of the list: ")

    total_occurrences = my_grocery_list.count(user_selected_value)

    print(f"Before: {my_grocery_list}")
    for _ in range(total_occurrences):
        my_grocery_list.remove(user_selected_value)
    for _ in range(total_occurrences):
        my_grocery_list.insert(0, user_selected_value)
    print(f"After:  {my_grocery_list}")
