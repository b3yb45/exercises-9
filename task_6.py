import random

class Point():
    def __init__(self, coords=tuple([0, 0])):
        self.__x, self.__y = coords

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def distance(self, other):
        dx = self.__x - other.get_x()
        dy = self.__y - other.get_y()
        return (dx**2 + dy**2)**0.5
    
    def sum(self, other):
        sum_point = Point((self.__x + other.get_x(), self.__y + other.get_y()))
        return sum_point

    def __str__(self):
        return f'Точка: {self.__x} {self.__y}'

    def __repr__(self):
        return self.__str__()
    

coords1 = tuple([random.randint(-100, 100), random.randint(-100, 100)])
coords2 = tuple([random.randint(-100, 100), random.randint(-100, 100)])
point1 = Point(coords1)
point2 = Point(coords2)

print(point1, point2)

print(point1.get_x(), point1.get_y())
print(point2.get_x(), point2.get_y())
print(round(point1.distance(point2), 2))
point3 = point1.sum(point2)
print(point3)
