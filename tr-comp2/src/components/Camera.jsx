import React from "react";
import "./camera.css";
import rectangle from "../assets/Rectangle.png";
const Camera = () => {
  return (
    <div className="camera-card">
      <h1>Camera</h1>
      <div className="select-container">
        <p className="define">Scan-type</p>
        <select>
          <option value="">CHEECK-IN</option>
        </select>
        <p className="define">Connected vidio device</p>

        <select>
          <option value="">SONY HPL100</option>
        </select>
        <p className="define">Quality</p>
        <select>
          <option value="">1080p</option>
        </select>
      </div>
      <button className="action-button">Scan</button>
      <img src={rectangle} alt="" />
    </div>
  );
};

export default Camera;
