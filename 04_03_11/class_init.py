from typing import Any, List

print(" WITH INIT ".center(40, "="))
class MyClass:

    def __init__(self, x:Any, y:Any, array:List):
        self.x = x
        self.y = y
        self.array = array


my_obj = MyClass(0, 0, [1, 2, 3])
x = my_obj.x
y = my_obj.y

x = 9

print("X", x)
print("my_obj.x", my_obj.x)
print("Y", y)
print("my_obj.y", my_obj.y)

my_obj.x = "happy panda"
print("my_obj.x", my_obj.x)

print('='*30)
external_array = my_obj.array
print("external_array", external_array)
external_array[0] = 100
print("external_array", external_array)
print("my_obj.array", my_obj.array)


print('='*30)
my_obj_2 = MyClass(0, 0, [1, 2, 3])
my_obj_2.x = 10
my_obj_2.y = 10
print("my_obj_2.x", my_obj_2.x)
print("my_obj_2.y", my_obj_2.y)
print("my_obj_2.array", my_obj_2.array)
print('-'*30)
print("my_obj.x", my_obj.x)
print("my_obj.y", my_obj.y)
print("my_obj.array", my_obj.array)
