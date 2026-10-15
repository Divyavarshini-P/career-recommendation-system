import "./../styles/Footer.css";

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-container">
        <p>
          © {new Date().getFullYear()} Career Recommendation System
        </p>

        <p>
          AI Powered Resume Analyzer & Career Recommendation
        </p>
      </div>
    </footer>
  );
}

export default Footer;