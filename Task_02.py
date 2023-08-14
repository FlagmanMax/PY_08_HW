# Задание №2
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.

import json

def func():
    while True:
        try:
            name, pers_id, level = input("Введите данные: Имя id уровень: ").split()
        except ValueError:
            break
        level = int(level)

        if not 0<level<8:
            print('Ошибка ввода!')
            continue

        with open('Task_02.json', 'r') as f:
            try:
                data = json.load(f)
            except:
                data = {}

            for user in data.values():
                if pers_id in user.keys():
                    print("id уже используется!")
                    continue

        with open('Task_02.json', 'w') as f:
            if level not in data:
                data[level] = {}
            data[level][pers_id] = name

            json.dump(data, f, ensure_ascii=False, indent=2)
