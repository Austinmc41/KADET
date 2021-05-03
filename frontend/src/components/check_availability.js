import React, { Component } from "react"; 
import { Button } from 'react-bootstrap'; 
import history from '../history'; 

export default class check_availabilityr extends Component {
    render() {
        return (
            <div className="container">
                <div className="text-center">
                    <h3>Complete the pre-check before attempting to generate a schedule</h3>
                    <form>
                        <Button variant="btn btn-success" onClick={() => history.push('/algorithm')}>Run Availability Check</Button>
                    </form>
                </div>
            </div>
        );
    }
}
 