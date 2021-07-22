# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_adress = input("Введите IP-адрес в формате 10.0.1.1: ")
ip_adress_spl = ip_adress.split('.')

if int(ip_adress_spl[0]) >= 1 and int(ip_adress_spl[0]) <=223:
   print('unicast')
elif int(ip_adress_spl[0]) >= 224 and int(ip_adress_spl[0]) <=239:
   print('multicast')
elif ip_adress == '255.255.255.255':
   print('local broadcast')
elif ip_adress == '0.0.0.0':
   print('unassigned')
else:
   print('unused')

