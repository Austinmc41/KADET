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
      activeDict: this.props.activeDict,
      activeResident: this.props.activeResident,
      weekKey: this.props.weekKey,
    };
  }

  handleChange = (e) => {
    let { name, value } = e.target;

    if (e.target.type === "checkbox") {
      value = e.target.checked;
    }

    const activeDict = { ...this.state.activeDict, [name]: value };

    this.setState({ activeDict });

    this.setState({
      activeResident: {
        ResidentSchedule: {
          ...this.state.ResidentSchedule,
          [this.state.weekKey]: value
        }
      }
     });
  };

  render() {
    const { toggle, onSave } = this.props;
    const dictionaryKey = "ResidentSchedule[" + this.state.weekKey + "]"

    return (
      <Modal isOpen={true} toggle={toggle}>
        <ModalHeader toggle={toggle}>Rotations -{this.state.weekKey}-</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="resident-rotation">Rotation</Label>
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