require('file?name=[name].[ext]!../node_modules/neo4j-driver/lib/browser/neo4j-web.min.js');
var Event = require('./models/Event');
var Tweet = require('./models/Tweet');
// var MovieCast = require('./models/MovieCast');
var _ = require('lodash');

var neo4j = window.neo4j.v1;
var driver = neo4j.driver("bolt://localhost", neo4j.auth.basic("neo4j", "password"));

function searchEvents(queryString) {
  var session = driver.session();
  return session
    .run(
      'MATCH (event:Event) \
      WHERE event.name =~ {name} \
      RETURN event',
      {name: '(?i).*' + queryString + '.*'}
    )
    .then(result => {
      session.close();
    //   console.log('Event result: ')
    //   console.log(result.records)
      return result.records.map(record => {
        return new Event(record.get('event'));
      });
    })
    .catch(error => {
      session.close();
      throw error;
    });
}

function getEvent(name) {
  var session = driver.session();
  return session
    .run(
      "MATCH (event:Event {name:{name}}) \
      OPTIONAL MATCH (event)<-[:TWEET_FROM]-(tweet:Tweet) \
      RETURN event.name AS name, \
      collect([tweet.text, \
           tweet.sentiment_polarity, tweet.created_at]) AS tweet_detail \
      LIMIT 1", {name})
    .then(result => {
        //   ORDER BY tweet.sentiment_polarity DESC

      session.close();

      if (_.isEmpty(result.records))
        return null;

        // console.log('get event: ')
        // console.log(result.records)

      var record = result.records[0];
      return new Tweet(record.get('name'), record.get('tweet_detail'))
    //   return new MovieCast(record.get('name'), record.get('tweet'));
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
