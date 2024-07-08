class Queue:
    def __init__(self):
        self.__data = list()

    def enqueue(self, item):
        self.__data.append(item)

    def dequeue(self):
        if len(self.__data) > 0:
            return self.__data.pop(0)
        return None

    def rear(self):
        if len(self.__data) > 0:
            return self.__data[len(self.__data)-1]
        return None

    def front(self):
        if len(self.__data) > 0:
            return self.__data[0]
        return None

    def is_empty(self):
        return len(self.__data) == 0

    def size(self):
        return len(self.__data)

    def clear(self):
        self.__data = list()

    def show(self):
        print(', ' . join(str(val) for val in self.__data))


class Dancer:
    def __init__(self, name, sex):
        self.sex = sex
        self.name = name

class Dance:
    def __init__(self, filename):
        self.male = Queue()
        self.female = Queue()
        self.__get_dancer(filename)

    def __get_dancer(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.read().split('\n')
        for line in lines:
            dancer = line.strip().split(' ')
            if dancer[0].upper() == 'Д':
                self.female.enqueue(Dancer(dancer[1], dancer[0]))
            else:
                self.male.enqueue(Dancer(dancer[1], dancer[0]))


    def dance(self):
        print('Образовались следующие пары:')
        while not self.female.is_empty() and not self.male.is_empty():
            s = f'{self.female.dequeue().name} и {self.male.dequeue().name}'
            print(s)

        if self.female.size() > 0:
            print(f'Девочек в очереди {self.female.size()}', end='')
            print(f' И первая из них \u2014 {self.female.front().name}')
        if self.male.size() > 0:
            print(f'Мальчиков в очереди {self.male.size()}', end='')
            print(f' И первый из них \u2014 {self.male.front().name}')

process = Dance('dancers.txt')
process.dance()