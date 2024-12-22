import React from "react";
import "./AbsenceInfo.css";

export default function AbsenceInfo({
  fullName,
  age,
  gender,
  occ,
  location,
  dateDepo,
}) {
  return (
    <div className="absh-body">
      <div className="abs-body">
        <div className="Info-Card-Abs">
          <div className="abs-general-info">
            <img src="profile.jpg" alt="Profile Picture" />
            <div>
              <h3>{fullName}</h3>
              <span>
                {age} / {gender}
              </span>
            </div>
          </div>
          <div>
            <div>
              <label>Age:</label> {age} y.o.
            </div>
            <div>
              <label>Name:</label> {fullName}
            </div>
            <div>
              <label>Occupation:</label> {occ}
            </div>
            <div>
              <label>Location:</label> {location}
            </div>
          </div>
        </div>
        <div className="text-card">
          <p>
            Emmelie is a traditional book-worm and has always been from a young
            age. She is a housekeeper mom with two kids and has a lot of time to
            read and relax.
          </p>
          <small>{dateDepo} hours ago</small>
        </div>
      </div>
      <div className="bouttons">
        <button className="accept-abs">Approve</button>
        <button className="decline-abs">Decline</button>
      </div>
    </div>
  );
}
