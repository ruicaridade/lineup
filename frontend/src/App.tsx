import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import "./App.css";

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/users">
          <h1>Users</h1>
        </Route>
        <Route path="/">
          <h1>Index</h1>
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
