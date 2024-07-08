import timeit

def power1(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result

def power2(base, exp):
    if exp == 0:
        return 1
    return base * power2(base, exp - 1)

def power3(base, exp):
    if exp == 0:
        return 1
    if exp % 2 == 0:
        return power3(base, exp / 1) ** 2
    return base * power3(base, exp - 1)
# print(power2(2, 4))
# print(power3(2, 4))
print("one ", timeit.timeit('power1(2, 1000)', globals=globals(), number=1), "milliseconds")
print("two ", timeit.timeit('power2(2, 10)', globals=globals(), number=1), "milliseconds")
print("three ", timeit.timeit('power3(2, 10)', globals=globals(), number=1), "milliseconds")
