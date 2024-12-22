import { useState } from "react";
import "./TaskManagement.css";
import user from "../assets/Logo.png";
import { CiFilter } from "react-icons/ci";
import { TbFileExport } from "react-icons/tb";

const TaskManagement = () => {
  const [tasks, setTasks] = useState([
    { id: "Task#1", date: "12/12/24", priority: "A", status: "Done" },
    { id: "Task#2", date: "13/12/24", priority: "B", status: "not done" },
    { id: "Task#3", date: "14/12/24", priority: "C", status: "in progress" },
    { id: "Task#3", date: "14/12/24", priority: "B", status: "not done" },
    { id: "Task#3", date: "14/12/24", priority: "C", status: "in progress" },
    { id: "Task#3", date: "14/12/24", priority: "A", status: "Done" },
    { id: "Task#3", date: "14/12/24", priority: "A", status: "in progress" },
    { id: "Task#3", date: "14/12/24", priority: "B", status: "in progress" },
  ]);

  const [searchQuery, setSearchQuery] = useState("");
  const [filterOpen, setFilterOpen] = useState(false); // State to toggle filter dropdown
  const [selectedPriority, setSelectedPriority] = useState(""); // State for selected priority

  const handleSearchChange = (e) => setSearchQuery(e.target.value);
  const handleExport = () => alert("Exporting tasks...");
  const handleFilter = () => setFilterOpen(!filterOpen); // Toggle filter dropdown

  // Filtered tasks based on search and selected priority
  const filteredTasks = tasks.filter((task) => {
    const matchesSearch = task.id
      .toLowerCase()
      .includes(searchQuery.toLowerCase());
    const matchesPriority =
      selectedPriority === "" || task.priority === selectedPriority;
    return matchesSearch && matchesPriority;
  });

  const handlePriorityFilter = (priority) => {
    setSelectedPriority(priority);
    setFilterOpen(false); // Close the dropdown after selecting
  };

  return (
    <div
      style={{
        position: "fixed",
        right: 0,
        width: "calc(100vw - 256px)",
        overflow: "auto",
        height: "100vh",
      }}
    >
      <div
        className="task-management-container "
        style={{
          width: "100%",
        }}
      >
        <div className="user">
          <img src={user} alt="" />
          <p>user</p>
        </div>
        <hr className="separator" />
        <div className="controls">
          <h2>My Tasks</h2>
          <input
            type="text"
            placeholder="Search tasks..."
            value={searchQuery}
            onChange={handleSearchChange}
            className="search-bar"
          />
          <div className="filter-container">
            <button className="filter-icon" onClick={handleFilter}>
              <CiFilter className="filter" />
              <p>Filter</p>
            </button>
            {filterOpen && (
              <div className="filter-dropdown">
                <button onClick={() => handlePriorityFilter("")}>All</button>
                <button onClick={() => handlePriorityFilter("A")}>A</button>
                <button onClick={() => handlePriorityFilter("B")}>B</button>
                <button onClick={() => handlePriorityFilter("C")}>C</button>
              </div>
            )}
          </div>
          <button className="export-icon" onClick={handleExport}>
            <TbFileExport className="export" />
            <p>Export</p>
          </button>
        </div>
        <table className="task-table">
          <thead>
            <tr>
              <th></th>
              <th>Task ID</th>
              <th>Date</th>
              <th>Priority</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {filteredTasks.map((task, index) => (
              <tr key={index}>
                <td></td>
                <td>{task.id}</td>
                <td>{task.date}</td>
                <td>{task.priority}</td>
                <td>
                  <select
                    className={`select ${task.status}`}
                    name="status"
                    id="status"
                    defaultValue={task.status}
                    onChange={(e) => {
                      setTasks((prev) => {
                        prev[index].status = e.target.value;
                        const arr = [...prev];
                        return arr;
                      });
                    }}
                  >
                    <option value="inprogress">In progress</option>
                    <option value="notdone">Not done</option>
                    <option value="Done">Done</option>
                  </select>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default TaskManagement;
