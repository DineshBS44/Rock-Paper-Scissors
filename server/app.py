import matplotlib.pyplot as plt
import numpy as np
import cv2

import tensorflow as tf
from tensorflow import keras

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/predict", methods=["POST"])
def predict():
    imgStr = request.files["image"].read()
    npimage = np.fromstring(imgStr, np.uint8)
    image = cv2.imdecode(npimage, cv2.IMREAD_GRAYSCALE)

    InputData = np.array(image)
    print(InputData.shape)
    print(type(InputData))

    InputData = InputData.reshape(1, 300, 300, 1)
    InputData = InputData.astype('float32')
    InputData /= 255
    print(InputData.shape)

    loaded_model = keras.models.load_model('./my_model')
    Output = loaded_model.predict(InputData)

    print("Output: ", Output)
    print(type(Output[0][0]))

    mostProbable = 0.0
    prediction = "None"
    for i in range(3):
        if float(Output[0][i]) > mostProbable:
            mostProbable = float(Output[0][i])
            if i == 0:
                prediction = "Rock"
            elif i == 1:
                prediction = "Paper"
            else:
                prediction = "Scissors"
    
    print("Prediction: ", prediction)

    return jsonify({
        'Prediction': prediction
    })


@app.route("/")
def index():
    return "Not a valid endpoint"
