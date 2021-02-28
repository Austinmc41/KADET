import React, { Component } from "react";
import { Router, Switch, Route } from "react-router-dom";

import Home from "./components/Home";
import Settings from "./components/settings.component";
import Criteria from "./components/criterion.component";
import One from "./components/one";
import Two from "./components/two";
import Three from "./components/three";
import NotFound from "./components/NotFound";
import history from './history';

export default class Routes extends Component {
    render() {
        return (
            <Router history={history}>
                <Switch>
                    <Route path="/" exact component={Home} />
                    <Route path="/Settings" component={Settings} />
                    <Route path="/Rotations" component={Criteria} />
                    <Route path="/One" component={One} />
                    <Route path="/Two" component={Two} />
                    <Route path="/Three" component={Three} />
                    <Route>
                        <NotFound />
                    </Route>
                </Switch>
            </Router>
        )
    }
}