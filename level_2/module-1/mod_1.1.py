class Lamp:
    brand = 'Phillips'
    count = 0
    def __init__(self, floor=0):
        self.__state = False
        #приватность
        self.__floor = floor
        print(f'Создана лампочка ' + Lamp.brand)
        Lamp.count += 1

    def get_state(self):
        return self.__state

    state = property(get_state)
    # def get_floor(self):
    #     return self.__floor
    # def set_floor(self, v):
    #     self.__floor = v
    # floor = property(get_floor, set_floor)

    #decorator
    #getter
    @property
    def floor(self):
        return self.__floor

    #setter
    @floor.setter
    def floor(self, value):
        self.__floor = value

    def switch_on(self):
        if not self.state:
            print("on")
            self.__state = True
    def switch_off(self):
        if (self.state):
            print('off')
            self.__state = False

    def __repr__(self):
        return f'Я - лампа на {self.floor} этаже'
    @staticmethod
    def foo():
        Lamp.count += 3

    @classmethod
    def foo2(cls):
        cls.count += 3

lamp1 = Lamp(1)
lamp2 = Lamp(4)
lamp3 = Lamp(10)
# print(lamp2)
# s = str(lamp3)
# print(s)
# lamp1.switch_on()
# lamp1.switch_off()

# print(isinstance(lamp1, Lamp))

# print(lamp1.state)
# print(lamp1.floor)
# lamp1.floor = 3
# print(lamp1.floor)
# print(lamp2.floor)
# print(Lamp.brand)
# print(Lamp.floor)