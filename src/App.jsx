import React from "react";
import Sidebar from "./components/Sidebar";
import Header from "./components/Header";
import FormContainer from "./components/FormContainer";
import "./App.css";

const App = () => {
  return (
    <div className="app">
      <Sidebar />
      <div className="main-content">
        <Header />
        <FormContainer />
      </div>
    </div>
  );
};

export default App;
