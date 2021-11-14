"""Ф-я host_ping  пингует список адресов"""
import pprint
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


def host_ping(ip_addr, is_str: bool = False):
    command = ['ping', ' -c', ' 4']
    if not is_str:
        get_ips = get_domains_ips(ip_addr)
    else:
        get_ips = ip_addr
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
        # достаем ip
        ip = data[i][0].split(' ')[1]
        # определяем: пингуется или нет
        received = data[i][0].split(',')
        if 'received' in received[-4] or 'received' in received[-3]:
            received = received[1].split()[0]
            if int(received) > 0:
                try:
                    print(f'«Узел {ip} | {socket.gethostbyaddr(ip)[0]} доступен»')
                except socket.herror:
                    print(f'«Узел {ip} доступен»')
            else:
                try:
                    print(f'«Узел {ip} | {socket.gethostbyaddr(ip)[0]} недоступен»')
                except socket.herror:
                    print(f'«Узел {ip} недоступен»')


range_ip = ['192.168.0.0', '192.168.0.3']


def host_range_ping(ip_list):
    """Известные проблемы: игнорирует первый адрес, переходя сразу к следующему"""
    range_ip_address = []

    # делаем адреса объектами ф-ии ip_address
    for ip in ip_list:
        range_ip_address.append(ipaddress.ip_address(ip))

    # создаем список от первого адреса до последнего
    range_str_ip = []
    ip1 = range_ip_address[0]
    ip2 = range_ip_address[1]

    while len(range_str_ip) < int(str(range_ip_address[-1]).split('.')[-1]):
        if ip2 > ip1:
            ip1 += 1
            range_str_ip.append(str(ip1))

    host_ping(range_str_ip, is_str=True)


if __name__ == '__main__':
    host_ping(domains)
    host_range_ping(ip_list=range_ip)
