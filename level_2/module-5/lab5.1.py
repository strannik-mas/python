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

class DanceFloor:
    def __init__(self, fileName):
        self.fileName = fileName
        self.pairs = list()
        self.qMen = Queue()
        self.qWomen = Queue()

    def dance(self):
        with open(self.fileName, 'r+', encoding='utf-8') as f:
            for line in f.readlines():
                lineArr = line.split(' ')
                if lineArr[0] == 'М':
                    self.qMen.enqueue(lineArr[1])
                else:
                    self.qWomen.enqueue(lineArr[1])

        while not self.qWomen.is_empty() and not self.qMen.is_empty():
            i = 0
            self.pairs.append(str(self.qWomen.dequeue()) + ' и ' + str(self.qMen.dequeue()))
            i += 1

        print('Образовались следующие пары:')
        for p in self.pairs:
            print(p)
        if self.qMen.size() > 0:
            print(f'Мальчиков в очереди: {self.qMen.size()} и первый из них - {self.qMen.front()}')
        else:
            print(f'Девочек в очереди: {self.qWomen.size()} и первая из них - {self.qWomen.front()}')
