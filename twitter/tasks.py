from twitter.celery import app
from twitter.tweet_processing import TweetProcessing


@app.task
def bulk_parsing(users_attributes, tweets_attributes):
    # writing to DB
    TweetProcessing.batch_processing(users_attributes, tweets_attributes)
