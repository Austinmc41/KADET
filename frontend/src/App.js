import React, { Component } from "react";
import Modal from "./components/criterion.modal";
import axios from "axios";

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      criteriaList: [],
      modal: false,
      activeItem: {
        RotationType: "",
        MinResident: 0,
        MaxResident: 0,
      },
    };
  }

  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios
      .get("/criteria/api/")
      .then((res) => this.setState({ criteriaList: res.data }))
      .catch((err) => console.log(err));
  };

  toggle = () => {
    this.setState({ modal: !this.state.modal });
  };

  handleSubmit = (item) => {
    this.toggle();

    if (item.id) {
      axios
        .put(`/criteria/api/${item.id}/`, item)
        .then((res) => this.refreshList());
      return;
    }
    axios
      .post("/criteria/api/", item)
      .then((res) => this.refreshList());
  };

  handleDelete = (item) => {
    axios
      .delete(`/criteria/api/${item.id}/`)
      .then((res) => this.refreshList());
  };

  createItem = () => {
    const item = { RotationType: "", MinResident: 0, MaxResident: 0 };

    this.setState({ activeItem: item, modal: !this.state.modal });
  };

  editItem = (item) => {
    this.setState({ activeItem: item, modal: !this.state.modal });
  };

  renderCriteria = () => {
    const newItems = this.state.criteriaList;

    return newItems.map((item) => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className={`mr-2`}
        >
          {item.RotationType}
        </span>
        <span>
          <button
            className="btn btn-secondary mr-2"
            onClick={() => this.editItem(item)}
          >
            Edit
          </button>
          <button
            className="btn btn-danger"
            onClick={() => this.handleDelete(item)}
          >
            Delete
          </button>
        </span>
      </li>
    ));
  };

  render() {
    return (
      <main className="container">
        <h1 className="text-uppercase text-center my-4">Resident Scheduler app</h1>
        <p><h4 className="text-uppercase text-center my-4">(almost functional)</h4></p>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="mb-4">
                <button 
                  className="btn btn-primary"
                  onClick={this.createItem}
                >
                  Add criteria
                </button>
              </div>

              <ul className="list-group list-group-flush border-top-0">
                {this.renderCriteria()}
              </ul>
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

export default App;