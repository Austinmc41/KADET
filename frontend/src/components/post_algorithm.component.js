import Accordion from 'react-bootstrap/Accordion';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import Table from 'react-bootstrap/Table';
import React, { Component } from "react";
import Modal from "./update_rotation.modal";
import axios from "axios";

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

class GeneratedSchedule extends Component {
  constructor(props) {
    super(props);
    this.state = {
      requestList: [],
      modal: false,
      dictionaryKey: 0,
      activeItem: {
        Status: "",
      },
      activeDict: {},
      activeResident: {
        generatedSchedule: {},
      },
    };
  }

  componentDidMount() {
    this.refreshSchedule();
  }

  refreshSchedule = () => {
    axios
      .get("https://kadet0354.pythonanywhere.com/schedule/api/grid/")
      .then((res) => this.setState({ requestList: res.data }))
      .catch((err) => console.log(err));
  };

  toggle = () => {
    this.setState({ modal: !this.state.modal });
  };

  handleSubmit = (item) => {
    this.toggle();

    if (item.id) {
      console.log('put attempt for ' + JSON.stringify(item))
      axios
        .put(`https://kadet0354.pythonanywhere.com/schedule/api/grid/${item.id}/`, item)
        .then((res) => this.refreshSchedule());
      return;
    }
    console.log('post attempt for ' + JSON.stringify(item))
    axios
      .post("https://kadet0354.pythonanywhere.com/schedule/api/grid/", item)
      .then((res) => this.refreshSchedule());
  };

  handleDelete = (item) => {
    axios
      .delete(`https://kadet0354.pythonanywhere.com/schedule/api/grid/${item.email}/`)
      .then((res) => this.refreshSchedule());
  };

  createItem = () => {
    const item = {Status: "" };

    this.setState({ activeResident: item, modal: !this.state.modal });
  };

  editItem = (item) => {
    this.setState({ activeResident: item });
  };

  editElement = (element) => {
    this.setState({ activeDict: element, modal: !this.state.modal });
  };

  renderRequests = () => {
    const newItems = this.state.requestList;
      return newItems.map((item) => (
        <tr key={item.id}>
          <td>
            {item.email}
          </td>
          <td>
            {item.name}
          </td>
          <td>
            {item.postGradLevel}
          </td>
          {Object.entries(item.generatedSchedule).map( ([key, value]) => (
            <td key={key}>
              <button
                className="btn btn-info"
                onClick={() => {
                  this.setState({ dictionaryKey: key });
                  this.editItem(item);
                  this.editElement(item.generatedSchedule)
                }}
              >
                {value}
              </button>
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
        <h3 className="text-center">Fully Generated Schedule</h3>
        <div>
          <div className="mb-4">
            <Table striped bordered hover>
              <thead>
                <tr>
                  <th>
                    email
                  </th>
                  <th>
                    name
                  </th>
                  <th>
                    PGY
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
        {this.state.modal ? (
          <Modal
            activeDict={this.state.activeDict}
            activeResident={this.state.activeResident}
            weekKey={this.state.dictionaryKey}
            toggle={this.toggle}
            onSave={this.handleSubmit}
          />
        ) : null}
      </main>
    );
  }
}

export default GeneratedSchedule;