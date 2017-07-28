from __future__ import absolute_import
from celery import Celery
from twitter import settings
from neomodel import db

db.set_connection(settings.NEO4J_URL)
app = Celery('twitter',
             broker=settings.BROKER_URL,
             include=['twitter.tasks'])
app.config_from_object('twitter.celeryconfig')
if __name__ == '__main__':
    app.start()
