import React from "react";
import Header from "./components/Header";
import "./formApp2.css";
import Sidebar2 from "../components/Sidebar2";
import FormContainer2 from "../components/FormContainer2";

const FormApp = () => {
  return (
    <div className="app">
      <Sidebar2 />
      <div className="main-content">
        <Header />
        <FormContainer2 />
      </div>
    </div>
  );
};

export default FormApp;
