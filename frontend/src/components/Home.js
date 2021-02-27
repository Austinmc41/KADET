import React, { Component } from "react";
import { Button } from 'react-bootstrap';
import history from '../history';
import "./Home.css";

export default class Home extends Component {
    render() {
        return (
            <div className="Home">
                <div className="lander">
                    <h1>Welcome!</h1>
                    <p>Get started with our Resident Scheduler!</p>
                    <form>
                        <Button variant="btn btn-success" onClick={() => history.push('/Scheduler')}>Click here to get started</Button>
                    </form>
                </div>
            </div>
        );
    }
}