import timeit

def my_function():
    # Здесь будет ваш впечатляющий код
    pass

def factorial1(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
def factorial2(n):
    if n == 0:
        return 1
    return n * factorial2(n - 1)
timed_run1 = timeit.timeit('factorial1(10000)', globals=globals(), number=1)
print("one", timed_run1, "milliseconds")
#t1 = Timer("factorial2(50)", "from __main__ import factorial2")
print("two ", timeit.timeit('factorial2(50)', globals=globals(), number=1), "milliseconds")
def factorial3(n, acc = 1):
    if n <= 1:
        return acc
    return factorial3(n - 1, n * acc)   #хвостовая рекурсия
print("three ", timeit.timeit('factorial3(50)', globals=globals(), number=1), "milliseconds")