# Varys

Real time world events monitoring and alert system by crawling information from the internet, just as Varys the Master of Whisperers and his little birds

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

```
Python 2.7
Conda (miniconda package manager is fine)
RabbitMQ
Celery
Neo4J
```

### Installing

A step by step series of examples that tell you have to get a development env running

Conda create & activate a new enviornment for the project

```
conda create -n yourenvname python=x.x
```

Install packages

```
conda install neomodel celery amqp textblob twilio tweepy
```
### Running

To start Varys to 1) grab tweets & news, 2) analyze the data, 3)store & visualize in graph, 4) watch for score changes & send alert

1. Start rabbitmq-server

2. Start neo4j in your system, where credentials set to following upon browsing to `http://127.0.0.1:7474/browser/` 
```
ac: neo4j
pw: password
```

3. To run celery worker in 1st terminal

```
celery -A twitter worker -l info -Q streaming -n streaming
```

4. In 2nd terminal, run 

```
python start_streaming.py
```
NOTE: stream_pipeline() could be whatever the steps you want where you process the tweets. I include a simple example in the utils.py module *batch_size should be the amount of tweets processed at once.

### Development

1. Checkout and Pull the latest development
2. Branch out for feature develpment
3. Merge back to development

