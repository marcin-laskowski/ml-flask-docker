import json
from flask import Flask, request
from syndicai import PythonPredictor

app = Flask(__name__)


@app.route('/')
def hello():
    """ Main page of the app. """
    return "Hello World!"


@app.route('/predict')
def predict():
    """ Return JSON serializable output from the model """
    payload = request.args
    classifier = PythonPredictor("")
    return classifier.predict(payload)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
