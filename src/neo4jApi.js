require('file?name=[name].[ext]!../node_modules/neo4j-driver/lib/browser/neo4j-web.min.js');
var Event = require('./models/Event');
var MovieCast = require('./models/MovieCast');
var _ = require('lodash');

var neo4j = window.neo4j.v1;
var driver = neo4j.driver("bolt://localhost", neo4j.auth.basic("neo4j", "password"));

function searchEvents(queryString) {
  var session = driver.session();
  return session
    .run(
      'MATCH (event:Event) \
      WHERE event.name =~ {title} \
      RETURN event',
      {title: '(?i).*' + queryString + '.*'}
    )
    .then(result => {
      session.close();
      console.log('Event result: ')
      console.log(result.records)
      return result.records.map(record => {
        return new Event(record.get('event'));
      });
    })
    .catch(error => {
      session.close();
      throw error;
    });
}

function getEvent(title) {
  var session = driver.session();
  return session
    .run(
      "MATCH (event:Event {title:{title}}) \
      OPTIONAL MATCH (event)<-[r]-(person:Person) \
      RETURN event.title AS title, \
      collect([person.name, \
           head(split(lower(type(r)), '_')), r.roles]) AS cast \
      LIMIT 1", {title})
    .then(result => {
      session.close();

      if (_.isEmpty(result.records))
        return null;

      var record = result.records[0];
      return new MovieCast(record.get('title'), record.get('cast'));
    })
    .catch(error => {
      session.close();
      throw error;
    });
}

function getGraph() {
  var session = driver.session();
  return session.run(
    'MATCH (e:Event)<-[:TWEET_FROM]-(t:Tweet) \
    RETURN e.title AS event, collect(t.text) AS tweet \
    LIMIT {limit}', {limit: 100})
    .then(results => {
      session.close();
      var nodes = [], rels = [], i = 0;
      results.records.forEach(res => {
        nodes.push({title: res.get('event'), label: 'event'});
        var target = i;
        i++;

        res.get('tweet').forEach(text => {
          var tweet = {text: text, label: 'tweet'};
          var source = _.findIndex(nodes, tweet);
          if (source == -1) {
            nodes.push(tweet);
            source = i;
            i++;
          }
          rels.push({source, target})
        })
      });

      return {nodes, links: rels};
    });
}

exports.searchEvents = searchEvents;
exports.getEvent = getEvent;
exports.getGraph = getGraph;
