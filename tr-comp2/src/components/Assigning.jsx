import React, { useState } from "react";
import "./Assigning.css";

const Assigning = ({ user }) => {
  // State management for task and employee details
  const [taskDetails, setTaskDetails] = useState({
    taskName: "",
    department: "",
    description: "",
    startDate: "",
    deadline: "",
  });

  const [employeeDetails, setEmployeeDetails] = useState({
    name: "",
    surname: "",
    message: "",
  });

  const handleTaskChange = (e) => {
    const { name, value } = e.target;
    setTaskDetails((prev) => ({ ...prev, [name]: value }));
  };

  const handleEmployeeChange = (e) => {
    const { name, value } = e.target;
    setEmployeeDetails((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Task Details:", taskDetails);
    console.log("Employee Details:", employeeDetails);
    alert("Task assigned successfully!");
  };

  return (
    <div className="form-container">
      <header>
        <h1>Assigning a new task</h1>
        <div className="user-profile">
          <span>{user}</span>
          <div className="user-icon"></div>
        </div>
      </header>
      <div className="form-wrapper">
        <form className="task-form" onSubmit={handleSubmit}>
          <h2>Task Details</h2>
          <label>
            Task Name
            <input
              type="text"
              name="taskName"
              placeholder="Task's Name"
              value={taskDetails.taskName}
              onChange={handleTaskChange}
            />
          </label>
          <label>
            Employee's Department
            <select
              name="department"
              value={taskDetails.department}
              onChange={handleTaskChange}
            >
              <option value="">Employee's Department</option>
              <option value="HR">HR</option>
              <option value="IT">IT</option>
              <option value="Sales">Sales</option>
            </select>
          </label>
          <label>
            Task Description
            <textarea
              name="description"
              placeholder="Enter Description Here"
              value={taskDetails.description}
              onChange={handleTaskChange}
            ></textarea>
          </label>
          <label>
            Starting Date
            <input
              type="date"
              name="startDate"
              value={taskDetails.startDate}
              onChange={handleTaskChange}
            />
          </label>
          <label>
            Deadline
            <input
              type="date"
              name="deadline"
              value={taskDetails.deadline}
              onChange={handleTaskChange}
            />
          </label>
        </form>

        <form className="employee-form">
          <h2>Employee Details</h2>
          <label>
            Name
            <input
              type="text"
              name="name"
              placeholder="Employee's Name"
              value={employeeDetails.name}
              onChange={handleEmployeeChange}
            />
          </label>
          <label>
            Surname
            <input
              type="text"
              name="surname"
              placeholder="Employee's Surname"
              value={employeeDetails.surname}
              onChange={handleEmployeeChange}
            />
          </label>
          <label>
            Message
            <textarea
              name="message"
              placeholder="Enter Message Here"
              value={employeeDetails.message}
              onChange={handleEmployeeChange}
            ></textarea>
          </label>
        </form>
      </div>
      <div className="action-button">
        <button onClick={handleSubmit}>Add Task</button>
      </div>
    </div>
  );
};

export default Assigning;
