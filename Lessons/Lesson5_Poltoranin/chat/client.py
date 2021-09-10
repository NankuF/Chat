import socket
import json

from chat.common.utils import send_msg, console_reader, recv_msg, create_presence, process_ans

import logging
import log.client_log_config

CLIENT_LOGGER = logging.getLogger('client')


def main():
    server_address, server_port = console_reader()
    CLIENT_LOGGER.debug(f'Установлено соединение с сервером: {server_address} {server_port}')

    # Cоздаем сокет-клиент
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_address, server_port))
    # создаем сообщение, что мы онлайн
    msg_to_server = create_presence()
    CLIENT_LOGGER.debug(f'Сообщение для сервера: {msg_to_server}')
    send_msg(sock, msg_to_server)
    try:
        # парсим ответ сервера, возвращая 200 или 400
        answer = process_ans(recv_msg(sock))
        CLIENT_LOGGER.info(f'Получаем ответ сервера: {answer}')
    except (ValueError, json.JSONDecodeError):
        CLIENT_LOGGER.error('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
