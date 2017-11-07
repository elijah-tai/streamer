from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/button-click', methods = ['GET'])
def handle_button_click():
    return "Success!"
