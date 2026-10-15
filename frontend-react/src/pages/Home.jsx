import { useNavigate } from "react-router-dom";

function Home() {

  const navigate = useNavigate();

  return (
    <section className="home-section">

      <div className="home-content">

        <h1>
          AI Career Recommendation System
        </h1>

        <p>
          Analyze your resume, discover your skill gaps,
          calculate your ATS score, and find the best
          career opportunities for you.
        </p>

        <button
          onClick={() => navigate("/analyze")}
          className="home-button"
        >
          🚀 Analyze My Resume
        </button>

      </div>

    </section>
  );
}

export default Home;