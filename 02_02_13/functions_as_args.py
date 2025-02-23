from typing import Callable


def add(x: int, y: int) -> int:
    return x + y


def sub(x: int, y: int) -> int:
    return x - y

# f(int, int) -> int
def calc(x: int, y: int, function:Callable[[int, int], int]) -> int:
    result = function(x, y)
    return result

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
op = input("Enter an operator (+, -): ")

if op == "+":
    r = calc(x, y, add)
elif op == "-":
    r = calc(x, y, sub)
else:
    r = "error"

print(f"{x} {op} {y} = {r}")


"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwOi8vYXBpLndzLm5haHRyZWRhcmcuY29tIiwiYXVkIjoiNHpldmRwMnF2c2Vpd2p6ZTM4YW80ZyIsImV4cCI6MTczOTYzNzAzNiwic3ViIjoicHJvLXA4RUtWcjUwTjdBWnpucVciLCJzY29wZSI6W3sibmFtZSI6Ii4qIiwiYWN0aW9uIjoiYWxsb3ciLCJoZWFkZXJzX21hdGNoZXJfb3AiOiJhbmQiLCJoZWFkZXJzX21hdGNoZXIiOltdfV19.PKYilgiyTqbS5i_qFy_4ynoQ0VpSJxcqLpZJxwz56LU"
