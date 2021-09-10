"""Константы"""

import logging

# Порт по умолчанию для сетевого ваимодействия
DEFAULT_PORT = 15000
# IP адрес по умолчанию для подключения клиента
DEFAULT_ADDRESS = ''
# Максимальная очередь подключений
MAX_CONNECTIONS = 5
# Максимальная длинна сообщения в байтах
MAX_PACKAGE_LENGTH = 1024
# Кодировка проекта
ENCODING = 'utf-8'

# Прококол JIM основные ключи:
ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'

# Прочие ключи, используемые в протоколе
PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'

# Уровень логирирования
LOGGING_LEVEL = logging.DEBUG
