# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess
def ping_ip_addresses(adress):
    for i in adress:
        ok_1 = []
        not_01 = []
        reply = subprocess.run(['ping', '-c', '3', '-n', i], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
        if reply.returncode == 0:
            ok_1.append(i)
        else:
            not_01.append(i)
    kort = (ok_1, not_01)

    return kort
