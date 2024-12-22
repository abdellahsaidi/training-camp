import { FaCamera } from "react-icons/fa"; // Font Awesome icons
import { MdManageAccounts } from "react-icons/md"; // Material Design icons
import { IoIosInformationCircleOutline, IoMdLogOut } from "react-icons/io"; // Ionicons
import { IoSettingsOutline } from "react-icons/io5"; // Ionicons v5
import { AiOutlineDashboard } from "react-icons/ai"; // Ant Design icons
import { GoTasklist } from "react-icons/go"; // GitHub Octicons
import { LuFileClock } from "react-icons/lu"; // Lucide icons
import "./Sidebar.css";
import { FaFileSignature } from "react-icons/fa";

import logo from "../Assets/logo.png";

const Sidebar = () => {
  return (
    <div className="sidebar">
      <div className="sidebar-content">
        <a href="/">
          <img src={logo} alt="Logo" className="sidebar-logo" />
        </a>
        <ul className="sidebar-menu">
          <li>
            <p>
              <AiOutlineDashboard className="sidebar-icon" /> Dashboard
            </p>
          </li>
          <li>
            <p>
              <GoTasklist className="sidebar-icon" /> Tasks
            </p>
          </li>
          <li>
            <p>
              <LuFileClock className="sidebar-icon" /> Leave Request
            </p>
          </li>
          <li>
            <p>
              <FaFileSignature className="sidebar-icon" /> Abscence
            </p>
          </li>
        </ul>
      </div>

      <div className="sidebar-footer">
        <div className="sidebar-divider"></div>
        <ul>
          <li>
            <p className="sidebar-pfoot">
              <IoIosInformationCircleOutline className="icon" /> Help
            </p>
          </li>
          <li>
            <p className="sidebar-pfoot">
              <IoSettingsOutline className="icon" /> Settings
            </p>
          </li>
          <li>
            <p className="sidebar-logout">
              <IoMdLogOut className="icon" /> Log Out
            </p>
          </li>
        </ul>
      </div>
    </div>
  );
};

export default Sidebar;
