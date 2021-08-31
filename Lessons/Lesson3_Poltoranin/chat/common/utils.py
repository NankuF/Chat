import json
from socket import socket
import sys

from common.variables import DEFAULT_PORT, DEFAULT_ADDRESS, ENCODING, MAX_PACKAGE_LENGTH


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

    return return_port_and_address()


def send_msg(socket: socket, msq: dict) -> None:
    """
    Отправляет сообщение, кодирует в байты
    """
    json_msg = json.dumps(msq)  # приводим dict к str, чтобы затем ее закодировать
    encode_msg = json_msg.encode(ENCODING)
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
