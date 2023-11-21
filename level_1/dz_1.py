import math
#task 4
##while True:
##    n = input('enter number ')
##    if n.isdigit():
##        n = int(n)
##        print(f'Следующее число для числа {n}: {n+1}')
##        print(f'Предыдущее число для числа {n}: {n-1}')
##        break;

#task 5
##while True:
##    n = input('enter number of students: ')
##    k = input('enter number of apples: ')
##    if n.isdigit() and k.isdigit():
##        n = int(n)
##        k = int(k)
##        ya = int(k/n)
##        print(f'Яблок у студентов: {ya}, в корзине: {k-ya*n}')
##        break;

#task 6
##while True:
##    n = input('enter number of seconds after midnight: ')
##    if n.isdigit():
##        n = int(n)
##        chasov = math.floor(n/3600)
##        m = math.floor((n-chasov*3600)/60)
##        print(f'часов: {chasov}, minutes: {m}')
##        break;
    
#task 7
##while True:
##    print('enter first time')
##    h1 = input('enter hours: ')
##    m1 = input('enter minutes: ')
##    s1 = input('enter seconds: ')
##    print('enter second time')
##    h2 = input('enter hours: ')
##    m2 = input('enter minutes: ')
##    s2 = input('enter seconds: ')
##    if h1.isdigit() and m1.isdigit() and s1.isdigit() and h2.isdigit() and m2.isdigit() and s2.isdigit():
##        h1 = int(h1)
##        m1 = int(m1)
##        s1 = int(s1)
##        h2 = int(h2)
##        m2 = int(m2)
##        s2 = int(s2)
##        razn = s2 + m2*60 + h2*3600 - s1 - m1*60 - h1*3600
##        print(f'raznica: {razn}')
##        break;

#ЧИСЛА
#task 1
##while True:
##    n = input('enter number ')
##    if n.isdigit():
##        n = int(n)
##        l = math.floor(n/10)
##        print(f'right part для числа {n}: {n%10}')
##        print(f'left part для числа {n}: {l}')
##        break;

#task2
##while True:
##    n = input('enter number ')
##    if n.isdigit():
##        n = int(n)
##        r = str(n%10)
##        l = str(math.floor(n/10))
##        print(f'chislo naoborot для числа {n}: {r+l}')
##        break;

#task3-4
##while True:
##    n = input('enter number more than 9 ')
##    if n.isdigit() and int(n) > 9:
##        n = int(n)
##        r2 = n%10
##        r3 = n%100
##        r4 = str(math.floor(r3/10))
##        r = str(r3)
##        print(f'последние 2 цифры для числа {n}: {r}')
##        print(f'цифра в ряду десяток для числа {n}: {r4}')
##        break;

#task5
##while True:
##    n = input('enter number ')
##    if n.isdigit() and int(n) > 99:
##        n = int(n)
##        r2 = n%10
##        r3 = n%100
##        r4 = math.floor(r3/10)
##        r5 = math.floor(n/100)
##        summa = r5 + r4 + r2
##        print(f'summa chisel {n}: {summa}')
##        break;
    
#task6
##d = input('enter double number ')
##d1 = float(d)*10
##d2 = math.floor(d1%10)
##print(d2)

###task7
##while True:
##    n = input('enter year ')
##    if n.isdigit():
##        n = int(n)
##        v = math.ceil(n/100)
##        print(f'век для года {n}: {v}')
##        break;

#task8
##while True:
##    n = input('enter day of year ')
##    if n.isdigit():
##        n = int(n)
##        v = n%7
##        if v <=3:
##            v += 3
##        elif v == 4:
##            v = 0
##        elif v==5:
##            v = 1
##        elif v==6:
##            v = 2
##        print(f'день недели дня {n}: {v}')
##        break;

#task9
##while True:
##    n = input('enter minutes after midnite ')
##    if n.isdigit():
##        n = int(n)
##        ch = math.floor(n/60)
##        m = n%60
##        if m == 0:
##            m = '00'
##        print(f'{ch}:{m}')
##        break;

#task10
while True:
    n1 = input('enter number of students in 1 class: ')
    n2 = input('enter number of students in 2 class: ')
    n3 = input('enter number of students in 3 class: ')
    if n1.isdigit() and n2.isdigit() and n3.isdigit():
        n1 = int(n1)
        n2 = int(n2)
        n3 = int(n3)
        st = math.ceil((n1 + n2 + n3)/2)
        print(f'tables need {st}')
        break;
