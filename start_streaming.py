from twitter.streaming_api import Streaming
from twitter.utils import stream_pipeline
from twitter import settings
from graph.graph_processing import Graph
from graph.alert import Alert
from neomodel import db
from twitter.tasks import news_bulk_parsing

print 'initiating Streamer'
db.set_connection(settings.NEO4J_URL)

first_time = False
# first_time = True

if first_time:
    clear_neo4j_database(db)
    graph = Graph()
    news_attributes = graph.prepare_news_attributes()
    print 'news'
    print news_attributes
    news_result = news_bulk_parsing.delay(news_attributes)
    companies_attributes = graph.prepare_attributes()
    print 'companies_attributes'
    print companies_attributes
    graph.init_db(companies_attributes)
    print 'DB initiated!!!'

    Alert.send_sms('+85262308397', 'Tesla score increased! check our graph')
    Alert.send_email('martinshin95@gmail.com', 'Welcome to Varys')
else:
    streamer = Streaming(pipeline=stream_pipeline, batch_size=10)
    print 'start streaming... '
    streamer.start_streaming(to_track=settings.TO_TRACK)
