import json
from pythonAtestation.model.fun_model import *
from pythonAtestation.config import *
from datetime import datetime, timedelta, date

# Команды
def teams():
    print('Выберите одну из следующих команд:')
    print('создать и сохранить')
    print('все заметки')
    print('выбрать заметку')
    print('выбор по дате')
    print('добавить')
    print('редактировать')
    print('удалить')
    team = input('Введите команду ')
    return team

# Название заметки
def getTitle():
    title = input('Введите название заметки ')
    return title

# Текущее время
def getDate():
    dat = datetime.now()
    return str(dat)

# Текст заметки
def getBody():
    body = input('Введите текст заметки ')
    return body

# Вывод на экран
def output_screen():
    with open(path + '/pythonAtestation/data_file.json', 'r', encoding='utf-8') as json_data:
        data = json.load(json_data)
    for i in data["notes"]:
        print(i)
    print('Операция прошла успешно')

