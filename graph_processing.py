import datetime

from twilio.rest import Client
from twitter.models import Company
from twitter import settings
from neomodel import db

class Graph:
    DATETIME_FORMAT = '%Y-%m-%d_%H:%M'
    def __init(self):
        self.score = 0
        db.set_connection(settings.NEO4J_URL)

    # To init Company, Tweets, News Node
    def init_db(self):
        print 'initing db for first time setup'
        companies_attributes = []
        for company_name in settings.TO_TRACK:
            print company_name
            # TODO: add other details with Google Knowlege Graph
            company = {
                'id_str': company_name,
                'name': company_name,
                'created_at': datetime.datetime.now().strftime(self.DATETIME_FORMAT),
                'modified_at': datetime.datetime.now().strftime(self.DATETIME_FORMAT),
            }
            companies_attributes.append(company)

        print companies_attributes
        # companies = Company.create_or_update(*companies_attributes)
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
