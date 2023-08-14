# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

import csv
import json

def func_csv():

    with (
        open('Task_02.json', 'r') as f_json,
        open('Task_02.csv', 'w', encoding='utf-8', newline='') as f_csv
    ):
        try:
            data = json.load(f_json)
        except:
            data = {}
        # data = json.load(f_json)

        writer = csv.writer(f_csv, delimiter=';')

        columns = ['level', 'pers_id', 'name']
        writer.writerow(columns)

        result = []
        for key, value in data.items():
            for i in data[key]:
                result.append([key, i, data[key][i]])
        writer.writerows(result)
        # csv.writer(data, f_csv, dialect='excel')

    print('Ok!')

func_csv()