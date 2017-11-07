# streamer

The simplest streaming application that I could think of - streaming a binary `0` or `1` based on whether or not a button was clicked.

Mainly to learn Apache Kafka and data visualization for stream data.

### Setup

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

In another terminal window, run the Flask app.

```
export FLASK_APP=app.py
python -m flask run
```

Start Kafka streaming

