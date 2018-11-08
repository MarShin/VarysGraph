import random

from twitter.tweet_processing import TweetProcessing
from twitter.tasks import bulk_parsing
from twitter.models import Company

def stream_pipeline(statuses):
    users_attributes, tweets_attributes = TweetProcessing.prepare_batch_processing(statuses)

    print 'BATCH Tweet'
    print tweets_attributes
    print
    bulk_result = bulk_parsing.delay(users_attributes, tweets_attributes)

    tesla = Company.nodes.get(name='Tesla')
    news_score = random.uniform(-1, 1)
    tweet_score = random.uniform(-1, 1)
    brand_score = news_score + tweet_score

    tesla.news_score = news_score
    tesla.tweet_score = tweet_score
    tesla.brand_score = brand_score
    tesla.save()

    print '/////'
    print 'change score for every batch'
    tesla.refresh()
    print tesla
    print '/////'
