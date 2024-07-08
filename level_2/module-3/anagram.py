def anagram1(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    #квадратичная сложность
    array = list(s2)
    pos1 = 0    #позиция для 1 строки
    success = True  #условие прекращение цикла - если не найдена буква
    while pos1 < len(s1) and success:
        pos2 = 0
        found = False
        while pos2 < len(array) and not found:
            if s1[pos1] == array[pos2]:
                found = True
            else:
                pos2 += 1
        if found:
            array[pos2] = None
        else:
            success = False
        pos1 += 1
    return success

def anagram2(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    array1 = list(s1)
    array2 = list(s2)
    array1.sort()   #O(n*log(n)) или O(n^2)
    array2.sort()

    # pos = 0
    # length = len(s1)
    # while pos < length:
    #     if array1[pos] != array2[pos]:
    #         return False
    #     pos += 1
    # return True

    if array1 == array2:
        return True
    return False

def anagram3(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    array1 = [x for x in range(26)]     #количество букв в англ алфавите
    array2 = [x for x in range(26)]
    a_pos = 97      #позиция буквы а

    for char in s1:
        pos = ord(char) - a_pos
        array1[pos] = (array1[pos] or 0) + 1
    for char in s2:
        pos = ord(char) - a_pos
        array2[pos] = (array2[pos] or 0) + 1

    for i in array1:
        if array1[i] != array2[i]:
            return False
    return True
