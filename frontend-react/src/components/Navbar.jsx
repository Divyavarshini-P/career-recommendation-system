import { NavLink } from "react-router-dom";
import "../styles/Navbar.css";

function Navbar() {
  return (
    <nav className="navbar">

      <div className="logo">
        CareerAI
      </div>

      <div className="nav-links">

        <NavLink to="/">
          Home
        </NavLink>

        <NavLink to="/analyze">
          Analyze
        </NavLink>

        <NavLink to="/results">
          Results
        </NavLink>

        <NavLink to="/about">
          About
        </NavLink>

      </div>

    </nav>
  );
}

export default Navbar;