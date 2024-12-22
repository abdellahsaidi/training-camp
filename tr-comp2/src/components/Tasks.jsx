import React, { useState } from "react";
import "./Tasks.css";

export default function Tasks() {
  const [tasks, setTasks] = useState([
    { id: 1, name: "Training", completed: false },
    { id: 2, name: "Progress Supervision", completed: false },
    { id: 3, name: "Data Analysis", completed: false },
    { id: 4, name: "Budgeting", completed: false },
    { id: 5, name: "Scheduling", completed: false },
    { id: 6, name: "Problem Solving", completed: false },
    { id: 7, name: "Documentation", completed: false },
    { id: 8, name: "Back up and restore", completed: false },
    { id: 9, name: "Implementing Data", completed: false },
  ]);

  const toggleTaskCompletion = (id) => {
    setTasks((prevTasks) =>
      prevTasks.map((task) =>
        task.id === id ? { ...task, completed: !task.completed } : task
      )
    );
  };

  return (
    <div className="task-container">
      <h3>Important Tasks!</h3>
      <ul className="task-list">
        {tasks.map((task) => (
          <li
            key={task.id}
            className={`task-item ${task.completed ? "completed" : ""}`}
          >
            <label className="task-label" htmlFor={`task-${task.id}`}>
              <input
                type="checkbox"
                id={`task-${task.id}`}
                checked={task.completed}
                onChange={() => toggleTaskCompletion(task.id)}
              />
              <span className="task-name">{task.name}</span>
            </label>
          </li>
        ))}
      </ul>
    </div>
  );
}
