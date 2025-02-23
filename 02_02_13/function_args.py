def my_func(x, y, z=3):
    #print(f"x: {x}, y: {y}, z: {z}")
    return f"x: {x}, y: {y}, z: {z}"


result = my_func(1, 2)

my_func(y=2, x=1)

my_func(1, y=2)
print(result)
