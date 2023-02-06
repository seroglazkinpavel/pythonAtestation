import json
from pythonAtestation.config import *

# Выбор
def choice(arg):
    with open(path + "/pythonAtestation/data_file.json", encoding="UTF-8") as file_in:
        records = json.load(file_in)
        records_notes = records['notes']
    filtered_records = filter_set(records_notes, arg)
    return list(filtered_records)

# Создание и сохранения файла
def create_file_json(my_dict):
    with open(path + "/pythonAtestation/data_file.json", "w", encoding = 'utf8') as write_file:
        json.dump(my_dict, write_file, ensure_ascii = False, indent = 2)


# Добавление заметки
def add(let):
    with open(path + "/pythonAtestation/data_file.json", encoding = "utf8") as f:
        data = json.load(f)
        data['notes'].append(let)
    with open(path + "/pythonAtestation/data_file.json", 'w', encoding = "utf8") as outfile:
        json.dump(data, outfile, ensure_ascii = False, indent = 2)

# Выбор по дате
def filter_set(records_notes, date):
    def iterator_func(x):
        for v in x.values():
            if date in v:
                return True
        return False
    return filter(iterator_func, records_notes)

# Удаление заметки
def deleteprod(title):
    with open(path + "/pythonAtestation/data_file.json", 'r', encoding='utf-8') as json_data:
        data = json.load(json_data)

    for i in data["notes"]:
        if i["title"] == title:
            data["notes"].remove(i)

    with open(path + "/pythonAtestation/data_file.json", 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii = False, indent=2)