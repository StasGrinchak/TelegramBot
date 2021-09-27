from celery import Celery

app = Celery('periodical',
             broker='redis://127.0.0.1:6379',
             include=['periodical.tasks'])

app.conf.beat_schedule = {
    'add-every-20-seconds': {
        'task': 'periodical.tasks.add',
        'schedule': 20.0,
        'args': (16, 16)
    },
    'add-every-10-seconds': {
        'task': 'periodical.tasks.test',
        'schedule': 10.0,
        'args': (16, 16)
    },
}




app.conf.timezone = 'UTC'

if __name__ == '__main__':
    app.start()