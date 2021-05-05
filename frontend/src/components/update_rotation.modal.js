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
      activeDict: this.props.activeDict,
      activeResident: this.props.activeResident,
      weekKey: this.props.weekKey,
    };
  }

  handleChange = (e) => {
    let { name, value } = e.target;

    console.log('activeDict before: ' + JSON.stringify(this.state.activeDict))

    const activeDict = { ...this.state.activeDict, [name]: value };

    console.log('activeDict after: ' + JSON.stringify(activeDict))

    this.setState({ activeDict });

    this.setState(prevState => ({
      activeResident: {
        ...prevState.activeResident,
        generatedSchedule: activeDict
      }
     }));
  };

  render() {
    const { toggle, onSave } = this.props;

    return (
      <Modal isOpen={true} toggle={toggle}>
        <ModalHeader toggle={toggle}>Rotations</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="resident-rotation">Assign Rotation</Label>
              <Input
                type="select"
                id="resident-rotation"
                name={this.state.weekKey}
                value={this.state.activeDict[this.state.weekKey]}
                onChange={this.handleChange}>
                  <option> </option>
                  <option>VACATION</option>
                  <option>available</option>
              </Input>
            </FormGroup>
          </Form>
        </ModalBody>
        <ModalFooter>
          <Button
            color="success"
            onClick={() => onSave(this.state.activeResident)}
          >
            Save
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}