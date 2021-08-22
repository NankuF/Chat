"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

lst = ['разработка', 'администрирование', 'protocol', 'standard']
lst_encode = []
lst_decode = []
for i in lst:
    lst_encode.append(i.encode(encoding='utf-8'))

for i in lst_encode:
    lst_decode.append(i.decode(encoding='utf-8'))

print(lst_encode)
print(lst_decode)
