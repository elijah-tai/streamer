from flask import Flask
from flask_cors import CORS
from kafka import KafkaProducer

app = Flask(__name__)
CORS(app)

producer = KafkaProducer()

@app.route('/button-click', methods = ['GET'])
def handle_button_click():
    producer.send('streamer', b'User 1 clicked the subscribe button.') 
    return "Success!"
