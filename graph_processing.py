import datetime

from twitter.models import Company
from twitter import settings

# for one company
class Graph:
    DATETIME_FORMAT = '%Y-%m-%d_%H:%M'
    def __init(self):
        # self.scores = {}

    def prepare_attributes(self):
        companies_attributes = []
        for company_name in settings.TO_TRACK:
            print company_name
            # TODO: add other details with Google Knowlege Graph
            company = {
                'id_str': company_name,
                'name': company_name,
                'brand_score': 0.0,
                'tweet_score': 0.0,
                'news_score': 0.0
            }
            companies_attributes.append(company)
            # self.scores[company_name] = {
            #     'current_tweet_score': 0.0,
            #     'current_news_score': 0.0,
            #     'brand_score': 0.0
            # }
        return companies_attributes

    # To init Company
    def init_db(cls, companies_attributes):
        print 'initing db for first time setup'
        companies = Company.create_or_update(*companies_attributes)

    def compute_score():
        pass

    def read_news(self):
        pass
