from twitter.celery import app
from twitter.tweet_processing import TweetProcessing
from graph.graph_processing import Graph

@app.task
def bulk_parsing(users_attributes, tweets_attributes):
    # writing to DB
    TweetProcessing.batch_processing(users_attributes, tweets_attributes)

@app.task
def news_bulk_parsing(news_attributes):
    print 'celery parsing news'
    Graph.batch_news_processing(news_attributes)
