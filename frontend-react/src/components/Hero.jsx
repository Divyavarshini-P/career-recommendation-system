import "./../styles/Hero.css";

function Hero() {
  return (
    <section className="hero">

      <div className="hero-content">

        <h1>
          AI Resume Analyzer &
          <span> Career Recommendation</span>
        </h1>

        <p>
          Analyze resumes, compare with job descriptions,
          identify skill gaps, receive AI-powered career
          recommendations and improve your resume instantly.
        </p>

        <a href="#analyze">
          <button className="hero-btn">
            Get Started
          </button>
        </a>

      </div>

    </section>
  );
}

export default Hero;