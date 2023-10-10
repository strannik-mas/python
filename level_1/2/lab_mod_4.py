##import random
##def birthday(iterations):
##    successes = 0
##    while True:
##        colChelovek = input('enter number of people ')
##        if colChelovek.isdigit() and int(colChelovek) >= 1:
##            colChelovek = int(colChelovek)
##            break
##    for i in range(1, iterations):
##        test = [random.randint(1, 365) for i in range(colChelovek)]
##        if len(test) != len(set(test)):  # День рождения совпал, т.к. в множестве нет повторений
##            successes += 1
##    return successes*100/iterations
import paradox.birthday
##v = birthday(1000)
##print(v)
print(paradox.birthday.birthday(1000))