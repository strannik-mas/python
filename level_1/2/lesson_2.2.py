#подключение модулей

##import math
##math.cos(1)
#from math import cos as math_cos, sin
##import numpy
##print(numpy.tan(3))
##print(numpy.product([1,2,3,4,5]))
#import functions
#print(dir(functions))
#print(__name__)
#import mylib.geos
import mylib.geos.areas
import mylib.times
#print(dir(mylib.geos))
a = mylib.geos.areas.area_of_disk(10)
print(a)