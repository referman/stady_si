# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

result = []
with open('config_sw1.txt') as f:
    for i in f:
        result.append(i.strip('\n').split(' '))
for i in result:
    if set(i) & set(ignore):
        continue
    elif i[0] == '!':
        continue
    else:
        print(' '.join(i))



'''
result = []
with open('config_sw1.txt') as f:
    for i in f:
        if i[0] != '!':
            result.append(i.strip('\n'))

result2 = []
for i in result:
    i = i.split(' ')
    result2.append(i)
for i in result2:
    try:
        if (i[0] not in ignore) and (i[1] not in ignore):
            print(' '.join(i))
    except:
        pass
print('end')
'''

#Можно было решить этот пример с использованием set() но я уже так делать не стал