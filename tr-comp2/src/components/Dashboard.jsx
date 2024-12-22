import React from "react";
import "./Dashboard.css";
import { BsThreeDots } from "react-icons/bs";

const Dashboard = () => {
  return (
    <div className="dashboard-container">
      <div className="dashheader">
        Welcome back, User <br />
        <h6>
          <p>
            Empower Your Work, Enhance Productivity: Real-Time Insights for
            Smarter Performance Management
          </p>
        </h6>
      </div>
      <div className="dashstats">
        <div className="dashstat-box">
          <div className="dashunder">
            <p>Working Days</p>
            <a href="">
              <BsThreeDots />
            </a>
          </div>
          <h3>
            257/ <small>365</small>
          </h3>
        </div>
        <div class="dashstat-box">
          <div className="dashunder">
            <p>Tasks Completed This Month</p>
            <a href="#">
              <BsThreeDots />
            </a>
          </div>
          <h3>
            257/ <small>365</small>
          </h3>
        </div>
        <div class="dashstat-box">
          <div className="dashunder">
            <p>Absence Days</p>
            <a href="#">
              <BsThreeDots />
            </a>
          </div>
          <h3>
            10/ <small>30</small>
          </h3>
        </div>
        <div class="dashstat-box">
          <div className="dashunder">
            <p>Justified Absence Days</p>
            <a href="#">
              <BsThreeDots />
            </a>
          </div>
          <h3>
            5/ <small>10</small>
          </h3>
        </div>
      </div>
      <div className="dashmain-content">
        <div className="dashunder">
          <div className="dashproduction-overview">Production Overview</div>
          <div className="dashimportant-tasks">Important Tasks</div>
        </div>
        <div className="dashoverview">Overview</div>
      </div>
    </div>
  );
};

export default Dashboard;
