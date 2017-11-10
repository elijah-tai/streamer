# streamer

The simplest streaming application that I could think of - streaming a binary `0` or `1` based on whether or not a button was clicked.

Mainly to learn Apache Kafka and data visualization for stream data.

### Setup

(On OSX) Install Apache Kafka with Homebrew

```
brew install kafka
```

In another terminal, start the ZooKeeper server, which helps manage the Kafka clusters.

```
zookeeper-server-start ../kafka_2.11-1.0.0/config/zookeeper.properties
```

In another terminal, start the Kafka Server.

```
/usr/local/Cellar/kafka/bin/kafka-server-start libexec/config/server.properties
```

Set up environment and dependencies.

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run a simple Python server to serve HTML.

```
python -m SimpleHTTPServer 8080
```

In another terminal window, run the Flask producer app.

```
export FLASK_APP=producer.py
python -m flask run
```

In another terminal window, run the producer

```
python consumer.py
```

### The Kafka Part

According to the [documentation](http://kafka.apache.org/documentation), Kafka has four core APIs:
* [Producer API](http://kafka.apache.org/documentation.html#producerapi)
* [Consumer API](http://kafka.apache.org/documentation.html#consumerapi)
* [Streams API](http://kafka.apache.org/documentation/streams)
* [Connector API](http://kafka.apache.org/documentation.html#connect)

The APIs most interesting to us will be the Producer API, which is essentially what the button pressing will need to use.

The Streams API is also interesting because it will allow us to process the button clicking in real-time!