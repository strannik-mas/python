#связанный список

#узел
class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def set_next(self, node):
        self.__next = node

    def get_next(self):
        return self.__next

#node = Node(42)

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def is_empty(self):
        return self.__head is None

    def add(self, item):
        node = Node(item)
        node.set_next(self.__head)
        self.__head = node
        if (self.__tail is None):
            self.__tail = node

    def size(self):
        current = self.__head
        count = 0
        while not current is None:
            current = current.get_next()
            count += 1
        return count

    def search(self, item):
        current = self.__head
        while not current is None:
            if current.get_data() == item:
                return True
            else:
                current = current.get_next()
        return False

    def __str__(self):
        if self.__head is None:
            return '[]'
        current = self.__head
        out = '[' + str(current.get_data()) + ', '
        while not current.get_next() is None:
            current = current.get_next()
            out += str(current.get_data()) + ', '
        return out + ']'

    def remove(self, item):
        current = self.__head
        prev = None
        while True:
            if current.get_data() == item:
                break
            else:
                prev = current
                current = current.get_next()
        if prev is None:
            #удаление первого узла
            self.__head = current.get_next()
        else:
            prev.set_next(current.get_next())

    def append(self, item):
        if self.__head is None:
            self.add(self, item)
            return
        node = Node(item)
        # current = self.__head
        # prev = None
        # while current is not None:
        #     prev = current
        #     current = current.get_next()
        # prev.set_next(node) #после цикла тут будет последний узел
        current = self.__tail
        current.set_next(node)
        self.__tail = node

    def index(self, item):
        if self.__head is None:
            return -1
        current = self.__head
        pos = 0
        while True:
            if current.get_data() == item:
                return pos
            else:
                current = current.get_next()
                pos += 1





my_list = LinkedList()
my_list.add(42)
# my_list.add(33)
# my_list.add(17)
print(my_list.size())
