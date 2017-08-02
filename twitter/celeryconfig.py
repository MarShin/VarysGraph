from kombu import Queue, Exchange


CELERY_TASK_SERIALIZER = 'json'

CELERY_QUEUES = (
    Queue('streaming', Exchange('streaming'), routing_key='streaming'),
)

CELERY_ROUTES = {
    'twitter.tasks.bulk_parsing': {'queue': 'streaming', 'routing_key': 'streaming'},
    'twitter.tasks.news_bulk_parsing': {'queue': 'streaming', 'routing_key': 'streaming'},
}
