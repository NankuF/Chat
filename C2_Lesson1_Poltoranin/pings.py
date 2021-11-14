"""Ф-я host_ping  пингует список адресов"""

import subprocess
import ipaddress
import socket


domains = ['8.8.8.8', '10.10.10.10', 'yandex.ru']


def get_domains_ips(list_ips: list) -> list:
    domains_ips = []
    for domain in domains:
        if domain.isascii():
            domains_ips.append(socket.gethostbyname(domain))
        else:
            domains_ips.append(domain)
    ipv4_address_list = [str(ipaddress.ip_address(address)) for address in domains_ips]
    return ipv4_address_list


def host_ping(ip_addr):
    command = ['ping', ' -c', ' 4']
    get_ips = get_domains_ips(ip_addr)
    result = []
    for address in get_ips:
        command = ''.join(command)
        addr = ''.join(address)
        result.append(f'{command} {addr}')

    data = []
    n = 1
    for r in result:
        print(f'Ping_{n}_address')
        n += 1
        process = subprocess.Popen(r.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
        data.append(process.communicate())

    # print(data)
    for i in range(len(data)):
        ip = data[i][0].split(' ')[1]
        recieved = data[i][0].split(',')[-3].split(' ')[1]
        if int(recieved) > 0:
            try:
                print(f'«Узел {ip} | {socket.gethostbyaddr(ip)[0]} доступен»')
            except socket.herror:
                print(f'«Узел {ip} доступен»')
        else:
            try:
                print(f'«Узел {ip} | {socket.gethostbyaddr(ip)[0]} недоступен»')
            except socket.herror:
                print(f'«Узел {ip} недоступен»')


if __name__ == '__main__':
    host_ping(domains)
