import React, { useState } from "react";
import "./Header.css";

const Header = () => {
  const [dropdownVisible, setDropdownVisible] = useState(false);

  const toggleDropdown = () => {
    setDropdownVisible(!dropdownVisible);
  };

  return (
    <header className="header">
      <div className="user-profile" onClick={toggleDropdown}>
        <div className="user-icon"></div>
        <span>User</span>
        <div className={`dropdown-menu ${dropdownVisible ? "visible" : ""}`}>
          <ul>
            <li>Profile</li>
            <li>Settings</li>
            <li>Logout</li>
          </ul>
        </div>
      </div>
    </header>
  );
};

export default Header;
