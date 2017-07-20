import tweepy

consumer_key = 'XuYKBsUyeL9s1WTtOa6GZcVow'
consumer_secret = 'jBoiK8GX338iEF9K3WdTIg5oRYjxKDNqYYuOgesrgAMVaZcJCY'

access_token = '3084549211-fKwTodC5ohZMACudRLbexgXhe9RmuG9CHrvaws4'
access_token_secret = '9FCPes0XAiq0reaVgc5Cb9TWCrLmiHivd1b784QC8zsrM'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
print

# Get the User object
user = api.get_user('marz_shin')
print user.screen_name
print user.followers_count
for friend in user.friends():
    print friend.screen_name
