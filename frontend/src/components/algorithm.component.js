import Table from 'react-bootstrap/Table';
import React, { Component } from "react";
import axios from "axios";

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

class Status extends Component {
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
    this.refreshList();
    this.refreshSchedule();
  }

  refreshList = () => {
    axios
      .get("/algorithm/api/")
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

  renderRequests = () => {
    const newItems = this.state.requestList;
      return newItems.map((item) => (
        <tr>
          <td>
            {item.email}
          </td>
          {Object.entries(item.ResidentSchedule).map( ([key, value]) => (
            <td key={key}>
              {value}
            </td>
          ))}
        </tr>
      ));
  };

  render() {
    const tableHeader = () => {
      let tableHeaderWeeks = [];
      for (let week = 0; week < 52; week++) {
        tableHeaderWeeks.push(<th>week_{week}</th>);
      }
      return tableHeaderWeeks;
    };

    return (
      <main>
        <h3 className="text-center">Algorithm status</h3>
        <div>
          <div>
            <div className="card p-3">
              <div className="mb-4">
              </div>
              <ul className="list-group list-group-flush border-top-0">
                {this.renderStatus()}
              </ul>
              <div>
                <Table striped bordered hover>
                  <thead>
                    <tr>
                      <th>
                        email
                      </th>
                      {tableHeader()}
                    </tr>
                  </thead>
                  <tbody>
                    {this.renderRequests()}
                  </tbody>
                </Table>
              </div>
            </div>
          </div>
        </div>
      </main>
    );
  }
}

export default Status;