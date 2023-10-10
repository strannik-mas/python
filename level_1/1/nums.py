import random
n1 = random.randrange(1,11)
n2 = random.randrange(1,11)

###n2 = 3
#s = str(n1) + ' + ' + str(n2) ' = ' + str(n1 + n2)
#s = '{} + {} = {}'.format(n1,n2,n1+n2)
#s = f'{n1} + {n2} = {n1+n2}'
##w = input('enter length: ')
##w = int(w)
##h = input('enter heigth: ')
##h = int(h)
##s = f'square {w}x{h}  = {w*h}'
##print(s)
#answer = input('сколько будет 2+2? ')
while True:
    answer = input(f'сколько будет {n1}+{n2}? ')
    test = answer.replace('.','',1)
    if not test.isdigit():
        print('nado chislo')
        continue
    else:
        if answer == test:
            answer = int(answer)
        else:
            answer = float(answer)
        #if answer.isdigit():
        if answer == n1 + n2:
            print('yes')
            break
        else:
            print('no')
        #else:
            #print('nado chislo')

