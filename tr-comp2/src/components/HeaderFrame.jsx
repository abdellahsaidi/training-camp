import React from "react";
import "./HeaderFrame.css";
import { BsThreeDots } from "react-icons/bs";

const HeaderFrame = ({ absence = 0, absencejs = 0, workingdays = 0 }) => {
  return (
    <div className="header-container">
      <div className="profile-section">
        <div className="profile-icon"></div>
        <span>User</span>
      </div>
      <div className="welcome-section">
        <h2>Welcome back, User</h2>
        <p className="welcome-message">
          Empower Your Work, Enhance Productivity: Real-Time Insights for
          Smarter Performance Management
        </p>
      </div>
      <div className="stats-section">
        <div className="stat-box">
          <div className="stat-header">
            <p>Working Days</p>
            <a href="#" aria-label="More options">
              <BsThreeDots />
            </a>
          </div>
          <h3>
            {workingdays} / <small>365</small>
          </h3>
        </div>
        <div className="stat-box">
          <div className="stat-header">
            <p>Tasks Completed This Month</p>
            <a href="#" aria-label="More options">
              <BsThreeDots />
            </a>
          </div>
          <h3>
            {workingdays} / <small>365</small>
          </h3>
        </div>
        <div className="stat-box">
          <div className="stat-header">
            <p>Absence Days</p>
            <a href="#" aria-label="More options">
              <BsThreeDots />
            </a>
          </div>
          <h3>
            {absence} / <small>30</small>
          </h3>
        </div>
        <div className="stat-box">
          <div className="stat-header">
            <p>Justified Absence Days</p>
            <a href="#" aria-label="More options">
              <BsThreeDots />
            </a>
          </div>
          <h3>
            {absencejs} / <small>10</small>
          </h3>
        </div>
      </div>
    </div>
  );
};

export default HeaderFrame;
