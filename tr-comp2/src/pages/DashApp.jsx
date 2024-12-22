import React from "react";
import Sidebar from "../components/Sidebar";
import HeaderFrame from "../components/HeaderFrame";
import "./App.css";

const DashApp = () => {
  return (
    <div className="headerframe">
      <Sidebar />
      <div className="main-content">
        <HeaderFrame />
      </div>
    </div>
  );
};

export default DashApp;
