import random
colDv = 3
d = random.randrange(1,4)
ishVeroyatnost = int(100 / colDv)
while True:
    variant1 = input('выбери номер двери от 1 до 3 ')
    if variant1.isdigit() and int(variant1) >= 1 and int(variant1) <=3:
        colDv = 2;
        ver2 = int(100 / colDv);
        print(f'ish ver = {ishVeroyatnost}, ver posle vibora = {ver2}')
        print(f'вероятность увеличится на {ver2-ishVeroyatnost} процентов')
        break
