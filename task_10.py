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
    

class Segment():
    def __init__(self, point1=Point(), point2=Point()):
        self.__a = point1
        self.__b = point2
        self.__intersection = False

    def one_intersection(self):
        x1 = self.__a.get_x()
        y1 = self.__a.get_y()
        x2 = self.__b.get_x()
        y2 = self.__b.get_y()
        if x1 * y1 * x2 * y2 < 0:
            self.__intersection = True
        return self.__intersection

    def __str__(self):
        return f'Отрезок: {self.__a}; {self.__b}'

    def __repr__(self):
        return self.__str__()
    

class CoordinateSystem():
    def __init__(self):
        self.__segments = []

    @property
    def segments(self):
        return self.__segments

    def add_segment(self, ab=Segment()):
        self.__segments.append(ab)
        self.__intersections = 0
    
    def axis_intersection(self):
        for i in self.__segments:
            if i.one_intersection():
                self.__intersections += 1
        
        return self.__intersections

    def __str__(self):
        return f'Плоскость: {self.__segments}'

    def __repr__(self):
        return self.__str__()


coord_sys = CoordinateSystem()
for i in range(5):
    coords1 = tuple([random.randint(-100, 100), random.randint(-100, 100)])
    coords2 = tuple([random.randint(-100, 100), random.randint(-100, 100)])
    coord_sys.add_segment(Segment(Point(coords1), Point(coords2)))

print(coord_sys.axis_intersection())
print(coord_sys.segments)
