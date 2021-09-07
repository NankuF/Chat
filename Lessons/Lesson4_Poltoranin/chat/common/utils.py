import json
from socket import socket
import sys
import time

from .variables import DEFAULT_PORT, DEFAULT_ADDRESS, ENCODING, MAX_PACKAGE_LENGTH, ACTION, USER, RESPONSE, PRESENCE, \
    ACCOUNT_NAME, TIME, ERROR


def create_presence(account_name='Guest'):
    """
    Функция генерирует ответ о присутствии клиента
    """
    # {'action': 'presence', 'time': 1573760672.167031, 'user': {'account_name': 'Guest'}}
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return out


def process_ans(message):
    """
    Функция разбирает ответ сервера и возвращает 200 либо 400
    """
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError


def process_client_message(message):
    '''
    Обработчик сообщений от клиентов, принимает словарь -
    сообщение от клинта, проверяет корректность,
    возвращает словарь-ответ для клиента
    '''
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


def console_reader() -> (int, int):
    """
    Определяет параметры командной строки, если их нет - задаёт дефолтные значения.
    Пример командной строки: server.py -p 15000 -a 0.0.0.0
    """

    def return_port_and_address():

        if 'server.py' in sys.argv and 'client.py' in sys.argv:
            raise ValueError(print('В функции должен быть только один параметр'))

        else:
            if 'server.py' in sys.argv:  # server.py -p 15000 -a 0.0.0.0
                try:
                    if '-p' in sys.argv:
                        take_port = sys.argv.index('-p') + 1
                        port = int(sys.argv[take_port])
                        if port < 1024 or port > 65535:
                            raise ValueError
                    else:
                        port = DEFAULT_PORT
                    if '-a' in sys.argv:
                        take_address = sys.argv.index('-a') + 1
                        address = sys.argv[take_address]
                    else:
                        address = DEFAULT_ADDRESS
                    return address, port
                except IndexError:
                    print('После параметра -\'p\' необходимо указать номер порта.')
                    print('В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
                    sys.exit(1)

            if 'client.py' in sys.argv:  # client.py 192.168.1.2 8079
                try:
                    address = sys.argv[1]
                    port = int(sys.argv[2])
                    if port < 1024 or port > 65535:
                        raise ValueError
                except IndexError:
                    address = DEFAULT_ADDRESS
                    port = DEFAULT_PORT
                except ValueError:
                    print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
                    sys.exit(1)
                return address, port

        if ('client.py' or 'server.py') not in sys.argv:
            address = DEFAULT_ADDRESS
            port = DEFAULT_PORT
            return address, port

    return return_port_and_address()


def send_msg(socket: socket, msq: dict) -> None:
    """
    Отправляет сообщение, кодирует в байты
    """
    if isinstance(msq, dict):
        json_msg = json.dumps(msq)  # приводим dict к str, чтобы затем ее закодировать
        encode_msg = json_msg.encode(ENCODING)
    else:
        raise TypeError

    if isinstance(encode_msg, bytes):
        socket.send(encode_msg)


def recv_msg(socket: socket) -> dict:
    """
    Принимает сообщение, декодирует в dict
    """
    encoded_response = socket.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError

# b = b'"hello"'
# j_dec = b.decode('utf-8')
# j_dec = json.loads(j_dec)
# # print(j_dec, type(j_dec))
#
# lst = [0, '-p',2]
# print(lst.index('-p')+1)
