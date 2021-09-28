from celery import Celery
from celery.schedules import crontab


app = Celery('periodical',
             broker='redis://127.0.0.1:6379',
             include=['periodical.tasks'])


app.conf.beat_schedule = {
    'add-every-20-seconds': {
        'task': 'periodical.tasks.add',
        'schedule':crontab (minute='*/10',hour='9,17', day_of_week='mon,tue,wed,thu,fri'),
        'args': (16, 16)
    },
    'add-every-10-seconds': {
        'task': 'periodical.tasks.test',
        'schedule': crontab (minute='*/10',hour='17,19', day_of_week='mon,tue,wed,thu,fri'),
        'args': (16, 16)
    },
}



app.conf.timezone = 'UTC'

if __name__ == '__main__':
    app.start()