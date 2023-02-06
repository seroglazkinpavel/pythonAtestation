import json
from datetime import datetime, timedelta, date
from pythonAtestation.model.fun_model import *
from pythonAtestation.config import *
from pythonAtestation.view.command_interface import *

def get_value():
    my_bool = True
    while my_bool:
        team = teams()
        my_dict = {}
        data_notes = {'notes': [my_dict]}
        #dat = datetime.now()
        if (team == 'создать и сохранить'):
            my_dict['title'] = getTitle()
            my_dict['body'] = getBody()
            my_dict['date'] = getDate()
            if (my_dict['title'] == '' or my_dict['body'] == ''):
                print('Нет указанных данных')
                break
            create_file_json(data_notes)
            output_screen()
            break
        if (team == 'добавить'):
            my_dict['title'] = getTitle()
            my_dict['body'] = getBody()
            my_dict['date'] = getDate()
            if (my_dict['title'] == '' or my_dict['body'] == ''):
                print('Нет указанных данных')
                break
            else:
                add(my_dict)
            output_screen()
            break
        if (team == 'все заметки'):
            with open(path + "/pythonAtestation/data_file.json", encoding="UTF-8") as file_in:
                records = json.load(file_in)
                db_sorted = sorted(records["notes"], key=lambda row: row['date'])
                for item in db_sorted:
                    print(item)
            break
        if (team == 'выбор по дате'):
            date = input('Введите дату формата: Y-m-d ')  # ("%Y-%m-%d %H:%M:%S")
            if (date == ''):
                print('Не ввели дату.')
                break
            my_choice = choice(date)
            if (my_choice == [] or my_choice == None):
                print('Заметок на такую дату нет.')
            else:
                print(my_choice)
            break
        if (team == 'выбрать заметку'):
            title = input('Введите название заметки ')
            if (title == ''):
                print('Не ввели заметку.')
                break
            my_choice = choice(title)
            if (my_choice == []):
                print('Таких заметок нет.')
            else:
                print(my_choice)
            break
        if (team == 'удалить'):
            title = input('Введите название заметки для удаления ')
            if (title == ''):
                print('Не ввели название заметки для удаления')
                break
            deleteprod(title)
            output_screen()
            break
        if (team == 'редактировать'):
            title = input('Введите название заметки ')
            if (title == ''):
                print('Не ввели название заметки')
                break
            with open(path + '/pythonAtestation/data_file.json', 'r', encoding='utf-8') as json_data:
                data = json.load(json_data)
            for i in data["notes"]:
                if i["title"] == title:
                    i['date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    new_title = input('Измените название заметки ')
                    if (new_title != ''):
                        i['title'] = new_title
                    else:
                        i['title'] = i['title']
                    new_body = input('Измените текст заметки ')
                    if (new_body != ''):
                        i['body'] = new_body
                    else:
                        i['body'] = i['body']
            with open(path + '/pythonAtestation/data_file.json', 'w', encoding='utf-8') as outfile:
                json.dump(data, outfile, ensure_ascii=False, indent=2)
            for i in data["notes"]:
                print(i)
            print('Операция прошла успешно')
            break
        else:
            print('Не правильно набрана команда. Повторите.')



get_value()