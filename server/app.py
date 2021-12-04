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

    outputList = [[Output[0][0], "Rock"], [Output[0][1], "Paper"], [Output[0][2], "Scissors"]]
    outputList.sort(reverse=True)

    print(outputList)

    return jsonify({
        'MostLikelyPrediction': str(outputList[0][1]),
        'MostLikelyPredictionProbability': str(round(float(outputList[0][0]), 6)),
        'SecondMostLikelyPrediction': str(outputList[1][1]),
        'SecondMostLikelyPredictionProbability': str(round(float(outputList[1][0]), 6)),
        'ThirdMostLikelyPrediction': str(outputList[2][1]),
        'ThirdMostLikelyPredictionProbability': str(round(float(outputList[2][0]), 6))
    })


@app.route("/")
def index():
    return "Not a valid endpoint"
