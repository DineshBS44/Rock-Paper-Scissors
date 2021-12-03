import matplotlib.pyplot as plt
import numpy as np

import tensorflow as tf
from tensorflow import keras

from flask import Flask, request

app = Flask(__name__)

@app.route("/api/predict", methods=["POST"])
def predict():
    file = request.file
    image = file.get('image')
    InputData = [[image]]
    loaded_model = keras.models.load_model('./my_model')
    Output = loaded_model.predict(InputData)
    Output = '{ "Prediction": "' + str(Output[0]) + '" }'

    return jsonify({
        'Prediction': str(Output[0])
    })

@app.route("/")
def index():
    return "Not a valid endpoint"
