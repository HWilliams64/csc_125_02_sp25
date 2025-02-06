var = True
var = False


# Key Word
# and = > * or x => multiply
# or = > + => addition

# Rules
# True => 1
# False => 0
# and => *
# or => +
# any number greater than 1 => True
# Orders of operation (), *, +

var = True and False
print("True and False =", var)
# True and False => 1 * 0 => 0

var = True or False
print("True or False =", var)
# True or False => 1 + 0 => 1

var = True or True
print("True or True =", var)
# True or True => 1 + 1 => 2 => True

x = 10
y = 4
var = x > y and y < x
# x > y => 10 > 4 => True
# y < x => 4 < 10 => True
# True and True => 1 * 1 => 1 => True

print("x > y and y < x =", var)

# >, <, >=, <=, ==, !=, is
# == : value comparison
# is : identity comparison

s1 = "Hello"
s2 = "hello"
var = s1 == s2
print("s1 == s2 =", var)

var = s1 != s2
print("s1 != s2 =", var)

var = s1 is s2
print("s1 is s2 =", var)

s1 = "Hello" * 80_000
s2 = "Hello" * 80_000
var = s1 is s2
print("s1 is s2 =", var)


s1 = "Hello"
s2 = 'Hello'
var = s1 == s2
print("s1 == s2 =", var)

# keyword not

var = not True
print("not True =", var)

var = not False
print("not False =", var)


var = not True and False
print("not True and False =", var)
