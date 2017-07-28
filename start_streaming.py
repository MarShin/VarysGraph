from twitter.streaming_api import Streaming
from twitter.utils import stream_pipeline
from twitter import settings
from graph_processing import Graph
from alert import Alert
from neomodel import db

print 'initiating Streamer'
db.set_connection(settings.NEO4J_URL)
first_time = False

if first_time:
    graph = Graph()
    companies_attributes = graph.prepare_attributes()
    print 'companies_attributes'
    print companies_attributes

    graph.init_db(companies_attributes)
    print 'DB initiated!!!'
    # Alert.send_sms('+85262308397', 'Tesla score increased! check our graph')
else:
    streamer = Streaming(pipeline=stream_pipeline, batch_size=10)
    print 'start streaming... '
    streamer.start_streaming(to_track=settings.TO_TRACK)
