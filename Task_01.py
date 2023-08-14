# Задание №1
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json
import os

# def file_transform_to_json(filename):
#     with (
#         open(filename, 'r', encoding='utf-8',) as file_r,
#         open(f'Task_01_{filename}.json', 'w', encoding='utf-8') as file_w):
#         data = file_r.readlines()
#         list_to_save = []
#         for line in data:
#             key, value = line.strip().split(' ')
#             list_to_save.append((key.title(), value))
#         json.dump(list_to_save, file_w, ensure_ascii=False, indent = 2)
#         print(list_to_save)

def file_transform_to_json(filename):
    with (
        open(filename, 'r', encoding='utf-8',) as file_r,
        open(f'Task_01_{filename}_dict.json', 'w', encoding='utf-8') as file_w):
        data = file_r.readlines()
        dict_to_save = {}
        for line in data:
            key, value = line.strip().split(' ')
            if key.title() in dict_to_save.keys():
                dict_to_save[key.title()].append(value)
            else:
                dict_to_save[key.title()] = [value]
        json.dump(dict_to_save, file_w, ensure_ascii=False, indent = 2)
        print(dict_to_save)

filename = "Old_Task_03.txt"
file_transform_to_json(filename)
