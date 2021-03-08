import Form from 'react-bootstrap/Form'
import Accordion from 'react-bootstrap/Accordion';
import Card from 'react-bootstrap/Card';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';

export default function DetailViewRequests() {
    return (
      <main className="container">
        <h3 className="text-center">Schedule Requests</h3>
        <div className="row">
          <div className="col-md-5 col-sm-10 mx-auto p-0">
          <div className="card p-3">
		        <Form>
  <Form.Row className="align-items-center">
    <Col xs="auto">
      <Form.Label htmlFor="inlineFormInput" srOnly>
        Name
      </Form.Label>
      <Form.Control
        className="mb-2"
        id="inlineFormInput"
        placeholder="Email"
      />
    </Col>
    <Col xs="auto">
      <Button type="submit" className="mb-2">
        Obtain Schedule Requests
      </Button>
    </Col>
  </Form.Row>
</Form>
      </div>
      </div>
      {false ? (
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
        ) : (<p></p>)}
      </div>
      </main>
    );
  }