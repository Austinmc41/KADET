import React from 'react';
//import './Navbar.css';
import * as reactBootstrap from 'react-bootstrap';
import { withRouter } from 'react-router-dom';

const Navigation = (props) => {
    console.log(props);
    return (
        <reactBootstrap.Navbar bg="primary" variant="dark">
            <reactBootstrap.Navbar.Brand href="#home">Resident Scheduler</reactBootstrap.Navbar.Brand>
            <reactBootstrap.Navbar.Toggle aria-controls="basic-navbar-nav" />
            <reactBootstrap.Navbar.Collapse id="basic-navbar-nav">
                <reactBootstrap.Nav className="mr-auto">
                    <reactBootstrap.Nav.Link href="/">Home</reactBootstrap.Nav.Link>
                    <reactBootstrap.Nav.Link href="/Rotations">Criteria</reactBootstrap.Nav.Link>
                    <reactBootstrap.Nav.Link href="/One">One</reactBootstrap.Nav.Link>
                    <reactBootstrap.Nav.Link href="/Two">Two</reactBootstrap.Nav.Link>
                    <reactBootstrap.Nav.Link href="/Three">Three</reactBootstrap.Nav.Link>
                </reactBootstrap.Nav>
            </reactBootstrap.Navbar.Collapse>
        </reactBootstrap.Navbar>
    )
}

export default withRouter(Navigation);