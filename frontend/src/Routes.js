import React, { Component } from "react";
import { Router, Switch, Route } from "react-router-dom";

import App from "./Scheduler/App";
import Criteria from "./components/criterion.component";
import One from "./components/one";
import Home from "./Home/Home";
import history from './history';

export default class Routes extends Component {
    render() {
        return (
            <Router history={history}>
                <Switch>
                    <Route path="/" exact component={Home} />
                    <Route path="/Rotations" component={Criteria} />
                    <Route path="/One" component={One} />
                </Switch>
            </Router>
        )
    }
}