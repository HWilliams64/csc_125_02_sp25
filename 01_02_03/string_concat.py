w1 = "Hello"
w2 = "World"

# When we use the + operator with strings, it concatenates them. This means we
# are adding them together to form a single string.

print(w1 + " " + w2)

# str() is a function that converts a value to a string
var = 2
print(w1 + " " + w2 + str(var))

# Formatted strings are strings that have placeholders for variables. The format
# method is used to replace the placeholders with the variables.
day = "Monday"
var_str = "I want {} apple pies on {}".format(var, day)
print(var_str)

# f-strings are formatted strings that have placeholders for variables. The
# variables are placed inside curly braces. The variables are replaced with the
# values when the string is evaluated.
template = f"I want {var*20} apple pies on {day}"
print(template)
