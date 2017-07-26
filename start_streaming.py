from twitter.streaming_api import Streaming
from twitter.utils import stream_pipeline
from twitter import settings
from graph_processing import Graph

print 'initiating Streamer'

first_time = True

if first_time:
    graph = Graph()
    graph.init_db()
    # graph.send_sms('+85262308397', 'Welcome to GraphAlert!')


#
# # *stream_pipeline could be whatever you want where you process the tweets. I include a simple example in the utils.py module *batch_size should be the amount of tweets processed at once. I tried with 100, and it works just fine.
# streamer = Streaming(pipeline=stream_pipeline, batch_size=10)
#
# print 'start streaming... '
# streamer.start_streaming(to_track=settings.TO_TRACK)
