import { FaCamera } from "react-icons/fa";
import { MdManageAccounts } from "react-icons/md";
import { IoIosInformationCircleOutline, IoMdLogOut } from "react-icons/io";
import { IoSettingsOutline } from "react-icons/io5";
import "./Sidebarr.css";
import logo from "../Assets/logo.png";

const Sidebarr = () => {
  return (
    <div className="sidebar">
      <div className="sidecontent">
        <a href="">
          <div className="logoside">
            <img src={logo} alt="Logo" className="sidebar-logo" />
            <h3>DashaRHi</h3>
          </div>{" "}
        </a>
        <ul>
          <li>
            <p>
              <FaCamera /> Camer Scan
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

export default Sidebarr;
