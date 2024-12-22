import React from "react";
import { FaCamera } from "react-icons/fa";
import { MdManageAccounts } from "react-icons/md";
import { IoIosInformationCircleOutline, IoMdLogOut } from "react-icons/io";
import { IoSettingsOutline } from "react-icons/io5";
import "./Sidebar.css";
import logo from "../Assets/logo.png";


const Sidebar = () => {
  return (
    <div className="sidebar">
      <div className="sidecontent">
        <a href="">
          <img src={logo} alt="Logo" className="sidebar-logo" />
        </a>
        <ul>
          <li>
            <p>
              <FaCamera /> Camera Scan
            </p>
          </li>
          <li>
            <p>
              <MdManageAccounts /> Manage Account
            </p>
          </li>
        </ul>
      </div>

      <div className="sidefooter">
        <div className="divider"></div>
        <ul>
          <li>
            <p className="pfoot">
              <IoIosInformationCircleOutline /> Help
            </p>
          </li>
          <li>
            <p className="pfoot">
              <IoSettingsOutline /> Settings
            </p>
          </li>
          <li>
            <p className="logout">
              <IoMdLogOut /> Log Out
            </p>
          </li>
        </ul>
      </div>
    </div>
  );
};

export default Sidebar;
