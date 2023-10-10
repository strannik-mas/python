import re
with open('lab_8_log.txt', 'r+', encoding='utf-8') as f:
    for line in f:
        r = re.search(r'(\d{3}) (прибыл|отправился) (из|в) (\w+) в (\d{2}:\d{2}:\d{2})', line)
        if r is not None:
            with open('lab_8_train.txt', 'a', encoding='utf-8') as f:
                f.write('[' + r.group(5) + '] - Поезд № ' + r.group(1) + ' ' + r.group(3) + ' '  + r.group(4) + '\n')
        