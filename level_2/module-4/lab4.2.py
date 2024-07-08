#vagons

class Stack:
    def __init__(self):
        self.__data = list()

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        if len(self.__data) > 0:
            return self.__data.pop()
        return None

    def peek(self):
        if len(self.__data) > 0:
            return self.__data[len(self.__data)-1]
        return None

    def is_empty(self):
        return len(self.__data) == 0

    def size(self):
        return len(self.__data)

    def show(self):
        print('\n' . join(str(val) for val in self.__data))

def do_lab(train):
    # '3 2 1'
    dock = Stack()
    train = train.split()   #['3', '2', '1']
    train = list(map(int, train)) #[3,2,1]
    list_of_nums = sorted(train.copy())
    #needed = 1  #какой вагон нужен
    needed = list_of_nums.pop(0)

    for cur in train:
        dock.push(cur)
        if cur == needed:
            dock.pop()
            #needed += 1
            if len(list_of_nums):
                needed = list_of_nums.pop(0)
        while dock.size() > 0:
            if dock.peek() == needed:
                dock.pop()
                #needed += 1
                if len(list_of_nums):
                    needed = list_of_nums.pop(0)
            else:
                break

    if dock.is_empty():
        print('Vyveli')
    else:
        print('Neudacha')


while True:
    nums = input('Enter vagons numbers: ')
    if nums == '0':
        break
    do_lab(nums)