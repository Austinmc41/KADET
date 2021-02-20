import React, { Component } from "react";

const criteriaItems = [
  {
    id: 1,
    RotationType: "ipsum dolor",
    MinResident: 2,
    MaxResident: 5,
  },
  {
    id: 2,
    RotationType: "sit amet",
    MinResident: 3,
    MaxResident: 5,
  },
  {
    id: 3,
    RotationType: "enim ad",
    MinResident: 4,
    MaxResident: 5,
  },
  {
    id: 4,
    RotationType: "minim veniam",
    MinResident: 5,
    MaxResident: 5,
  },
];

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      criteriaList: criteriaItems,
    };
  }

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
          >
            Edit
          </button>
          <button
            className="btn btn-danger"
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
        <p><h4 className="text-uppercase text-center my-4">(non-functional, just display)</h4></p>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="mb-4">
                <button className="btn btn-primary">
                  Add criteria
                </button>
              </div>

              <ul className="list-group list-group-flush border-top-0">
                {this.renderCriteria()}
              </ul>
            </div>
          </div>
        </div>
      </main>
    );
  }
}

export default App;