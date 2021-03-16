import React, { Component } from "react";
import Accordion from 'react-bootstrap/Accordion';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import Modal from "./request.modal";
import axios from "axios";

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

class Requests extends Component {
  constructor(props) {
    super(props);
    this.state = {
      requestsList: [],
      modal: false,
      activeItem: {
      },
    };
  }

  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios
      .get("/requests/api/")
      .then((res) => this.setState({ requestsList: res.data }))
      .catch((err) => console.log(err));
  };

  toggle = () => {
    this.setState({ modal: !this.state.modal });
  };

  handleSubmit = (item) => {

    this.toggle();

    if (item.id) {
      axios
        .put(`/requests/api/${item.id}/`, item)
        .then((res) => this.refreshList());
      return;
    }
    axios
      .post("/requests/api/", item)
      .then((res) => this.refreshList());
  };

  createItem = () => {
    const item = { RotationType: "" };

    this.setState({ activeItem: item, modal: !this.state.modal });
  };

  editItem = (item) => {
    this.setState({ activeItem: item, modal: !this.state.modal });
  };

  renderRequests = () => {
    const newItems = this.state.requestsList;

    return newItems.map((item) => (
        <Accordion>
          <Card>
            <Card.Header className="d-flex justify-content-between align-items-center">
              <div className={`mr-2`}>
                <Accordion.Toggle
                  as={Button}
                  variant="link"
                  eventKey={item.id}
                  title="Click to view scheduling requests"
                >
                  +
                </Accordion.Toggle>
                {item.firstName} {item.lastName}
              </div>
              <div>
                <button
                  className="btn btn-secondary"
                  onClick={() => this.editItem(item)}
                >
                  Edit
                </button>
              </div>
            </Card.Header>
            <Accordion.Collapse eventKey={item.id}>
                <Card.Body className="text-muted">
                  <div  className="list-group border-0">
                    <span className="list-group-item border-0">
                      Email address: {item.email}
                    </span>
                    <span className="list-group-item border-0">
                      First request: {new Date(item.requestOne).toUTCString().slice(0,16)}
                    </span>
                    <span className="list-group-item border-0">
                      Second request: {new Date(item.requestTwo).toUTCString().slice(0,16)}
                    </span>
                    <span className="list-group-item border-0">
                      Third request: {new Date(item.requestThree).toUTCString().slice(0,16)}
                    </span>
                  </div>
                </Card.Body>
              </Accordion.Collapse>
          </Card>
        </Accordion>
    ));
  };

  render() {
    return (
      <main className="container">
        <h3 className="text-center">Resident requests</h3>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="mb-4">
                <button 
                  className="btn btn-primary"
                  onClick={this.createItem}
                >
                  Add requests
                </button>
              </div>
                {this.renderRequests()}
            </div>

          </div>
        </div>
        {this.state.modal ? (
          <Modal
            activeItem={this.state.activeItem}
            toggle={this.toggle}
            onSave={this.handleSubmit}
          />
        ) : null}
      </main>
    );
  }
}

export default Requests;