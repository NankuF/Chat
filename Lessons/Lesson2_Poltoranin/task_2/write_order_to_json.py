# Задание на закрепление знаний по модулю json.
#
# Есть файл orders в формате JSON с информацией о заказах.
# Написать скрипт, автоматизирующий его заполнение данными. Для этого:
# Создать функцию write_order_to_json(), в которую передается 5 параметров
# — товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date).
# Функция должна предусматривать запись данных в виде словаря в файл orders.json.
# При записи данных указать величину отступа в 4 пробельных символа;
# Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.

import datetime
import json

item = 'Пипл'
quantity = 0
price = 345
buyer = 'Штат'
date = str(datetime.datetime.now())


def write_order_to_json(item, quantity, price, buyer, date):
    """
    Функция принимает на вход 5 переменных и собирает их в словарь.
    После этого получает список json, читает его и Переписывает файл json(сохраняя все данные),
    добавляя в конец текущий словарь.
    """

    dct = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date

    }
    # Читаем json. Изначально там находится {"orders":[]}.
    # Получаем его как dict, и вставляем по ключу наш сформированный dict.
    with open('orders.json', 'r', encoding='utf-8') as f:
        take_dct = json.load(f)
        take_dct['orders'].append(dct)

    # Полностью переписываем файл с добавленным словарем, сохраняя структуру и данные в исходном json.
    with open('orders.json', 'w', encoding='utf-8') as f_n:
        take_dct = json.dumps(take_dct, indent=4)
        f_n.write(take_dct)


if __name__ == '__main__':
    write_order_to_json(item, quantity, price, buyer, date)
