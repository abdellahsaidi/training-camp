import React from "react";
import "./HeaderFr2.css";

const HeaderFr2 = ({ name = "Guest User" }) => {
  return (
    <div className="header-container">
      <div className="header-left">
        <h2>Most Recent Leave</h2>
        <p>{name}</p>
      </div>
      <div className="header-right">
        <div className="headuserhead-icon"></div>
        <span>{name}</span>
      </div>
    </div>
  );
};

export default HeaderFr2;
