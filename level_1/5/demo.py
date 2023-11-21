##def hello(name):
##    return 'Hi ' + name
##
##hi = hello

#print(hi('jogh'))

##def sum_of_ints(start, end):
##    n = 0
##    for i in range(start, end + 1):
##        n += i
##        return n
##    
##def sum_of_squares(start, end):
##    n = 0
##    for i in range(start, end + 1):
##        n += i ** 2
##        return n
##    
##def sum_of_cubes(start, end):
##    n = 0
##    for i in range(start, end + 1):
##        n += i ** 3
##        return n

##def sum_of(start, end, fn):
##    n = 0
##    for i in range(start, end + 1):
##        n += fn(i)
##    return n
    
##def ints(x): return x
##def squares(x): return x ** 2
##def cubes(x): return x**3
##def areas(x): return x**2 * 3.14

##print(sum_of(1, 10, lambda x: x))
##print(sum_of(1, 10, lambda x: x ** 2))
##print(sum_of(1, 10, lambda x: x ** 3))
##print(sum_of(1, 10, lambda x: x ** 2 * 3.14))
##print(sum_of(1, 10, squares))
##print(sum_of(1, 10, cubes))

##lst = [1,2,3,4,5,6,7]
##new_lst = []
#императив
##for item in lst:
##    new_lst.append(str(item))

#функциональное решение/декларативное
##new_lst = list(map(str, lst))
##new_lst = list(map(lambda x: x*10, lst))

##lst = [6, 3,7,2,5,6,8,8,9,4,8]
##filtered = set(filter(lambda i: i > 5, lst))

##from functools import reduce
##lst = [0,1,2,3,4,5]
##sum_all = reduce(lambda a,b: a + b, lst, 100)
##lst = [6, 3,7,2,5,6,8,8,9,4,8]
##max_item = reduce(lambda a,b: a if (a>b) else b, lst)

##a = [1,2,3]
##b = 'xyz'
##c = (None, True, False)
##
##z = list(zip(a,b,c))

##lst = [6, 3,7,2,5,6,8,8,9,4,8]
##lst = list(filter(lambda i: i > 5, lst))
##lst = list(map(lambda i: i*10, lst))
##sum_all = reduce(lambda a,b: a + b, lst)
##
##lst2 = [6, 3,7,2,5,6,8,8,9,4,8]
##sum_all2 = reduce(lambda a,b: a + b, list(map(lambda i: i*10, list(filter(lambda i: i > 5, lst2)))))

##def compose(f, g):
##    return lambda x: f(g(x))
##
##double = lambda x: x * 2
##inc = lambda x: x + 1
##
##inc_and_double = compose(double, inc)
##print(inc_and_double(2))

#def add(x):
##    return lambda y: x + y
##    def ret(y)
##        return y + x
##    return ret

#add = lambda x: lambda y: x + y
##a = add(10) #lambda y: 10 + y
##print(a(5))

##def setup(lst):
##    i=0
##    def ret():
##        nonlocal i
##        v = lst[i]
##        i += 1
##        return v
##    return ret
##
##next_val = setup([1,2,3,4,5])
    

##def add_underscores(fn):
##    return lambda name: '_' + fn(name) + '_'
##def add_underscores(understroke):
##    def decor(fn):
##        def wrapper(name):
##            return '_' + fn(name) + '_' + '\n' + understroke
##        return wrapper
##    return decor
##
##@add_underscores('=============')
##def hello(name):
##    return 'hello, ' + name

##@add_underscores
##def oops():
##    return 'oops'
#hello = add_underscores(hello)
##print(hello('vasya'))
##print(oops())

import functools

@functools.lru_cache(maxsize=None)
def square(n):
    print('here')
    return n**2

print(square(4))
print(square(4))
print(square(4))
print(square(4))
print(square(4))

