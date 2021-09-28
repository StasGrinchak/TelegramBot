import os

from periodical.celery import app

from main import morning,evening
@app.task
def add(x, y):
    print("Функция работает только Утром с 9 до 17")
    morning()
    return x + y

@app.task
def test(x, y):
    print("Функция работает только вечером с 17 до 19")
    evening()
    return x + y



# app.conf.beat_schedule = {
#     'add-every-20-seconds': {
#         'task': 'periodical.tasks.add',
#         'schedule':crontab (minute='*/10',hour='9,17', day_of_week='mon,tue,wed,thu,fri'),
#         'args': (16, 16)
#     },
#     'add-every-10-seconds': {
#         'task': 'periodical.tasks.test',
#         'schedule': crontab (minute='*/10',hour='18,19', day_of_week='mon,tue,wed,thu,fri'),
#         'args': (16, 16)
#     },
# }
