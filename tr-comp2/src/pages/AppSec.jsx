// AbsenceInfo.js
import React from "react";

function AbsenceInfo({ fullName, age, gender, occ, location, dateDepo }) {
  return (
    <div className="absence-info">
      <h1>Absence Information</h1>
      <p>
        <strong>Full Name:</strong> {fullName}
      </p>
      <p>
        <strong>Age:</strong> {age}
      </p>
      <p>
        <strong>Gender:</strong> {gender}
      </p>
      <p>
        <strong>Occupation:</strong> {occ}
      </p>
      <p>
        <strong>Location:</strong> {location}
      </p>
      <p>
        <strong>Date of Departure:</strong> {dateDepo}
      </p>
    </div>
  );
}

export default AbsenceInfo;
