# Rock, Paper and Scissors
> A project that is built for learning how Neural networks work and also to gain experience on how to build a basic end to end project that uses client-server architecture involving Neural Networks

A website that predicts if a 300x300 image is either a rock, paper or a scissor using a ML Model

## ML Model
- A Custom Neural network that is build using Tensorflow and Keras
- A Convolutional Neural Network is design with a lot of parameter tuning and testing to get better accuracy
- The Model is written and executed in Google Colab (faster execution due to its inbuilt GPU feature)
- The Trained Model is saved to the Backend that is present the `server` folder

## Backend
- The Backend uses `Flask` to create the `/api/predict` POST endpoint that predicts the output
- The input taken is an image sent by the client side.
- The saved Trained model that uses Convolutional Neural Net is loaded and run with the given input
- The output is sent back to the client

## Client
- The Client is written is `ReactJS`
- It is a simple frontend that takes in an image and a button to predict
- The data is sent to the Backend using the POST request and the predicted output is displayed