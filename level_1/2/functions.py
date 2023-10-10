def seconds_per_day(days=1):
    h = 24 * days
    m = h * 60
    s = m * 60
    #print(s)
    return days * 86400
print(__name__)
if __name__ == '__main__':
    sec = seconds_per_day()
    print(sec)

##def area_of_disk(radius):
##    return 3.14*radius**2
##
def area_of_ring(outer, inner):
    return area_of_disk(outer) - area_of_disk(inner)
##
##sq = area_of_ring(40, 25)
##print(sq)

#x = 10;
#def fn(x):
##def fn():
##    global x
##    print(x)
##    x = 20
##    print(x)
##print(x)
###fn(0)
##fn()
##print(x)
##def fn(a, b=2, c=3):
##    pass
##
##fn(10, c=20) #указать имя параметра
##fn(c=30, a=5)
##def fn(*params):
##    #print(type(params))
##    for p in params:
##        print(p)
##fn(1,2,3,4)
##def fnn(**params):
##    for p, m in params.items():
##        print(p, m)
##fnn(John=100, Mike=200)
    
def area_of_disk(radius):
    '''Help on function:
        area_of_disk(number) -> number
        Return area of disk by radius
    '''
    return 3.14*radius**2
##print(area_of_disk(55))