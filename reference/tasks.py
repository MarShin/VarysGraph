from celery import Celery
# both broker works: pyamqp://guest@localhost//
app = Celery('tasks', backend='redis://localhost', broker="amqp://guest:guest@127.0.0.1:5672/")

@app.task
def add(x, y):
    return x + y
