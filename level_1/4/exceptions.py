##try:
##    long = 20
##    short = 2
##    total = long * 3 + short * 2 #NameError
##    x = 'a' > 1  #TypeError
##    print(total)
##except NameError:
##except (TypeError, NameError):
##    print("error NameError")
##except TypeError:
##    print("error TypeError")
##except:
##    print("emae")
##    txt = input("enter something age:  ")
##    num = int(txt)
##    if num < 18:
##        raise Exception('не подходит по возрасту')
##    print('all right')
##except ValueError as e:
##    print(type(e))
##    print(e)
##except (EOFError, KeyboardInterrupt) as e:
##    if type(e) == "EOFError":
##        print("eoferror")
##    else:
##        print("you cancel operation: KeyboardInterrupt")
##except Exception as e:
##    print(e)
        
##except KeyboardInterrupt:
##    print("you cancel operation: KeyboardInterrupt")
##except:
##    print('something appear')
##else:
##    print("you enter: " + txt)
##finally:
##    print("finally end")
##print("end")

##try:
##    n = 1
##    try:
##        s = 'a' > 1
##    except:
##        print('inner')
##        raise Exception('inner exception')
##    finally:
##        print('ok')
##except:
##    print('outer')
##    raise Exception('from outer exception')
##finally:
##    print('end')
##def one():
##    s = 'a' + 'b'
##    raise Exception('')
##    
##def two():
##    n = 'a' > 1
##    
##def three():
##    pass

##def a():
##    b()
##def b():
##    c()
##def c():
##    d()
##
##def d():
##    if True:
##        raise Exception('error')
##try:
##    x = a()
##    one()
##    two()
##    three()
##except:
##    print('!!')
from typing import List, Dict, Tuple
s: str
n: int = 1
#s = 2

def is_equal(n1: int, n2: int)->bool:
    return n1 == n2

x: int = is_equal(3, 3)
y: int = input('')

lst: List[int]
lst = [1,2,3]
d: Dict[str, int]
t: List[Tuple[int, int]]
