import React from "react";
import "../App.css";
import LeaveHis from "../components/LeaveHis";
import HeaderFr2 from "../components/HeaderFr2";
import Sidebar from "../components/Sidebar";
import AbsenceInfo from "../components/AbsenceInfo";
import "./Absence.css";

const Absence = () => {
  const absenceData = {
    fullName: "James Gustavsson",
    age: 23,
    gender: "Male",
    occ: "Accountant",
    location: "Himmel",
    dateDepo: "2023-12-21",
  };

  const userName = "James Gustavsson";

  const leaveHistory = [
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

  return (
    <div className="absApp">
      <Sidebar />
      <div className="absMain">
        <HeaderFr2 name={userName} />
        <AbsenceInfo {...absenceData} />
        <LeaveHis leaves={leaveHistory} />
      </div>
    </div>
  );
};

export default Absence;
