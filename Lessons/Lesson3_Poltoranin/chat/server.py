import json
import socket
from common.utils import send_msg, recv_msg, console_reader


def main():
    """
    Cоздаём сокет-сервер
    Константа AF_INET соответствует Internet-домену. Сокеты, размещённые в этом домене,
    могут использоваться для работы в любой IP-сети. AF - address family

    Тип сокета определяет способ передачи данных по сети:
    SOCK_STREAM. Передача потока данных с предварительной установкой соединения. == TCP
    SOCK_DGRAM. Передача данных в виде отдельных сообщений (датаграмм). == UDP
    SOCK_RAW. Этот тип присваивается низкоуровневым (т. н. "сырым") сокетам.
    Их отличие от обычных сокетов состоит в том, что с их помощью программа может взять на себя
    формирование некоторых заголовков, добавляемых к сообщению.
    """

    listen_address, listen_port = console_reader()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((listen_address, listen_port))
    sock.listen(2)

    while True:
        client, client_address = sock.accept()
        try:
            # отправляем клиенту сообщение
            send_msg(client, {'server_msg': 'You connect!'})
            # получаем от клиента сообщение
            msg_to_client = recv_msg(client)
            print(msg_to_client)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('Принято некорретное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    main()