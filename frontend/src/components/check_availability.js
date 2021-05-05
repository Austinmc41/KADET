import { Button } from 'react-bootstrap';
import history from '../history';
import React, { Component } from "react";
import axios from "axios";

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

class RotationStatus extends Component {
  constructor(props) {
    super(props);
    this.state = {
      statusList: [],
      requestList: [],
      modal: false,
      activeItem: {
        Status: "",
      },
    };
  }

  componentDidMount() {
  }

  refreshList = () => {
    axios
      .get("/rotationcheck/api/")
      .then((res) => this.setState({ statusList: res.data }))
      .catch((err) => console.log(err));
  };

  refreshSchedule = () => {
    axios
      .get("/requests/api/")
      .then((res) => this.setState({ requestList: res.data }))
      .catch((err) => console.log(err));
  };

  toggle = () => {
    this.setState({ modal: !this.state.modal });
  };

  handleSubmit = (item) => {
    this.toggle();

    if (item.email) {
      axios
        .put(`/requests/api/${item.id}/`, item)
        .then((res) => this.refreshSchedule());
      return;
    }
    axios
      .post("/requests/api/", item)
      .then((res) => this.refreshSchedule());
  };

  handleDelete = (item) => {
    axios
      .delete(`/requests/api/${item.id}/`)
      .then((res) => this.refreshSchedule());
  };

  createItem = () => {
    const item = {Status: "" };

    this.setState({ activeItem: item, modal: !this.state.modal });
  };

  editItem = (item) => {
    this.setState({ activeResident: item });
  };

  renderStatus = () => {
    const newItems = this.state.statusList;

    return newItems.map((item) => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className={`mr-2`}
        >
          {item.Status}
        </span>

      </li>
    ));
  };


  render() {
    return (
      <main className="container">
        <h3 className="text-center">Complete the pre-check before attempting to generate a schedule</h3>
        <div className="text-center">
          <form>
            <Button variant="btn btn-success" onClick={() => this.refreshList()}>Run Availability Check</Button>
          </form>
        </div>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
                {this.renderStatus()}
            </div>
          </div>
        </div>
        <div className="text-center">
          <form>
          <Button variant="btn btn-success" onClick={() => history.push('/pre_algorithm')}>view schedule of vacations</Button>
          </form>
        </div>
      </main>
    );
  }

}

export default RotationStatus;