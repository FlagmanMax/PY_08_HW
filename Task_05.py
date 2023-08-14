# Задание №5
# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.
import os
import pickle
import json


def proc_pickle():
    for file in os.listdir():
        # source_name = file.split(".")[0]
        # source_ext = file.split(".")[1]
        if file.endswith('.json'):
            with (
                open(file, 'r') as f_read,
                open(f'{file[:-5]}.pickle', 'wb') as f_write
                ):
                data = json.load(f_read)
                pickle.dump(data,f_write)

proc_pickle()