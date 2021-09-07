import socket
import json

from chat.common.utils import send_msg, console_reader, recv_msg, create_presence, process_ans


def main():
    server_address, server_port = console_reader()

    # Cоздаем сокет-клиент
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_address, server_port))
    # создаем сообщение, что мы онлайн
    msg_to_server = create_presence()
    send_msg(sock, msg_to_server)
    try:
        # парсим ответ сервера, возвращая 200 или 400
        answer = process_ans(recv_msg(sock))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
