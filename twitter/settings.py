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

# SendGrid credentials
SENDGRID_API_KEY = ''

NEO4J_URL = ''

# Things to track: Company name
# TO_TRACK = [
#     'Tesla',
#     'Samsung',
#     'Snapchat',
#     'Google',
#     ]

TO_TRACK = ['autopilot']

# DateTime format
DATETIME_FORMAT = '%Y-%m-%d_%H:%M'

# Used to get twitter API credential
from graph.local_settings import *
