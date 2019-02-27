from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, RelationshipFrom)

from twitter.models import Event, Tweet, Company
config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'


class Country(StructuredNode):
    code = StringProperty(unique_index=True, required=True)

    # traverse incoming IS_FROM relation, inflate to Person objects
    inhabitant = RelationshipFrom('Person', 'IS_FROM')


config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'

print('create new events')

tesla = Company.nodes.get(name='Tesla')
print('tesla')
print(tesla)

# jim = Person(name='Jim', age=3).save()
# jim.age = 4
# jim.save() # validation happens here
# jim = Person.nodes.get(name='Jim')
# jim.delete()
# jim.refresh() # reload properties from neo
# print( jim.id # neo4j internal id

event = Event.nodes.get(name='Model 3 Delivered')
event.weighting = 3.3
event.save()
