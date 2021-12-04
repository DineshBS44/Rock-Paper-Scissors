import logo from './logo.svg';
import './App.css';
import {Button, Form, Input} from 'semantic-ui-react';
import React from 'react';
import axios from 'axios';

class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      image: null,
      displayError: "",
      displayResult: "",
    };
  }

  onSubmitHandler = (event) => {
    event.preventDefault();
    
    this.setState({displayResult: ""});
    if(this.state.image != null) {
      const formData = new FormData();
      formData.append('image', this.state.image);
      fetch('http://localhost:5000/api/predict', {
        method: 'POST',
        body: formData
      })
      .then(response => response.json())
      .then(response => {
        if (response.error) {
          this.setState({
            displayError: response.error,
            displayResult: "",
          });
        } else {
          this.setState({
            displayError: "",
            displayResult: response.MostLikelyPrediction,
          });
        }
      });

      console.log("Executing this");
      // axios.post('http://localhost:5000/api/predict', formData)
      // .then(response => {
      //   if (response.data.error) {
      //     this.setState({
      //       displayError: response.data.error,
      //       displayResult: "",
      //     });
      //   } else {
      //     this.setState({
      //       displayError: "",
      //       displayResult: response.data.Prediction,
      //     });
      //   }
      // });
    }

  };

  onFileChange = event => {
    this.setState({ image: event.target.files[0] });  
  };

  render() {
    return (
      <div>
        <h1>Rock, Paper and Scissors ML Prediction</h1>
        <br />
        <h3>Upload an image below to see the prediction</h3>
        <br />
        <Form onSubmit={this.onSubmitHandler}>
        <Form.Field>
        <Input type="file" accept=".png" onChange={this.onFileChange}></Input>
        </Form.Field>
        <br />
        <Button primary>Upload!</Button>
        </Form>
        <br />
        <br />
        <p>{this.state.displayError}</p>
        <br />
        <br />
        <p> The result of the prediction is: {this.state.displayResult}</p>
      </div>
    );
  }
}

export default App;
