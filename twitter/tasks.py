from twitter.celery import app
from twitter.tweet_processing import TweetProcessing
from graph.graph_processing import Graph

@app.task
def bulk_parsing(users_attributes, tweets_attributes):
    # writing to DB
    TweetProcessing.batch_processing(users_attributes, tweets_attributes)
#
# @app.task
# def first_time_setup(graph_attributes):
#     Graph.init_db(graph_attributes)
