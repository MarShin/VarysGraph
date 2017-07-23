from twitter.tweet_processing import TweetProcessing
# from twitter.tasks import bulk_parsing

def stream_pipeline(statuses):
    users_attributes, tweets_attributes = TweetProcessing.prepare_batch_processing(statuses)

    print 'BATCH users_attributes: '
    print users_attributes
    print
    print 'BATCH tweets_attributes'
    print tweets_attributes

    # bulk_parsing.delay(users_attributes, tweets_attributes)
