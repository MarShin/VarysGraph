from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
    UniqueIdProperty, RelationshipTo, RelationshipFrom)

from twitter.models import Event, Tweet, Company

config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'

print 'create new events'

tesla = Company.nodes.get(name='Tesla')
print 'tesla'
print tesla

event = Event.nodes.get(name='Model 3 Delivered')
event.weighting = 3.3
event.save()
