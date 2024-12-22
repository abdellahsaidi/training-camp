import React from "react";
import "./LeaveHis.css";

const LeaveHis = () => {
  const leaves = [
    {
      date: "02/11/2023",
      duration: "06 Days",
      reason: "Sickness",
      status: "Approved",
    },
    {
      date: "14/03/2024",
      duration: "19 Days",
      reason: "Sickness",
      status: "Approved",
    },
    {
      date: "23/07/2024",
      duration: "07 Days",
      reason: "Vacation",
      status: "Refused",
    },
  ];

  const statusClassMap = {
    Approved: "status-approved",
    Refused: "status-refused",
  };

  return (
    <div className="leave-history-container">
      <h2 className="leave-history-title">History of Leaves</h2>
      <table className="leave-history-table">
        <thead>
          <tr>
            <th>Date</th>
            <th>Duration</th>
            <th>Reason</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {leaves.map((leave, index) => (
            <tr key={index}>
              <td>{leave.date}</td>
              <td>{leave.duration}</td>
              <td>{leave.reason}</td>
              <td>
                <span
                  className={statusClassMap[leave.status] || "status-default"}
                >
                  {leave.status}
                </span>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default LeaveHis;
