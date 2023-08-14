# Задание №6
# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

import csv
import pickle


def csv_converter(file):
    with (
        open(file, 'rb') as f_read,
        open(f'{file[:-7]}.csv', 'w') as f_write
        ):
        data = pickle.load(f_read)

        head = data.keys()
        writer = csv.writer(f_write,delimiter=";")
        writer.writerow(head)


        for line, values in data.items():
            a, b = tuple(*values.values())
            writer.writerow([*values.keys(), a, b])

csv_converter('Task_04.pickle')

