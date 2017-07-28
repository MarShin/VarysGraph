import datetime

from twitter.models import Company
from twitter import settings
from neomodel import config

class Graph:
    DATETIME_FORMAT = '%Y-%m-%d_%H:%M'
    def __init(self):
        self.score = 0
        config.DATABASE_URL = settings.NEO4J_URL
        # db.set_connection(settings.NEO4J_URL)

    @staticmethod
    # TODO: prepare Tweet & News attribue
    def prepare_attributes():
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
        return companies_attributes

    # To init Company, Tweets, News Node
    @classmethod
    def init_db(cls, companies_attributes):
        print 'initing db for first time setup'
        companies = Company.create_or_update(*companies_attributes)

    def compute_score():
        pass

    def read_news(self):
        pass
