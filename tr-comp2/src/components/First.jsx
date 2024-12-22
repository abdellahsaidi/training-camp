import React from "react";
import "./first.css";
import logo from "../Assets/logo.png";

const First = () => {
  return (
    <div className="intro">
      <div className="text-content">
        <h3>Welcome back, User</h3>
        <p>
          Empower Your Factory, Optimize Every Operation: Real-Time Insights for
          Smarter Manufacturing
        </p>
        <h4>Check-in/out Scan</h4>
      </div>
      <img src={logo} alt="Logo" className="logo" />
      <p className="user">User</p>
    </div>
  );
};

export default First;
