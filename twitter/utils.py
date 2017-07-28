from twitter.tweet_processing import TweetProcessing
from twitter.tasks import bulk_parsing

def stream_pipeline(statuses):
    users_attributes, tweets_attributes = TweetProcessing.prepare_batch_processing(statuses)

    # print 'BATCH users_attributes: '
    # print users_attributes
    print
    print 'BATCH tweets_attributes'
    print tweets_attributes

    bulk_result = bulk_parsing.delay(users_attributes, tweets_attributes)

    # if bulk_result.ready():
    #     changes = compute_score()
    #     if changes >= threshold:
    #          alert.send_sms('+85262308397', 'Tesla score increased! check our graph')
    #     if changes <= threshold:
    #         alert.send_sms('+85262308397', 'Tesla score decreased! check our graph')
