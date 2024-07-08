class Point:
    __count = 0
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        Point.__count += 1

    @classmethod
    def count_points(cls):
        return cls.__count

    def get_x(self):
        return self.__x
    def set_x(self, v):
        self.__x = v
    x = property(get_x, set_x)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, v):
        self.__y = v

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def __repr__(self):
        return f'Я - точка: {self.x} x {self.y}'

