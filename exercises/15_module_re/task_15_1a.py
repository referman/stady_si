# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом,
чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""

#Моя сложная версия
"""
import re
def get_ip_from_cfg(file):
    spisok = []
    with open(file) as f:
        asl = f.read()
        spisok = re.split(r'[!\n]+', asl)
        yet = ('interface', ' ip address')
        spisok_1 = [i for i in spisok if i.startswith(yet)]
        spisok_1 = ' '.join(spisok_1)
        regular = (r'(interface \S+\s+ip address (\S+) (\S+))')
        spisok_2 = re.finditer(regular, spisok_1)
        spisok_3 = []
        for i in spisok_2:
            spisok_3.append(i.group())
        spisok_3 = ''.join(spisok_1)
        regular_2 = r'((interface) (\S+)\s+(ip address \S+ \S+))'
        spisok_4 = [i.group(1) for i in re.finditer(regular_2, spisok_3)]
        spisok_4 = ' '.join(spisok_4)
        print(spisok_4)
        regular_3 = (r'ip address (\S+) (\S+)')
        regular_4 = r'(interface) (\S+)\s+(ip address \S+ \S+)'
        spisok_5 = [b.group(2) for b in re.finditer(regular_4, spisok_4)]
        spisok_6 = [i.groups() for i in re.finditer(regular_3, spisok_4)]
        slovar = dict(zip(spisok_5, spisok_6))
        return slovar
"""

import re
def get_ip_from_cfg(config):
    with open(config) as f:
        regex = re.compile(
            r"interface (?P<intf>\S+)\n"
            r"( .*\n)*"
            r" ip address (?P<ip>\S+) (?P<mask>\S+)"
        )
        match = regex.finditer(f.read())

    result = {m.group("intf"): m.group("ip", "mask") for m in match}
    return print(result)

get_ip_from_cfg('config_r1.txt')

