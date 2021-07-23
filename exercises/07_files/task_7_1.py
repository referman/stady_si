# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
result = []
with open('ospf.txt') as f:
    for i in f:
        i = i.split()
        result.append({'Prefix': i[1], 'AD/Metric': i[2].strip('[]'), 'Next-Hop': i[4].strip(','), 'Last update': i[5].strip(','), 'Outbound Interface': i[6]})

for i in result:
    for a, b in i.items():
        print('{:25}{}'.format(a, b))
