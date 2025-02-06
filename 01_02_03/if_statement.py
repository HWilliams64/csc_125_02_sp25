import sys
# Keywords
# if - at statement for conditional execution
# else - at statement execution when the original condition is false
# elif - at statement for conditional execution when the original condition is false

# Syntax
# if <logical expression>:
#    <statement>
#    <statement>
#    <statement>

number_1 = 0
number_2 = 0

# 1) Ask for an input from the user ==========================================

user_input = input("Enter a number: ")
# Input is a function waits for user input and returns a string

is_number = user_input.isnumeric()
# isnumeric is a method that checks if the string is a number

if is_number:
    number_1 = float(user_input)
    # int() converts (parse/cast) a string to an integer

    print("User input is a number:", number_1, type(number_1))

else:
    print(f"User input \"{user_input}\" is not a number")
    sys.exit(1)

#  2) Ask for an input from the user ==========================================
user_input = input("Enter a number: ")

if user_input.isnumeric():
    number_2 = float(user_input)
    print("User input is a number:", number_2, type(number_2))

else:
    print(f"User input \"{user_input}\" is not a number")
    sys.exit(1)

#  3) Compare the two numbers ================================================

if number_1 != number_2:
    print(f"{number_1} is not equal {number_2}")
elif number_1 > number_2:
    print(f"{number_1} is greater than {number_2}")
elif number_1 < number_2:
    print(f"{number_1} is less than {number_2}")
else:
    print(f"{number_1} is equal to {number_2}")
