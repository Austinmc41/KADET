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

    return (
      <Modal isOpen={true} toggle={toggle}>
        <ModalHeader toggle={toggle}>Rotation Block Details</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="criteria-label">Rotation label</Label>
              <Input
                type="text"
                id="criteria-label"
                name="RotationType"
                value={this.state.activeItem.RotationType}
                onChange={this.handleChange}
                placeholder="Enter rotation label"
              />
            </FormGroup>
            <FormGroup>
              <Label for="criteria-minResident">Minumum residents needed</Label>
              <Input
                type="number"
                id="criteria-minResident"
                name="MinResident"
                value={this.state.activeItem.MinResident}
                onChange={this.handleChange}
                placeholder="Enter number of residents"
              />
            </FormGroup>
            <FormGroup>
              <Label for="criteria-maxResident">Maximum residents needed</Label>
              <Input
                type="number"
                id="criteria-maxResident"
                name="MaxResident"
                value={this.state.activeItem.MaxResident}
                onChange={this.handleChange}
                placeholder="Enter number of residents"
              />
            </FormGroup>
          </Form>
        </ModalBody>
        <ModalFooter>
          <Button
            color="success"
            onClick={() => onSave(this.state.activeItem)}
          >
            Save
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}