from typing import List
try:
    filename: str = input("enter filename  ")
    lst: List[int] = []
    with open(filename, 'r+', encoding='utf-8') as f:
        i: int = 0
        for line in f:
            try:
                line = int(line)
            except ValueError as e:
                print('on line number ' + str(i) + ' appear error:')
                print(e)
            else:
                if (i != 0):
                    lst.append(line)
                else:
                    kol = line
            finally:
                i += 1
        print(i)
        print(kol)
        if i < kol:
            raise Exception('не хватает чисел')
        elif i > kol:
            raise Exception('чисел больше чем надо')
            
except (EOFError, KeyboardInterrupt) as e:
    if type(e) == "EOFError":
        print("eoferror" + e)
    else:
        print("you cancel operation: KeyboardInterrupt " + e)
except FileNotFoundError as e:
    print("not found file " + filename)
    print(e)
except Exception as e:
    print(type(e))
    print(e)
finally:
    print(lst)