import React from 'react';
import { automlApi } from '../services/AutomlApi';

class HelloPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      data: "null",
    }
  }

  async componentDidMount() {
    this.handleGetHello();
  }

  handleGetHello = async () => {
    try {
      const response = await automlApi.getHello();
      const data = response.data;
      this.setState({ data });
    } catch (error) {
      console.log(error);
    }
  }

  render() {
    return(
      <div>
        <p>This is Hello page!</p>
        <p>Here is the message from backend: {this.state.data} </p>
      </div>
    );
  }
}

export default HelloPage;
