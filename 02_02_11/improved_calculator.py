def number_input():
    while True:
        user_input = input("Enter a number: ")
        user_input = user_input.strip()  # Remove leading and trailing spaces
        formatted_num = user_input.replace(".", "", 1).replace("-", "", 1)
        if not formatted_num.isnumeric():
            print(f"User input \"{user_input}\" is not a number")
            continue  # Skip the rest of the code block and go back to the beginning
        break  # Stope the loop

    return float(user_input)

while True:

    number_1 = number_input()
    number_2 = number_input()

    print(number_1 + number_2)

    user_input = input("Do you want to continue? (y/n): ")
    if user_input.lower() != "y":
        print("Goodbye!")
        break
