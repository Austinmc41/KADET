import React, { Component } from "react";
import { Button } from 'react-bootstrap';
import history from '../history';

export default class run_scheduler extends Component {
    render() {
        return (
            <div className="container">
                <div className="text-center">
                    <h3>Let the algorithm do its magic!</h3>
                    <form>
                        <Button variant="btn btn-success" onClick={() => history.push('/Settings')}>Generate Schedule</Button>
                    </form>
                </div>
            </div>
        );
    }
}