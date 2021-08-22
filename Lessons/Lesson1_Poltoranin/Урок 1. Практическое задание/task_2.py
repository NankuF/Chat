"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

s1 = b'class'
s2 = b'function'
s3 = b'method'
print(s1, '|', type(s1), '|', 'len:', len(s1))
print(s2, '|', type(s2), '|', 'len:', len(s2))
print(s3, '|', type(s3), '|', 'len:', len(s3))


def bin_format(*args: str) -> []:
    lst = [*args]
    lst_b_string = []
    for i in lst:
        lst_b_string.append(bytes(i, 'utf-8'))

    bin_s = ''
    bin_lst = []
    for i, el in enumerate(lst_b_string):
        for els in el:
            bin_s += bin(els)
        bin_s = bin_s.replace('b', '')  # необязательно удалять, можно и так chr(int('0b1100011',2) == 'c'
        bin_lst.append((bin_s, lst[i]))
        bin_s = ''

    return bin_lst


result = bin_format('class', 'function', 'method')
# print('Рез-т работы ф-ии: ', result)
for i in result:
    print(type(i[0]), i[0], '| Длина:', len(i[0]), '| Слово:', i[1])

# c = b'c'  # указываем что строка байтовая
# b = ''
# s = ''
# for el in c:
#     b += bin(el)  # преобразуем байтовую строку в бинарный формат
#     s += chr(int(b, 2))  # преобразуем бинарный формат в буквы (привычные символы)
# print(b, s)
