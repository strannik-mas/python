#Абстрактные структуры данных: Стек
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


def is_palindrome(word):
    word = word.lower().replace(' ', '')
    rword = ""

    stack = Stack()

    for char in word:
        stack.push(char)

    while not stack.is_empty():
        rword += stack.pop()

    return word == rword;

# print(is_palindrome('privet'))
# print(is_palindrome('наган'))
# print(is_palindrome('а роза упала на лапу азора'))

def brackets_checker(s):
    stack = Stack()
    o_allowed = '{[('
    c_allowed = '}])'

    def matches(o, c):
        try:
            return o_allowed.index(o) == c_allowed.index(c)
        except:
            return False

    for char in s:
        #if char == '(':
        if char in o_allowed:
            stack.push(char)
        else:
            if stack.is_empty():
                return False
            else:
                #stack.pop()
                if not matches(stack.pop(), char):
                    return False

    if stack.is_empty():
        return True
    return False

# print(brackets_checker('(()(()))'))
# print(brackets_checker(')(()(()))'))
# print(brackets_checker('((()(()))'))
# print(brackets_checker('(({})(([])))'))

import math
def convertor(dec, base=2):
    allowed = '0123456789ABCDEF'
    stack = Stack()
    while dec > 0:
        stack.push(dec%base)
        dec = math.floor(dec/base)
    s = ''
    while not stack.is_empty():
        #s += str(stack.pop())
        s += allowed[stack.pop()]
    return s

print(convertor(196, 7))
print(convertor(196, 8))
print(convertor(196, 2))
print(convertor(196, 16))
print(convertor(255))
print(convertor(56))


