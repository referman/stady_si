# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
while True:
    ip_adress = input("Введите IP-адрес в формате 10.0.1.1: ")
    try:
        ip_chek = ''
        for i in ip_adress:
            if i.isdigit():
                ip_chek += i
            elif i == '.':
                ip_chek += i
            else:
                raise ValueError
        ip_adress_spl = ip_chek.split('.')
        ip_adress_spl = [int(i) for i in ip_adress_spl]
        ip_adress_spl_len = len(ip_adress_spl)
        if ip_adress_spl_len <= 3 or ip_adress_spl_len > 4:
            raise ValueError
        for i in ip_adress_spl:
            if i >= 256 or i <= -1:
                raise ValueError
        if ip_adress_spl[0] in range(1, 224):
            print('unicast')
        elif ip_adress_spl[0] in range(224, 240):
            print('multicast')
        elif ip_adress == '255.255.255.255':
            print('local broadcast')
        elif ip_adress == '0.0.0.0':
            print('unassigned')
        else:
            print('unused')
    except ValueError:
        print('Неправильный IP-адрес')
    else:
        break