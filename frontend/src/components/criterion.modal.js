
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
              <Label for="criteria-StartRotation">Rotation start date</Label>
              <Input
                type="date"
                id="criteria-StartRotation"
                name="StartRotation"
                value={this.state.activeItem.StartRotation}
                onChange={this.handleChange}
              />
            </FormGroup>
            <FormGroup>
              <Label for="criteria-EndRotation">Rotation start date</Label>
              <Input
                type="date"
                id="criteria-EndRotation"
                name="EndRotation"
                value={this.state.activeItem.EndRotation}
                onChange={this.handleChange}
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
            <FormGroup>
              <Label for="criteria-ResidentYear">Number of years resident has studied</Label>
              <Input
                type="select"
                id="criteria-ResidentYear"
                name="ResidentYear"
                value={this.state.activeItem.ResidentYear}
                onChange={this.handleChange}>
                  <option>0</option>
                  <option>1</option>
                  <option>2</option>
                  <option>3</option>
                  <option>4</option>
                  <option>5</option>
              </Input>
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