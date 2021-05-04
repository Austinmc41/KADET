import { Button } from 'react-bootstrap';
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
        <main>
            <div className="text-center">
                <h3 className="text-center">Complete the pre-check before attempting to generate a schedule</h3>
                <form>
                    <Button variant="btn btn-success" onClick={() => this.refreshList()}>Run Availability Check</Button>
                </form>
            </div>
            <div>
                <div>
                    <div className="card p-3">
                        <div className="mb-4">
                        </div>
                        <ul className="list-group list-group-flush border-top-0">
                            {this.renderStatus()}
                        </ul>
                        <div>
                        </div>
                    </div>
                </div>
            </div>
        </main>
    );
  }
}

export default RotationStatus;