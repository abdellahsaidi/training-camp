import React from "react";
import Sidebar from "../components/Sidebar";
import HeaderFrame from "../components/HeaderFrame";
import GrapheFrame from "../components/GrapheFrame";
import Tasks from "../components/Tasks";
import "./Static.css"; // Optional for overall styling

const StaticPage = () => {
  // Sample data for props
  const absence = 5;
  const absencejs = 2;
  const workingdays = 200;
  const numTasks = 50;
  const percent = 80;
  const unit = 350;
  const worker = 10;
  const delay = 15;

  return (
    <div className="statapp-container">
      <Sidebar />
      <div className="statmain-content">
        <HeaderFrame className="statheaderframe"
          absence={absence}
          absencejs={absencejs}
          workingdays={workingdays}
        />
        <div className="statframe-task">
          <GrapheFrame
            numTasks={numTasks}
            percent={percent}
            unit={unit}
            worker={worker}
            delay={delay}
          />
          <Tasks />
        </div>
      </div>
    </div>
  );
};

export default StaticPage;
