"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции

ВНИМАНИЕ!!: сдача задания
1) создать папку Lesson_1_Ivanov
2) в папку положить файлы task_1 - task_6 (а также txt-файл для последнего)
3) заархивировать папку! и сдать архив

Все другие варианты сдачи приму только один раз, потом буду ставить НЕ СДАНО
"""

s1 = 'разработка'
s2 = 'сокет'
s3 = 'декоратор'
print(type(s1))  # тип строка. s2 s3 аналогично

# c помощью онлайн конвертера
s1_1 = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
print(s1_1, type(s1_1))
s2_1 = '\u0441\u043e\u043a\u0435\u0442'
print(s2_1, type(s2_1))
s3_1 = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
print(s3_1, type(s3_1))

# с помощью цикла и функции
byte_s1 = bytes(s1, 'unicode_escape')  # переводим строку в байты
# print(byte_s1)
split_s1 = byte_s1.split(b'\\')
s = ''
for i, v in enumerate(split_s1):  # собираем байты в строку
    s += v.decode() + '\\'
s = s[:-1]
print('s == s1:', s == s1)
print('s:', s, type(s))

# с помощью ord и hex
lst_symbol = []
letter = 'разработка'  # ВОТ СЮДА ПОДСТАВЛЯЕМ НУЖНОЕ СЛОВО
for i in letter:
    _ord = ord(i)
    _hex = hex(_ord)
    lst_symbol.append(_hex.replace('x', ''))
# print(lst_symbol)
lst_unicode = []
for i in lst_symbol:
    if len(i) < 4:
        i = '\u005c' + 'u' + i
        lst_unicode.append(i)
    else:
        i = '\u005c' + 'u' + i
        lst_unicode.append(i)

print('lst_unicode:', lst_unicode)
s_unicode = ''.join(lst_unicode)
print('s_unicode:', s_unicode)
print('repr s_unicode:', repr(s_unicode))
# print('s_unicode type:', type(s_unicode))
# # ПРОВЕРКА https://unicode-table.com/ru/tools/decoder/

print(s_unicode is s1)
print(s_unicode == s1)
