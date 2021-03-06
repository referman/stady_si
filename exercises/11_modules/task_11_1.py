# -*- coding: utf-8 -*-
"""
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент
вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое
файла в строку, а затем передать строку как аргумент функции (как передать вывод
команды показано в коде ниже).

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

В словаре интерфейсы должны быть записаны без пробела между типом и именем.
То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt. При этом функция должна
работать и на других файлах (тест проверяет работу функции на выводе
из sh_cdp_n_sw1.txt и sh_cdp_n_r3.txt).

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def parse_cdp_neighbors(command_output):
    """
    Тут мы передаем вывод команды одной строкой потому что именно в таком виде будет
    получен вывод команды с оборудования. Принимая как аргумент вывод команды,
    вместо имени файла, мы делаем функцию более универсальной: она может работать
    и с файлами и с выводом с оборудования.
    Плюс учимся работать с таким выводом.
    """
    chois = ('R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'SW1', 'SW2', 'Eth', '0/', 'Fa')
    text_1 = [i for i in command_output.split() if i.startswith(chois)]
    text_2 = text_1[0].split('>')
    text_2 = text_2[0]
    text_1 = text_1[1:]
    def func(lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i + n]
    text_3 = list(func(text_1, 5))
    text_4 = {}
    for i in text_3:
        num_1, num_2, num_3, num_4, num_5 = i
        text_4[(text_2,num_2+num_3)] = (num_1, num_4+num_5)
    
    return text_4

if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_cdp_neighbors(f.read()))

#Вармант №2 с подключением модуля, убирающего ковычки
"""
from ast import literal_eval

def parse_cdp_neighbors(command_output):
    chois = ('R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'SW1', 'SW2', 'Eth', '0/', 'Fa')
    text_1 = [i for i in command_output.split() if i.startswith(chois)]
    text_2 = text_1[0].split('>')
    text_2 = text_2[0]
    text_1 = text_1[1:]
    def func(lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i + n]
    text_3 = list(func(text_1, 5))
    text_4 = {}
    for i in text_3:
        text_4[f"('{text_2}', '{''.join(i[1:3])}')"] = f"('{i[0]}', '{''.join(i[3:5])}')"
    text_5 = {literal_eval(k): literal_eval(v) for k,v in text_4.items()}
    return text_5
"""

