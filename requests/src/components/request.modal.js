import React, { Component } from "react";
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Input,
  Label,
  Row,
  Col
} from "reactstrap";

export default class CustomModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeItem: this.props.activeItem,
    };
  }

  handleChange = (e) => {
    let { name, value } = e.target;

    if (e.target.type === "checkbox") {
      value = e.target.checked;
    }

    const activeItem = { ...this.state.activeItem, [name]: value };

    this.setState({ activeItem });
  };

  render() {
    const { toggle, onSave } = this.props;

    const checkInput = () => {
      // may be possible to check form input here, before passing contral back from modal
      onSave(this.state.activeItem)
    };

    return (
      <Modal isOpen={true} toggle={toggle}>
        <ModalHeader toggle={toggle}>Resident's scheduling requests</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="first-name">First name</Label>
              <Input
                type="text"
                id="first-name"
                name="firstName"
                value={this.state.activeItem.firstName}
                onChange={this.handleChange}
                placeholder="Enter first name"
              />
            </FormGroup>
            <FormGroup>
              <Label for="last-name">Last name</Label>
              <Input
                type="text"
                id="last-name"
                name="lastName"
                value={this.state.activeItem.lastName}
                onChange={this.handleChange}
                placeholder="Enter last name"
              />
            </FormGroup>

                <FormGroup>
                  <Label for="email-address">Email address</Label>
                  <Input
                    type="email"
                    id="email-address"
                    name="email"
                    value={this.state.activeItem.email}
                    onChange={this.handleChange}
                    placeholder="Enter email address"
                  />
                </FormGroup>

                <FormGroup>
                  <Label for="first-request">First scheduling request</Label>
                  <Input
                    type="date"
                    id="first-request"
                    name="requestOne"
                    value={this.state.activeItem.requestOne}
                    onChange={this.handleChange}
                  />
                </FormGroup>

                <FormGroup>
                  <Label for="second-request">Second scheduling request</Label>
                  <Input
                    type="date"
                    id="second-request"
                    name="requestTwo"
                    value={this.state.activeItem.requestTwo}
                    onChange={this.handleChange}
                  />
                </FormGroup>


                <FormGroup>
                  <Label for="third-request">Third scheduling request</Label>
                  <Input
                    type="date"
                    id="third-request"
                    name="requestThree"
                    value={this.state.activeItem.requestThree}
                    onChange={this.handleChange}
                  />
                </FormGroup>
          </Form>
        </ModalBody>
        <ModalFooter>
          <Button
            color="success"
            onClick={checkInput}
          >
            Save
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}