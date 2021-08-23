"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import chardet
import subprocess
import os


def ping_custom(*args):
    def codes(code='utf-8'):
        command = [*args]
        ping = subprocess.Popen(command, stdout=subprocess.PIPE)
        for line in ping.stdout:
            dct_coding = chardet.detect(line)
            # print(dct_coding)
            line = line.decode(dct_coding['encoding']).encode(code)
            print(line.decode('utf-8'))

    os_name = os.name
    if os_name == 'posix':
        code = 'utf-8'
        codes(code)
    elif os_name == 'nt':
        code = 'cp1251'
        codes(code)
    elif os_name == 'mac':
        pass
        # code = 'utf-8'  # ???????????????????????????????
        # codes(code)


ping_custom('ping', '-c4', 'yandex.ru')
