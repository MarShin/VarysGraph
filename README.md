# To run celery worker
celery -A twitter worker -l info -Q streaming -n streaming
