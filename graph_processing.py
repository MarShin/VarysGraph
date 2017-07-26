from twitter.models import Company
from twilio.rest import Client
from twitter import settings
from neomodel import db

class Graph:
    def __init(self):
        self.score = 0
        db.set_connection(settings.NEO4J_URL)

    # To init Company, Tweets, News Node
    def init_db(self):
        print 'initing db for first time setup'
        for company in settings.TO_TRACK:
            print company
        # pass

    def compute_score():
        pass


    def read_news(self):
        pass

    # Need ~9seconds for sms to arrive
    # Every sms cost $0.04 HKD
    def send_sms(self, to_number, text='Alert from GraphAlert'):
        if to_number is None:
            print 'missing phone number'
            print
            logging.debug('SMS Receiver phone number missing')
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            to=to_number,
            from_="+14156502580",
            body=text)
        print 'SMS sent: ' + str(message.sid)

    def send_email(to_email, text='Alert from GraphAlert'):
        pass
