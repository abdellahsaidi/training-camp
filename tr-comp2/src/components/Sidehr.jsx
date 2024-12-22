import { AiFillDashboard } from "react-icons/ai";
import { FaFileSignature } from "react-icons/fa";
import { FaFileCircleExclamation } from "react-icons/fa6";
import { IoIosInformationCircleOutline } from "react-icons/io";
import { IoSettingsOutline } from "react-icons/io5";
import { FaFileExport } from "react-icons/fa6";
import { IoMdLogOut } from "react-icons/io";
import "./Sidebarr.css";
import logo from "../Assets/logo.png";

const Sidebar = () => {
  return (
    <div className="sidebar">
      <div className="sidecontent">
        <a href="">
          <div className="logoside">
            <img src={logo} alt="Logo" className="sidebar-logo" />
            <h3>DashaRHi</h3>
          </div>
        </a>
        <ul>
          <li>
            <p>
              <AiFillDashboard /> Dashboard
            </p>
          </li>
          <li>
            <p>
              <FaFileSignature /> Employees List
            </p>
          </li>
          <li>
            <p>
              <FaFileCircleExclamation /> Leave request
            </p>
          </li>
          <li>
            <p>
              <FaFileExport /> Absences
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
