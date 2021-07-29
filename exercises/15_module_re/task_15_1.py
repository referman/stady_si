# -*- coding: utf-8 -*-
"""
Задание 15.1

Создать функцию get_ip_from_cfg, которая ожидает как аргумент имя файла,
в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать IP-адреса и маски,
которые настроены на интерфейсах, в виде списка кортежей:
* первый элемент кортежа - IP-адрес
* второй элемент кортежа - маска

Например (взяты произвольные адреса):
[('10.0.1.1', '255.255.255.0'), ('10.0.2.1', '255.255.255.0')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.


Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""
import re
def get_ip_from_cfg(file):
    regular = (r'ip address (\S+) (\S+)')
    with open(file) as f:
        spisok = [i.groups() for i in re.finditer(regular, f.read())]

    return spisok



#Мой вариант:
'''
def get_ip_from_cfg(file):
    ip_adress = (r'ip address')
    regular = (r'(\d+\.\d+\.\d+\.\d+) +(\d+\.\d+\.\d+\.\d+)')
    spisok = []
    with open(file) as f:
        for i in f:
            if ip_adress in i:
                match = re.findall(regular, i)
                if match:
                    spisok += tuple(match)
    return print(spisok)

get_ip_from_cfg('config_r1.txt')
'''