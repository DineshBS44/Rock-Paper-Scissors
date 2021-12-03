import matplotlib.pyplot as plt
import numpy as np

import tensorflow as tf
import tensorflow_datasets as tfds

from tensorflow import keras

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    image = request.args.get('image')
    InputData = [[image]]
    loaded_model = keras.models.load_model('./my_model')
    Output = loaded_model.predict(InputData)
    Output = '{ "Prediction": "' + str(Output[0]) + '" }'

    return Output