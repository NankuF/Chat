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
import os
import csv
import re
import chardet

os.chdir(os.getcwd())

"""
NOTE:   Вопрос с chardet в функции decoding_in_utf_8 не решен,
        он не точно определяет кодировку, в результате теряем некоторые символы в кириллице.
"""


def decoding_in_utf_8(path: [str]) -> [str]:
    """
    Функция принимает список файлов/путей файлов в "любой" кодировке
    и возвращает список новых файлов в кодировке 'utf-8'
    """
    new_lst_files = []
    # cобираем названия для новых файлов с меткой _utf8
    for file in path:
        new_file = os.path.splitext(file)
        new_file = f'{new_file[0]}_utf8{new_file[1]}'
        new_lst_files.append(new_file)

    # открываем каждый файл и  перекодируем в utf-8 с записью в новый файл.
    # если перекодировать построчно, то chadret не всегда верно определяет кодировку.
    count = 0
    while count < len(new_lst_files):
        with open(path[count], 'rb') as f:
            data = f.read()
            codec = chardet.detect(data)
            file_in_utf_8 = data.decode(codec['encoding']).encode('utf-8').decode('utf-8')

        with open(new_lst_files[count],'w') as nf:
            nf.write(file_in_utf_8)
        count += 1
    return new_lst_files


def get_data(files_utf8: [str], re_pattern: [r'str']) -> [{}]:
    """
    Функция принимает список файлов и список регулярных выражений.
    Возвращает список словарей, cобранный по регулярным выражениям re_pattern.
    """
    lst_dicts = []
    for file in files_utf8:
        dct = {}
        for pattern in re_pattern:
            with open(file) as f:
                for line in f:
                    head = re.search(pattern, line)  # object re.Match
                    if head is None:
                        pass
                    elif head:
                        # чтобы извлечь строку, а не re.match, применим метод group()
                        # отделяем значения по :, удаляем пробелы слева и справа
                        main_data_head = head.group().partition(':')[0].lstrip().rstrip()
                        result_head = head.group().partition(':')[2].lstrip().rstrip()
                        dct[main_data_head] = result_head
        lst_dicts.append(dct)
    return lst_dicts


def write_to_csv(data: [{}]) -> csv:
    """
    Функция принимает список словарей и возвращает файл в формате .csv
    """
    with open('data_dictwriter.csv', 'w') as f_n:
        F_N_WRITER = csv.DictWriter(f_n, fieldnames=list(data[0].keys()),
                                    quoting=csv.QUOTE_NONNUMERIC)
        F_N_WRITER.writeheader()
        for d in data:
            F_N_WRITER.writerow(d)

    # with open('data_dictwriter.csv') as f_n:
    #     print(f_n.read())


def write_files_to_csv(file: [str], pattern: [r'str']):
    """
    Функция, которую нужно запустить в этом модуле, либо импортировать из модуля.
    Функция принимает список файлов и список регулярных выражений  и возвращает файл в формате .csv
    """
    write_to_csv(get_data(decoding_in_utf_8(file), pattern))


if __name__ == '__main__':
    this_dir = os.getcwd()
    os.chdir(this_dir + '/task_1')    # система глючит и не определяет что я нахожусь в /task_1
    path_files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    pattern = [r'^Изготовитель системы*.*', r'^Название*.*', r'^Код продукта*.*', r'^Тип системы*.*']
    write_files_to_csv(path_files, pattern)
