# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций
# пакет для работы с файлами разных форматов.

import os
import sys
from pprint import pprint
import json
import csv
import pickle

def writer_all(current_path:str, source: dict[str,dict], json_file=False, csv_file=False, pickle_file=False):
    name = os.path.join(current_path, "Hw_01")

    if json_file:
        with open(name+'.json', 'w', encoding='utf-8') as json_data:
            json.dump(source, json_data, indent=4, ensure_ascii=False)

    if pickle_file:
        with open(name+'.pickle', 'wb', ) as pickle_data:
            pickle.dump(source, pickle_data)

    if csv_file:
        with open(name+'.csv', 'w', encoding='utf-8') as csv_data:
            file = [['Full_path', 'Name', 'Parent_dir', 'Type', 'Size']]
            for key, item in source.items():
                file.append([key, *item.values()])
            csv.writer(csv_data, dialect='excel', delimiter=';').writerows(file)



def json_writer(current_path:str, source: dict[str,dict]):
    name = os.path.join(current_path, "Hw_01.json")
    with open(name, 'w', encoding='utf-8') as data:
        json.dump(source, data, indent=4, ensure_ascii=False)

def csv_writer(current_path:str, source: dict[str, dict]):
    name = os.path.join(current_path, "Hw_01.csv")
    file = [['Full_path', 'Name', 'Parent_dir', 'Type', 'Size']]
    for key, item in source.items():
        file.append([key, *item.values()])
    with open (name, 'w', encoding='utf-8') as data:
        write_csv = csv.writer(data, dialect='excel', delimiter=';')
        write_csv.writerows(file)


def pickle_writer(current_path:str, source: dict[str, dict]):
    name = os.path.join(current_path, "Hw_01.pickle")
    with open(name, 'wb', ) as data:
        pickle.dump(source, data)

def size_of_dir(dir_path: str) -> int:
    total_size = 0;
    for path,_,files in os.walk(dir_path):
        for file in files:
            total_size += sys.getsizeof(os.path.join(path, file))
    return total_size

def process_directory(path_: str = os.getcwd()):
    result = {}
    for path, dir_list, file_list in os.walk(path_):
        for cur_dir in dir_list:
            result[os.path.join(path, cur_dir)] = {'name': cur_dir,
                                                'path': path,
                                                'type': 'DIR',
                                                'size': size_of_dir(os.path.join(path, cur_dir))}

        for cur_file in file_list:
            result[os.path.join(path,cur_file)] = {'name':cur_file,
                                               'path':path,
                                               'type':'FILE',
                                               'size':sys.getsizeof(os.path.join(path,cur_file))}

    writer_all(path_,result, json_file=True, csv_file = True)
    # json_writer(path_,result)
    # pickle_writer(path_, result)
    # csv_writer(path_, result)
    return result

res = process_directory("c:/Work/!GB/14 Python/08_Seminar/")
pprint(res)