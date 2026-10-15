function About() {

  return (
    <section className="about-section">

      <h1>About CareerAI</h1>

      <p>
        CareerAI is an AI-powered career recommendation
        system designed to help students and job seekers
        understand their career opportunities.
      </p>

      <div className="about-grid">

        <div className="about-card">
          <h3>📄 Resume Analysis</h3>
          <p>
            Analyze resume content and extract important skills.
          </p>
        </div>

        <div className="about-card">
          <h3>🎯 ATS Score</h3>
          <p>
            Evaluate resume compatibility using an ATS scoring system.
          </p>
        </div>

        <div className="about-card">
          <h3>💼 Career Recommendation</h3>
          <p>
            Recommend suitable careers based on your skills.
          </p>
        </div>

        <div className="about-card">
          <h3>📊 Skill Gap Analysis</h3>
          <p>
            Identify skills you need to develop for your target career.
          </p>
        </div>

      </div>

    </section>
  );
}

export default About;