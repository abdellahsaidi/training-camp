import { useState } from "react";
import "./TaskManagement.css";
import user from "../assets/Logo.png";
import { CiFilter } from "react-icons/ci";
import { TbFileExport } from "react-icons/tb";
import { CiCirclePlus } from "react-icons/ci";

const Taskhr = () => {
  const [tasks, setTasks] = useState([
    {
      employee: "Nadjah Lamis",
      duration: "6 days",
      departement: "Finance",
      decesion: "Approved",
    },
    {
      employee: "Ben Ahmed Hichem",
      duration: "19 days",
      departement: "Finance",
      decesion: "Approved",
    },
    {
      employee: "Zerouali Salma",
      duration: "7 days",
      departement: "Sales",
      decesion: "Refused",
    },
    {
      employee: "Hamdani Amine",
      duration: "20 days",
      departement: "Finance",
      decesion: "Approved",
    },
  ]);

  const [searchQuery, setSearchQuery] = useState("");
  const [filterOpen, setFilterOpen] = useState(false);
  const [selectedDepartment, setSelectedDepartment] = useState("");

  const handleSearchChange = (e) => setSearchQuery(e.target.value);
  const handleExport = () => alert("Exporting tasks...");
  const handleFilter = () => setFilterOpen(!filterOpen);

  // Filter tasks based on search query and selected department
  const filteredTasks = tasks.filter((task) => {
    const matchesSearch = task.employee
      .toLowerCase()
      .includes(searchQuery.toLowerCase());
    const matchesDepartment =
      selectedDepartment === "" || task.departement === selectedDepartment;
    return matchesSearch && matchesDepartment;
  });

  const handleDepartmentFilter = (department) => {
    setSelectedDepartment(department);
    setFilterOpen(false); // Close dropdown after selecting
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
        className="task-management-container"
        style={{
          width: "100%",
        }}
      >
        <div className="user">
          <img src={user} alt="User logo" />
          <p>User</p>
        </div>
        <hr className="separator" />
        <div className="controls">
          <h2>Processing Leave Requests</h2>
          <input
            type="text"
            placeholder="Search by employee..."
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
                <button onClick={() => handleDepartmentFilter("")}>All</button>
                <button onClick={() => handleDepartmentFilter("Finance")}>
                  Finance
                </button>
                <button onClick={() => handleDepartmentFilter("Marketing")}>
                  Marketing
                </button>
                <button onClick={() => handleDepartmentFilter("Sales")}>
                  Sales
                </button>
                <button onClick={() => handleDepartmentFilter("Research")}>
                  Research
                </button>
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
              <th>Employee</th>
              <th>Duration</th>
              <th>Departement</th>
              <th>Decision</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            {filteredTasks.map((task, index) => (
              <tr key={index}>
                <td>{task.employee}</td>
                <td>{task.duration}</td>
                <td>{task.departement}</td>
                <td
                  style={{
                    color: task.decesion === "Approved" ? "green" : "red",
                  }}
                >
                  {task.decesion}
                </td>
                <td>
                  <input
                    style={{
                      color: "white",
                      height: "30px",
                      width: "110px",
                      background: "#7A5CFA",
                      borderRadius: "6px",
                      border: "none",
                    }}
                    type="submit"
                    className="view-more-btn"
                    value={"view more"}
                    onClick={() => alert(`Viewing more about ${task.employee}`)}
                  ></input>
                  <CiCirclePlus
                    style={{
                      marginLeft: "-15px",
                      marginBottom: "-4px",
                    }}
                  />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Taskhr;
