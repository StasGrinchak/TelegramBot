import os

from periodical.celery import app

from main import morning
@app.task
def add(x, y):
    print("я срабатываю каждые 20 секунд")
    morning()
    return x + y


@app.task
def test(x, y):
    print("я срабатываю каждые 10 секунд")
    return x + y