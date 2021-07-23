# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ignore = ["duplex", "alias", "configuration"]


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


