import React from "react";
import { GoRocket } from "react-icons/go";
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import "./GrapheFrame.css";

// Register the required Chart.js components
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const GrapheFrame = ({ numTasks, percent, unit, worker, delay }) => {
  // Sample data for the graph
  const data = {
    labels: ["1-Dec", "5-Dec", "10-Dec"], // X-axis labels
    datasets: [
      {
        label: "Task Progress",
        data: [5, 20, 50], // Y-axis values aligned with labels
        borderColor: "#4caf50",
        backgroundColor: "rgba(76, 175, 80, 0.2)",
        tension: 0.4,
      },
    ],
  };

  // Chart options
  const options = {
    responsive: true,
    plugins: {
      legend: {
        display: true,
        position: "top",
      },
      title: {
        display: true,
        text: "Task Progress Over Time",
      },
    },
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  };

  // Conditional style
  const spanStyle = {
    fontSize: "10px",
    color: percent >= 0 ? "#14CA74" : "red",
    backgroundColor: percent >= 0 ? "#05C16833" : "pink",
    borderRadius: "10px",
    padding: "5px",
    margin: "0",
  };

  return (
    <div className="gr-production-overview">
      <h4>
        <GoRocket />
        Production Overview
      </h4>
      <p>Total Tasks Accomplished</p>
      <h6>
        {numTasks} <span style={spanStyle}>{percent}%</span>
      </h6>
      <div style={{ width: "100%", maxWidth: "600px", margin: "0 auto" }}>
        <Line data={data} options={options} />
      </div>
      <div className="gr-foot">
        <div>
          <h5>Unit Produced</h5>
          <p>{unit}/400</p>
        </div>
        <div class="gr-vl"></div>
        <div>
          <h5>Worker</h5>
          <p>{worker}</p>
        </div>
        <div class="gr-vl"></div>
        <div>
          <h5>Bottlenecks</h5>
          <p>AGV route issue flagged</p>
        </div>
        <div class="gr-vl"></div>
        <div>
          <h5>Delays</h5>
          <p>
            Time: {delay} {delay === 1 ? "minute" : "minutes"}
          </p>
        </div>
      </div>
    </div>
  );
};

export default GrapheFrame;
