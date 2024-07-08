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


#игра Hot potato
def hot_potato(names, num):
    queue = Queue()
    for name in names:
        queue.enqueue(name)

    queue.show()

    eliminated = ''
    while queue.size() > 1:
        for i in range(num):
            queue.enqueue(queue.dequeue())

        queue.show()
        eliminated = queue.dequeue()
        print(f'{eliminated} вышел из игры')

    return queue.dequeue()

names = ['vasya', 'sucka', 'petya', 'blad', 'katya', 'fedya']
# winner = hot_potato(names, 5)
# print(f'{winner} победил')

lst = ['9 Ivanov', '10 Petrov', '11 Sidorov', '9 Morozov', '9 Belyaev', '10 Nikitin']

def list_of_students(lst):
    q9 = Queue()
    q10 = Queue()
    q11 = Queue()

    for item in lst:
        student = item.split(' ')
        if (student[0] == '9'):
            q9.enqueue(student[1])
        elif (student[0] == '10'):
            q10.enqueue(student[1])
        elif (student[0] == '11'):
            q11.enqueue(student[1])

    while q9.size() > 0:
        print('9 ', q9.dequeue())
    while q10.size() > 0:
        print('10 ', q10.dequeue())
    while q11.size() > 0:
        print('11 ', q11.dequeue())

# list_of_students(lst)

#сортировка разрядная
import math
class RadixSort:
    def __init__(self, n):
        self.bins = list()
        self.nums = n
        for i in range(10):
            self.bins.append(Queue())

    def distibute(self, digit):
        for i in range(10):
            if digit == 1:
                self.bins[self.nums[i]%10].enqueue(self.nums[i])
            else:
                self.bins[math.floor(self.nums[i] // 10)].enqueue(self.nums[i])

    def collect(self):
        i = 0
        for digit in range(10):
            while not self.bins[digit].is_empty():
                self.nums[i] = self.bins[digit].dequeue()
                i += 1

    def show(self):
        return ''.join(str(self.nums))


from random import randrange
nums = []
for i in range(10):
    nums.append(randrange(100))

rs = RadixSort(nums)
print('before: ', rs.show())
rs.distibute(1)
rs.collect()
print('middle: ', rs.show())
rs.distibute(10)
rs.collect()
print('after: ', rs.show())



# class PriorityQueue(Queue):
#     pass
#
# class Client:
#     def __init__(self, name, priority):
#         self.priority = priority
#         self.name = name
#
#
# q = PriorityQueue()
# q.enqueue(Client('jon', 2))
# q.enqueue(Client('her', 1))

# class Deque:
    #Queue -(enqueue, dequeue) +
    #add_front()
    #add_rear()
    #remove_front()
    #remove_rear()

# def is_palindrom(string):
#     d = Deque()
#     for char in string:
#         d.add_rear(char)
#
#     while d.size() > 1:
#         if d.remove_front() != d.remove_rear():
#             return False
#     return True


