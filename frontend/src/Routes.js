import React, { Component } from "react";
import { Router, Switch, Route } from "react-router-dom";

import Home from "./components/Home";
import Settings from "./components/settings.component";
import Criteria from "./components/criterion.component";
import ListRequests from "./components/view_requests.component";
import NotFound from "./components/NotFound";
import history from './history';
import run_scheduler from "./components/run_scheduler";

export default class Routes extends Component {
    render() {
        return (
            <Router history={history}>
                <Switch>
                    <Route path="/" exact component={Home} />
                    <Route path="/Settings" component={Settings} />
                    <Route path="/Rotations" component={Criteria} />
                    <Route path="/view_requests" component={ListRequests} />
                    <Route path="/run_scheduler" component={run_scheduler} />
                    <Route>
                        <NotFound />
                    </Route>
                </Switch>
            </Router>
        )
    }
}