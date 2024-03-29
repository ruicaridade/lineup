import React from "react";
import { BrowserRouter, Redirect, Route, Switch } from "react-router-dom";
import "./App.css";
import UserDetails from "./routes/UserDetails";
import Users from "./routes/Users";

function App() {
  return (
    <div className="container mx-auto">
      <BrowserRouter>
        <Switch>
          <Route path="/users/:id">
            <UserDetails />
          </Route>
          <Route path="/users">
            <Users />
          </Route>
          <Route path="/">
            <Redirect to="/users" />
          </Route>
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;
