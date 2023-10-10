import re

##regexp = 'a'
##s = 'vasyA@mail.ru'
##match = re.match(regexp, s)  #ищет вхождения только сначала строки
##match = re.search(regexp, s)
##match = re.findall(regexp, s, re.I)
##print(match.group(0), match.start(), match.end())
##print(s.find('a'))
##print(match)
##split = re.split('-', '10-20-30-40', maxsplit=2)
##sub = re.subn(regexp, 'b', s)
##
##pattern = re.compile(regexp, re.I)
##pattern.search(s)

##s = 'Python Programming. for 1234 the Absolute. Beginner'
email = 'abc.test@gmail.com'
##r = re.findall('.', s)
##r = re.findall('\.', s)
##r = re.findall(r'\n', s)   #сырая строка
##r = re.findall(r'\w', s)   #тоже что . без пробелов [a-zA-Z0-9]    [^a-zA-Z0-9] => \W
##r = re.findall(r'[for]', s)
##r = re.findall(r'[^for]', s)
##r = re.findall(r'[a-zA-Z0-9]', s)
##r = re.findall(r'\w+', s)  #all words min 1 sybol without whitespace {1,}
##r = re.findall(r'\w*', s)    #{0,}
##r = re.findall(r'\w{1,}', s)
##r = re.findall(r'\w{3}', s)
##r = re.findall(r'\w{3} ', s)
##r = re.findall(r'^\w+', s) #begin of string
##r = re.findall(r'\w+$', s)

##r = re.findall(r'@\w+', email)   #'@gmail'
##r = re.findall(r'@\w+.\w+', email) #'@gmail.com'
##r = re.findall(r'\.\w+$', email)
##s = 'abc 12-1234 12-02-2017, asd 56-1235 1-05-2016, xyu 78-1235 25-01-2018'
s = '25-01-2018'
##r = re.findall(r'\d{1,2}-\d\d?-(\d{4})', s)
r = re.search(r'(\d{1,2})-(\d\d?)-(\d{4})', s)
print(r.group(0), r.group(1), r.group(2), r.group(3))
search = re.search(r'@mail|@gmail|@hotmail|@yandex', email)
pos = search.start()
print(pos)