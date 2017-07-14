Tutorial 1: Intro to Celery
from celery import Celery

app = Celery('tasks', broker='amqp://lcoalhost//')

@app.tasksdef reverse(string)
    return string[::-1]


# in terminal to start celery, see celery tasks monitor
# specify learn_celery.worker according to python filename
celery -A tasks learn_celery.worker --loglevel=info
# start RabbitMQ
sudo service rabbitmq-server start
sudo rabbitmqctl status

# in another terminal /  python code
reverse.delay('anthony')
>> AsyncResult task id (in terminal / python code)
==
>> ynohtna ( "anthony" spell backwards in celery monitor)

Tutorial 2: Integrate Celery with Flask
Browser visit Flask endpoint
Flask init async process and return 'task is handling' e.g. file is uploading, generating report, sending email etc to user better UX

#############
from flask mport Flask
flask celery configure pattern available in Flask website:
    def make_celery(app):
        celery = Celery(app.import_name, backend=app.config['CELERY_BACKEND'],
                        broker=app.config['CELERY_BROKER_URL'])
        celery.conf.update(app.config)
        TaskBase = celery.Task
        class ContextTask(TaskBase):
            abstract = True
            def __call__(self, *args, **kwargs):
                with app.app_context():
                    return TaskBase.__call__(self, *args, **kwargs)
        celery.Task = ContextTask
        return celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://localhost//'
app.config['CELERY_BACKEND'] ='db+mysql://somename:somename@172.123.112.23/sometask'

celery = make_celery(app)

@app.route('/endpoint')
def process(name):
    reverse.delay(name)
    return name

# name give in the python filename
@celery.task(name='learn_celery.reverse')
def reverse(string):
    return string[::-1]
if __name__ == '__main__':
    app.run(debug=True)
###############
Tutorial 3: Celery backend- store the result celery return instead of jsut a task id
define CELERY_RESULT_BACKEND: database, redis, cache, MongoDB, amqp
for this tutorial using 'db+mysql' pretty bad

use Redis as result backend, but RabbitMQ as message broker (popular)
in my case neo4j as result backend, ""
    app = Celery('tasks', backend='redis://localhost', broker='pyamqp://')

result = revers.delay('anthony')
result.status
>> 'PENDING'
>> 'SUCCESS'

to execute something when result is back
result.ready() == True:
    xxxx

result.get()
>>'ynohtna'

#######
Tutorial 4: Flask, Celery & SQLAlchemy
integreate with ORM
