import './App.css';
import Navigation from "./components/Navigation";
import Index from "./views/HomePage";
import AllGames from "./views/AllGames";
import React, { Fragment } from 'react';

import { Route, Switch } from "react-router-dom";

import  Login  from './views/Login'; 
import  SignUp  from './views/SignUp'; 


function App() {
  return (
    <Fragment>
      <div className="App">
        <div>
          <Navigation />
          <Route exact path="/" component={Index} />

          <Switch>
            {/* <Route exact path="/register" component={Register} />
            <Route exact path="/login" component={Login} />
            <Route exact path="/dashboard" component={Dashboard} /> */}
            <Route exact path="/games" component={AllGames} />
            <Route exact path="/login" component={Login} />
            <Route exact path="/signup" component={SignUp} />
            {/* <PrivateRoute exact path="/profile" component={Profile} />
            <PrivateRoute exact path="/about" component={About} /> */}
          </Switch>
        </div>
      </div>
    </Fragment>
  );
}

export default App;
