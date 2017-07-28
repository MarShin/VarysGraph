# To run celery worker
celery -A twitter worker -l info -Q streaming -n streaming

# *stream_pipeline could be whatever you want where you process the tweets. I include a simple example in the utils.py module *batch_size should be the amount of tweets processed at once.
