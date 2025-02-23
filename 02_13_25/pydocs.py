def add(x: int = 0, y:int=0) -> int:
    """
    This function adds two numbers and returns their sum.

    Arg:
        x (int): The first number to add.
        y (int): The second number to add.

    Returns:
        int: The sum of x and y.

    >>> r = add(2, 3)
    >>> assert r == 5
    """
    return x + y


# x = int(input("Enter the first number: "))
# y = int(input("Enter the second number: "))
# add(x, y)
# my_multi_line_str = """
# happy
# pandas
# dancing
# in
# the
# moon
# light
# """
# print(my_multi_line_str)
r = add("a", "b")
assert r == 5, f"I expected r to equal 5 but got {r} instead. The function is not working as expected."
