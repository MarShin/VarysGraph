var _ = require('lodash');

function Tweet(name, tweet) {
  _.extend(this, {
    name: name,
    tweets: tweet.map(function (t) {
      return {
        text: t[0],
        polarity: t[1],
        created_at: t[2]
      }
    })
  });
}

module.exports = Tweet;
