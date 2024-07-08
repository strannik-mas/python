import random
from random import randrange as rand
import abc

# # Модуль 2. Практическая работа

# ## Игра с геометрическими фигурами

class IShape(abc.ABC):
    '''Интерфейс для реализации геометрических фигур'''

    @abc.abstractmethod
    def get_perimeter(self):
        '''Возвращает периметр фигуры'''
        pass

    @abc.abstractmethod
    def get_area(self):
        '''Возвращает площадь фигуры'''
        pass

    @abc.abstractmethod
    def get_description(self):
        '''Возвращает произвольное описание фигуры'''
        pass


class Circle(IShape):
    PI = 3.14
    def __init__(self, radius):
        self.__radius = radius
    def get_perimeter(self):
        return self.__radius * 2 * self.PI

    def get_area(self):
        return self.__class__.PI * self.__radius**2

    def get_description(self):
        return f'Я - окружность с радиусом {self.__radius}'

class Rectangle(IShape):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def get_a(self):
        return self.__a

    a = property(get_a)

    def get_perimeter(self):
        return (self.__a + self.__b) * 2

    def get_area(self):
        return self.__a * self.__b

    def get_description(self):
        return f'Я - прямоугольник со сторонами {self.__a} и {self.__b}'

class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

    def get_description(self):
        return f'Я - квадрат со стороной {self.a}'


# class Game():
#     @staticmethod
#     def get_shape(self):
#         cls = random.choice(['Circle', 'Square', 'Rectangle'])
#         if cls == 'Circle':
#             self.__figure = Circle(random.randrange(1,10))
#         elif cls == 'Square':
#             self.__figure = Square(random.randrange(1,10))
#         else:
#             self.__figure = Rectangle(random.randrange(1,10), random.randrange(1,10))
#         return self.__figure.get_description()
#
#     @staticmethod
#     def calculate(self):
#         self.__answer = input('Играем? Y/N: ')
#         if self.__answer == 'y':
#             answerSquare = input('Укажите мою площадь: ')
#             area = self.__figure.get_area()
#             if float(answerSquare) == area:
#                 print('Правильно!')
#             else:
#                 print(f'Ошибка! Правильный ответ: {area}')
#
#             answerPerimeter = input('Укажите мой периметр: ')
#             perimeter = self.__figure.get_perimeter()
#             if float(answerPerimeter) == perimeter:
#                 print('Правильно!')
#             else:
#                 print(f'Ошибка! Правильный ответ: {perimeter}')
#         else:
#             print('Спасибо за участие!')
#
#
#     def run(self):
#         print(Game.get_shape(self))
#         Game.calculate(self)
#
#
#     def play(self):
#         self.__answer = ''
#         print('Привет! Мы геометрические фигуры и у нас есть 2 вопроса.')
#         while self.__answer != 'n':
#             self.run()

class Game:
    QUESTION_COUNT = 2

    def __init__(self):
        raise Exception('Нельзя создать экземпляр данного класса!')

    @staticmethod
    def __get_shape():
        type = rand(3)
        if type == 0:
            return Circle(rand(1,10))
        if type == 1:
            return Rectangle(rand(1, 10), rand(1,10))
        if type == 2:
            return Square(rand(1,10))

    @staticmethod
    def __calculate(string, answer):      #'площадь', 24 - правильный ответ
        while True:
            guess = input(f'Укажите {string} этой фигуры: ').strip()
            if not guess.replace('.', '', 1).isdigit():
                print('введи число!')
                continue
            break
        if float(guess) == answer:
            print('Правильно!')
        else:
            print(f'Ошибка! Правильный ответ: {answer}')

    @classmethod
    def __run(cls):
        shape = cls.__get_shape()
        if isinstance(shape, IShape):
            print(shape.get_description())
            cls.__calculate('площадь', shape.get_area())
            cls.__calculate('периметр', shape.get_perimeter())
        else:
            raise TypeError('Не та фигура!')

    @classmethod
    def play(cls):
        print(f'Привет! Мы геометрические фигуры и у нас есть {cls.QUESTION_COUNT} вопроса.')
        while True:
            is_game_over = input('Играем? Y/N: ').strip()
            if is_game_over.upper() == 'N':
                break
            cls.__run()

        print('Спасибо за участие!')


# g = Game()
# g.play()

Game.play()
