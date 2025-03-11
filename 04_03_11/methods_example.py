from typing import Union


class Coordinate:

    def __init__(self, x: Union[int, float], y: Union[int, float]):
        self.x = x
        self.y = y

    def add(self, x: Union[int, float], y: Union[int, float]):
        self.x += x
        self.y += y


point_1 = Coordinate(0,0)
print("Coordinate", point_1.x, point_1.y)
point_1.add(1, 1)
print("Coordinate", point_1.x, point_1.y)
