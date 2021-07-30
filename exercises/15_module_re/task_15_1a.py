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
import re
def get_ip_from_cfg(file):
    spisok = []
    with open(file) as f:
        asl = f.read()
        spisok = re.split(r'[!\n]+', asl)
        yet = ('interface', ' ip address')
        spisok_1 = [i for i in spisok if i.startswith(yet)]
        #spisok_1 = ' '.join(spisok_1    )
        #regular = (r'(interface \S+).*(ip address (\S+) (\S+))')
        slovar = {}
        aaa = len(spisok_1)
        print(aaa)
        for i in range(10):
            i = 0
            slovar[spisok_1[i]] = spisok_1[i+1]
            i += 2
        print(slovar)



    #regular = (r'(interface \S+)'r'(ip address \S+ \S+)')
    #with open(file) as f:
     #   match = re.findall(regular, f.read(), re.DOTALL)
        #match = {i.group(1): i.group(2) for i in re.finditer(regular, f.read(), re.DOTALL)}
#    print(match)


get_ip_from_cfg('config_r1.txt')
