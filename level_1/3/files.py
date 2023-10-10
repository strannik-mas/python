##f = open('test.txt', 'r+', encoding='utf-8')
##
##f.close()
with open('test.txt', 'r+', encoding='utf-8') as f:
##    print(f.read(5))
##    print(f.read(3))
    print(f.read())
    ##print(f.readline())
##    s = f.readline()
##    while s:
##        print(s)
##        s = f.readline()
    #lines = f.readlines()
    
#print(lines)
#for line in lines:
##    for line in f:
##        print(line)

##with open('test.txt', 'a', encoding='utf-8') as f:
##    f.write('\nLine six')
##    print(f.closed)
##    print(f.mode)
##    print(f.name)
##import csv
#with open('data.csv', 'r', encoding='utf-8') as f:
##    reader = csv.reader(f, delimiter=',')
##    for row in reader:
##        print(row)
##with open('data.csv', 'a', encoding='utf-8', newline='\n') as f:
##    writer = csv.writer(f, delimiter=',')
##    writer.writerow([])
##    writer.writerow(['Suka', 'hren', '222', '234-33-44'])

import os
print(os.path.exists('test.txt'))
print(os.getcwd())
print(os.listdir('.'))


