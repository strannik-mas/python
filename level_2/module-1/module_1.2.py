import random


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Я - точка: {self.x} x {self.y}'

from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Point3D(Point):
    def __init__(self, x, y, z):
        self.z = z
        Point.__init__(self,x,y)

    def move_by(self, x, y, z):
        self.x += x
        self.y += y
        self.z += z

    def move_to(self, x, y, z):
        self.z = z
        super().move_to(x, y)

    def __repr__(self):
        # s = Point.__repr__(self)
        s = super().__repr__()
        return f'{s} x {self.z}'


class Human:
    def __init__(self, name, sex):
        self.sex = sex.upper()
        self.name = name
        self.status = None

    #def marry(self, human):
    def __add__(self, human):
        if isinstance(human, Human):
            self.status = human
            human.status = self
        else:
            raise TypeError('Object human not a human')

    # def make_children(self, partner):
    def __mul__(self, partner):
        if self.status == partner and self.sex != partner.sex:
            return Human('', random.choice(['M', 'W']))
        else:
            raise Exception('Не могут иметь детей!')


john = Human('John', 'm')
mike = Human('Майк', 'm')
ann = Human('Ann', 'w')
sara = Human('Sara', 'w')
#john.marry(ann)
john + ann
#john.make_children(sara)
#baby = john.make_children(ann)
baby = john * ann
print(john.status.name)
print(ann.status.name)
print(baby)


# p = Point(10,20)
# p3d = Point3D(30, 40,50)
# p.move_to(100,200)
# p3d.move_by(300,400, 10)
# p3d.move_to(100,100, 10)
#
# # print(p3d.x, p3d.y)
# print(p)
# print(p3d)
# print(Color.RED)


