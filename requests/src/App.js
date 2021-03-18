import React, { Component} from "react";
import * as reactBootstrap from 'react-bootstrap';
import { Switch, Route } from "react-router-dom";
import Login from "./components/login";
import Register from "./components/register";
import NotFound from "./components/NotFound";

const Navigation = (props) => {
  console.log(props);
  return (
    <reactBootstrap.Navbar bg="primary" variant="dark">
      <reactBootstrap.Navbar.Brand href="#home">Requester</reactBootstrap.Navbar.Brand>
      <reactBootstrap.Navbar.Toggle aria-controls="basic-navbar-nav" />
      <reactBootstrap.Navbar.Collapse id="basic-navbar-nav">
        <reactBootstrap.Nav className="mr-auto">
          <reactBootstrap.Nav.Link href="/">Home</reactBootstrap.Nav.Link>
          <reactBootstrap.Nav.Link href="/login/">Login</reactBootstrap.Nav.Link>
          <reactBootstrap.Nav.Link href="/register/">Register</reactBootstrap.Nav.Link>
        </reactBootstrap.Nav>
      </reactBootstrap.Navbar.Collapse>
    </reactBootstrap.Navbar>
  )
}

class App extends Component {
  render() {
    return (
      <div className="App">
        <Navigation />
        <h1 className="text-uppercase text-center my-4">Requester app</h1>
        <Switch>
          <Route exact path={"/"} render={() => <div>Temp home page</div>}/>
          <Route path="/login/" component={Login} />
          <Route path="/register/" component={Register} />
          <Route>
            <NotFound />
          </Route>
        </Switch>
      </div>
    );
  }
}

export default App;