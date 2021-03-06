import React from 'react';
import Accordion from 'react-bootstrap/Accordion';
import Card from 'react-bootstrap/Card'

  /*
      Throw axios and constructor to declare state
        for the render below function to output the data from backend/residentrequests/api/
        Maybe terrence or draco can do it, should be fairly simple. (otherwise i can do it but not till next wednesday)
    */    
    const ListRequests = (props) => {
      return (
      <main className="container">
        <h3 className="text-center">Schedule Requests</h3>
        <div className="row">
          <div className="col-md-8 col-sm-10 mx-auto p-0">
            <div className="card p-3">
        <Accordion defaultActiveKey="">
      <Card>
      <Accordion.Toggle as={Card.Header} eventKey="0">
      '"First Name" + "Lastname"''
      </Accordion.Toggle>
      <Accordion.Collapse eventKey="0">
      <Card.Body>
        <p>Email Address:</p>
        <p>Request 1:</p>
        <p>Request 2:</p>
        <p>Request 3:</p>
      </Card.Body>
      </Accordion.Collapse>
      </Card>
      <Card>
      <Accordion.Toggle as={Card.Header} eventKey="1">
      Click me!
      </Accordion.Toggle>
      <Accordion.Collapse eventKey="1">
      <Card.Body>Hello! I'm another body</Card.Body>
      </Accordion.Collapse>
      </Card>
      </Accordion>
      </div>
      </div>
      </div>
      </main>
      );
    };
export default ListRequests;