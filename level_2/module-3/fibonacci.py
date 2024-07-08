def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)      #O(2**n)

def fib2(n):
    f = [0, 1, 1]
    for i in range(3, n):
        f.append(f[i-1] + f[i-2])
    return f[len(f)-1]      #O(n) + memory

def fib3(n):
    a, b = 0, 1
    for _ in range(n-1):   #without index
        a, b = b, a + b #переприсваивание b ->a a+b -> b
    return a        #O(n)

print(fib(5))
print(fib2(5))
print(fib3(5))


