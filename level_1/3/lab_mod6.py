def read_file(name):
    with open(name, 'r', encoding='utf-8') as f:
        stroka = f.read()
        stroka = stroka.lower()
        stroka = stroka.replace(',', '')
        stroka = stroka.replace(':', '')
        stroka = stroka.replace('.', '')
        spisok = stroka.split()
        return set(spisok)
    
def save_file(filename, words):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('Всего уникальных слов: ' + str(len(words)) + '\n')
        f.write('======================\n')
        for w in sorted(words):
            f.write(w + '\n')
    

w = read_file('dz_lab_mod6.txt')
save_file('lab_6_res.txt', w)