"""
Задание на закрепление знаний по модулю CSV.
Написать скрипт, осуществляющий выборку определенных данных
из файлов info_1.txt, info_2.txt, info_3.txt и
формирующий новый «отчетный» файл в формате CSV.
Для этого:
    Создать функцию get_data(),
    в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
    В этой функции из считанных данных необходимо с помощью регулярных выражений
    извлечь значения параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
    Значения каждого параметра поместить в соответствующий список.
    Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
    В этой же функции создать главный список для хранения данных отчета — например:
    main_data — и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС»,
    «Код продукта», «Тип системы».
    Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
    Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
    В этой функции реализовать получение данных через вызов функции get_data(),
    а также сохранение подготовленных данных в соответствующий CSV-файл;
    Проверить работу программы через вызов функции write_to_csv().

"""
import csv
from pprint import pprint

import chardet
import os
import re

# Подготавливаем полученный файл для работы в текущей системе. Декодируем в формат utf-8.
file = 'info_1.txt'
new_file = os.path.splitext(file)
new_file = f'{new_file[0]}_utf8{new_file[1]}'
# print(new_file)
with open(file, 'rb') as f:
    for line in f:
        dct_coding = chardet.detect(line)  # не совсем точно определяет кодировку. тем самым ломая символы
        # print(dct_coding)
        # убираем  ine.decode(dct_coding['encoding']) тк неточно определена кодировка модулем chardet
        line = line.decode('cp1251').encode('utf-8')
        line = line.decode('utf-8')
        with open(new_file, 'a') as nf:
            nf.write(line)

file = 'info_1_utf8.txt'

#
# def get_data(files_utf8: [str], re_pattern: []) -> {}:
#     result = []
#     main_data = []
#     count = 1
#     while count <= len(re_pattern):
#         with open(file) as f:
#             pattern = re_pattern.pop()
#             for line in f:
#                 head = re.search(pattern, line)  # object re.Match
#                 if head:
#                     # чтобы извлечь строку, а не re.match, применим метод group()
#                     # отделяем значения по :, удаляем пробелы слева и справа
#                     main_data.append(head.group().partition(':')[0].lstrip().rstrip())
#                     result.append(head.group().partition(':')[2].lstrip().rstrip())
#
#     # print(main_data)
#     # print(result)
#     dct = [dict(zip(main_data, result))]
#     # pprint(dct)
#     return dct
#
# files = []
# arg = [r'^Изготовитель системы*.*', r'^Название*.*', r'^Код продукта*.*', r'^Тип системы*.*']
# call_function = get_data(file_utf8=file, re_pattern=arg)
#
#
# def write_to_csv(data: [{}]) -> csv:
#     with open('kp_data_dictwriter.csv', 'w') as f_n:
#         F_N_WRITER = csv.DictWriter(f_n, fieldnames=list(data[0].keys()),
#                                     quoting=csv.QUOTE_NONNUMERIC)
#         F_N_WRITER.writeheader()
#         for d in data:
#             F_N_WRITER.writerow(d)
#
#     with open('kp_data_dictwriter.csv') as f_n:
#         print(f_n.read())
#
#
# write_to_csv(call_function)
