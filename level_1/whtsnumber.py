import random
num = random.randrange(1,11)

while True:
    answer = input('enter chislo ')
    if not answer.isdigit():
        print('nado chislo')
        continue
    answer = int(answer)
    if answer > num:
        print('chislo menshe')
    elif answer < num:
        print('chislo bolshe')
    else:
        print('ugadal')
        break
        
