import json
import socket
import time

from common.variables import ENCODING, ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME
from common.utils import send_msg, recv_msg, console_reader


def main():
    def create_presence(account_name='Guest'):
        '''
        Функция генерирует запрос о присутствии клиента
        :param account_name:
        :return:
        '''
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
        '''
        Функция разбирает ответ сервера
        :param message:
        :return:
        '''
        if RESPONSE in message:
            if message[RESPONSE] == 200:
                return '200 : OK'
            return f'400 : {message[ERROR]}'
        raise ValueError



    server_address, server_port = console_reader()

    # Cоздаем сокет-клиент
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_address, server_port))
    msg_to_client = recv_msg(sock)
    print(msg_to_client)
    send_msg(sock, {'hello': 'its client!'})


if __name__ == '__main__':
    main()
