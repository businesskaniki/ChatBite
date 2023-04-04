import { NavLink } from 'react-router-dom';
import { FaHome, FaUserFriends, FaBriefcase, FaCommentAlt, FaBell, FaUser } from 'react-icons/fa';
import './nav.css'

function Navbar() {
  return (
    <nav>
      <ul>
        <li>
          <NavLink exact to="/" activeClassName="active">
            <FaHome className="icon" />
            <span>posts</span>
          </NavLink>
        </li>
        <li>
          <NavLink to="/network" activeClassName="active">
            <FaUserFriends className="icon" />
            <span>Friends</span>
          </NavLink>
        </li>
        <li>
          <NavLink to="/jobs" activeClassName="active">
            <FaBriefcase className="icon" />
            <span></span>
          </NavLink>
        </li>
        <li>
          <NavLink to="/messaging" activeClassName="active">
            <FaCommentAlt className="icon" />
            <span>Messaging</span>
          </NavLink>
        </li>
        <li>
          <NavLink to="/notifications" activeClassName="active">
            <FaBell className="icon" />
            <span>Notifications</span>
          </NavLink>
        </li>
        <li>
          <NavLink to="/me" activeClassName="active">
            <FaUser className="icon" />
            <span>Me</span>
          </NavLink>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;
