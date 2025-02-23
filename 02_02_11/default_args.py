def sum(x = None, y = None):
    x = x or 0
    y = y or 0
    result = x + y
    return result


harry = 1
potter = 2
apple = sum(harry, potter)
print(apple)
