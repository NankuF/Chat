#  Задание на закрепление знаний по модулю yaml.

# Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. Для этого:
# Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список,
# второму — целое число, третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом,
# отсутствующим в кодировке ASCII (например, €);
# Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
# При этом обеспечить стилизацию файла с помощью параметра default_flow_style,
# а также установить возможность работы с юникодом: allow_unicode = True;
# Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.

import chardet
import yaml

# Переводим файл в кодировку utf-8
# with open('yaml_examples.yaml','rb') as f:
#     file = f.read()
#     x = chardet.detect(file)
#     # print(x)
#     y = file.decode(x['encoding']).encode('utf-8')
#     y= y.decode('utf-8')
# with open('yaml_examples.yaml','w') as f1:
#     f1.write(y)

data1 = {
    1: ['a', 'b', 'c'],
    2: 10,
    3: {
        1: '\u2564',
        2: '\u7654'
    }

}


def write_yaml(dct: {}):
    with open('file.yaml', 'w') as f:
        yaml.dump(dct, f, default_flow_style=True, allow_unicode=True)

    with open('file.yaml', 'r') as f:
        z = yaml.load(f)
        print(z)


if __name__ == '__main__':
    write_yaml(data1)
