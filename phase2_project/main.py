import json
import datetime
import sys
from json import JSONDecodeError

try:
    db = json.loads(open('db.json').read())
    print(db)
except JSONDecodeError:
    print('Database not found, try restore from backup...')
    try:
        db_backup = json.load(open('db_backup.json'))
        db = db_backup
    except FileNotFoundError:
        print('backup file not found, create new db...')
        db = {'task_database': {}}

"""
db stucture
{
    "task_database": {
            "user": str {
                task_id: str {
                        descr: strint
                        complete: bool
                        date: datetime
                        }
                    }
            }
"""

def create_task(user: str):
    task_id = int(max(db['task_database'][user].keys())) + 1
    descr = input('Введите текст задачи')
    db['task_database'][user][task_id] = {
                         'descr': descr,
                         'complete': False,
                         'date': str(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'))
                         }

def read_task(user: str):
    for user_tasks in db['task_database'][user].keys():
        print(db['task_database'][user][user_tasks])

def delete_task(user: str):
    task_id = input('Введите номер задачи\n')
    del db['task_database'][user][task_id]

def update_task(user: str):
    task_id = input('Введите номер задачи\n')
    descr = input('Введите новый текст задачи\n')
    db['task_database'][user][task_id]['descr'] = descr

def complete_task(user: str):
    task_id = input('Введите номер задачи\n')
    db['task_database'][user][task_id]['complete'] = True

def main():
    try:
        user = input('Введите имя пользователя\n')
    except KeyboardInterrupt:
        print('Что-то пошло не так')
        sys.exit(0)

    if db['task_database'].get(user) is None:
        db['task_database'][user] = {0:
                        {
                         'descr': 'Задача для примера',
                         'complete': False,
                         'date': str(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'))
                         }
                    }
    create_task(user)
    read_task(user)
    delete_task(user)
    update_task(user)
    complete_task(user)

if __name__ == '__main__':
    main()
    json.dump(db, open('db.json', 'w'), indent=2)