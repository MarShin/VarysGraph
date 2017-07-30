import datetime

import neomodel

class Event(neomodel.StructuredNode):
    name = neomodel.StringProperty(unique_index=True, required=True)
    weighting = neomodel.FloatProperty(required=False)
    modified = neomodel.DateTimeProperty(required=False)

    related_to = neomodel.RelationshipTo('Company', 'ABOUT')
    tweet_from = neomodel.RelationshipTo('Tweet', 'TWEET_FROM')
    cited_from = neomodel.RelationshipTo('News', 'CITE_FROM')

    def save(self):
        self.modified = datetime.datetime.now()
        super(Event, self).save()

class Company(neomodel.StructuredNode):
    id_str = neomodel.StringProperty(unique_index=True, required=True)
    name = neomodel.StringProperty(required=False)
    created_at = neomodel.DateTimeProperty(required=False)
    modified = neomodel.DateTimeProperty(required=False)
    description = neomodel.StringProperty(required=False)
    brand_score = neomodel.FloatProperty(required=False)
    tweet_score = neomodel.FloatProperty(required=False)
    news_score = neomodel.FloatProperty(required=False)
    stock_price = neomodel.FloatProperty(required=False)
    stock_change = neomodel.FloatProperty(required=False)
    mkt_cap = neomodel.FloatProperty(required=False)

    def save(self):
        self.modified = datetime.datetime.now()
        super(Company, self).save()

class News(neomodel.StructuredNode):
    pass

class Tweet(neomodel.StructuredNode):
    id_str = neomodel.StringProperty(unique_index=True, required=True)
    created_at = neomodel.DateTimeProperty(required=False)
    modified = neomodel.DateTimeProperty(required=False)
    retweeted = neomodel.BooleanProperty(required=False)
    retweet_id_str = neomodel.StringProperty(required=False, default='')
    reply_id_str = neomodel.StringProperty(required=False, default='')
    quote_id_str = neomodel.StringProperty(required=False, default='')
    mention_ids_str = neomodel.ArrayProperty(required=False, default=[])
    text = neomodel.StringProperty(required=False)
    coordinates = neomodel.ArrayProperty(required=False, default=[])
    lang = neomodel.StringProperty(required=False)
    features = neomodel.JSONProperty(required=False, default={})
    sentiment_polarity = neomodel.FloatProperty(required=False)
    sentiment_subjectivity = neomodel.FloatProperty(required=False)

    retweets = neomodel.RelationshipTo('Tweet', 'RETWEETS')
    mentions = neomodel.RelationshipTo('User', 'MENTIONS')
    replies = neomodel.RelationshipTo('Tweet', 'REPLIES')
    tags = neomodel.RelationshipTo('Hashtag', 'TAGS')
    contains = neomodel.RelationshipTo('Link', 'CONTAINS')
    quotes = neomodel.Relationship('Tweet', 'QUOTES')
    tweet_about = neomodel.RelationshipTo('Company', 'TWEETS')

    def save(self):
        self.modified = datetime.datetime.now()
        super(Tweet, self).save()


class User(neomodel.StructuredNode):
    id_str = neomodel.StringProperty(unique_index=True, required=True)
    name = neomodel.StringProperty(required=False)
    screen_name = neomodel.StringProperty(required=False)
    followers_count = neomodel.IntegerProperty(required=False)
    friends_count = neomodel.IntegerProperty(required=False)
    modified = neomodel.DateTimeProperty(required=False)
    created_at = neomodel.DateTimeProperty(required=False)
    description = neomodel.StringProperty(required=False)
    location = neomodel.StringProperty(required=False)
    coordinates = neomodel.ArrayProperty(required=False, default=[])
    time_zone = neomodel.StringProperty(required=False)
    url = neomodel.StringProperty(required=False)
    lang = neomodel.StringProperty(required=False)

    follows = neomodel.RelationshipTo('User', 'FOLLOWS')
    posts = neomodel.RelationshipTo('Tweet', 'POSTS')

    def save(self):
        self.modified = datetime.datetime.now()
        super(User, self).save()


class Hashtag(neomodel.StructuredNode):
    text = neomodel.StringProperty(unique_index=True, required=True)


class Link(neomodel.StructuredNode):
    url = neomodel.StringProperty(unique_index=True, required=True)
