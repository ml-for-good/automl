import React from 'react';
import keycloak from '../Keycloak';
import { automlApi } from '../services/AutomlApi';

class DashboardPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      data: "null",
    }
  }

  async componentDidMount() {
    this.handleGetDashboard();
  }

  handleGetDashboard = async () => {
    try {
      const response = await automlApi.getDashboard(keycloak.token);
      const data = response.data;
      this.setState({ data });
    } catch (error) {
      console.log(error);
    }
  }

  render() {
    return(
      <div>
        <p>This is Dashboard page!</p>
        <p>Here is the message from backend: {this.state.data} </p>
      </div>
    );
  }
}

export default DashboardPage;
