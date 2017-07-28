import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

# Twitter credentials
TWITTER_CONSUMER_TOKEN = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_SECRET = ''

# Twilio credentials
TWILIO_ACCOUNT_SID = ''
TWILIO_AUTH_TOKEN = ''

NEO4J_URL = ''

# Things to track: Company name
# STAGE ONE ONLY 1 COMPANY
TO_TRACK = [
    'Tesla',
    # 'Samsung',
    # 'Snapchat',
    # 'Google',
    ]

# DateTime format
DATETIME_FORMAT = '%Y-%m-%d_%H:%M'


# Used to get twitter API credential
from local_settings import *
