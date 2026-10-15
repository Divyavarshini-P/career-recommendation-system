import React from "react";
import "../styles/ResultCard.css";
function ResultCard({ result }) {
  if (!result) {
    return (
      <div className="result-empty">
        <h2>📊 Analysis Results</h2>
        <p>No analysis available yet.</p>
        <p>Please analyze your resume first.</p>
      </div>
    );
  }

  const {
    match_score = 0,
    ats_score = 0,
    ats_rating = "Needs Improvement",
    ats_breakdown = {},
    matched_skills = [],
    missing_skills = [],
    recommended_roles = [],
    feedback = [],
  } = result;

  const contactInformation =
    ats_breakdown.contact_information || 0;

  const resumeStructure =
    ats_breakdown.resume_structure || 0;

  const resumeLength =
    ats_breakdown.resume_length || 0;

  const skillMatch =
    ats_breakdown.skill_match || 0;


  // -----------------------------------------
  // Rating class
  // -----------------------------------------

  const getRatingClass = () => {
    const rating = ats_rating.toLowerCase();

    if (rating === "excellent") {
      return "rating-excellent";
    }

    if (rating === "very good") {
      return "rating-very-good";
    }

    if (rating === "good") {
      return "rating-good";
    }

    if (rating === "average") {
      return "rating-average";
    }

    return "rating-needs-improvement";
  };


  // -----------------------------------------
  // Progress percentage
  // -----------------------------------------

  const getPercentage = (value, maximum) => {
    return Math.min(
      Math.round((value / maximum) * 100),
      100
    );
  };


  return (
    <div className="results-container">

      {/* =====================================================
          PAGE TITLE
      ===================================================== */}

      <div className="results-title">
        <h1>📊 AI Resume Analysis</h1>

        <p>
          Resume compatibility, ATS evaluation,
          skill analysis and career recommendations
        </p>
      </div>


      {/* =====================================================
          TOP SCORE CARDS
      ===================================================== */}

      <div className="score-grid">

        {/* Match Score */}

        <div className="score-card match-card">

          <div className="score-icon">
            🎯
          </div>

          <div className="score-content">

            <h3>Match Score</h3>

            <div className="score-number">
              {Number(match_score).toFixed(1)}%
            </div>

            <p>
              Resume compatibility with the job description
            </p>

          </div>

        </div>


        {/* Skills Found */}

        <div className="score-card skills-found-card">

          <div className="score-icon">
            ✅
          </div>

          <div className="score-content">

            <h3>Skills Found</h3>

            <div className="score-number">
              {matched_skills.length}
            </div>

            <p>
              Skills matching the job requirements
            </p>

          </div>

        </div>


        {/* Missing Skills */}

        <div className="score-card missing-card">

          <div className="score-icon">
            ❌
          </div>

          <div className="score-content">

            <h3>Missing Skills</h3>

            <div className="score-number">
              {missing_skills.length}
            </div>

            <p>
              Skills to improve for this role
            </p>

          </div>

        </div>

      </div>


      {/* =====================================================
          ATS SCORE
      ===================================================== */}

      <section className="ats-card">

        <div className="ats-header">

          <div className="ats-title">

            <h2>
              🤖 ATS Resume Score
            </h2>

            <p>
              Resume compatibility with Applicant Tracking Systems
            </p>

          </div>


          {/* ATS Circle */}

          <div className="ats-score-circle">

            <div className="ats-score-number">
              {ats_score}
            </div>

            <div className="ats-score-total">
              /100
            </div>

          </div>

        </div>


        {/* ATS Rating */}

        <div className="ats-rating-box">

          <span>
            Resume Rating
          </span>

          <strong className={getRatingClass()}>
            {ats_rating}
          </strong>

        </div>


        {/* ATS Breakdown */}

        <div className="ats-breakdown">

          <h3>
            📊 ATS Score Breakdown
          </h3>


          {/* Contact */}

          <div className="ats-item">

            <div className="ats-item-header">

              <span>
                📇 Contact Information
              </span>

              <strong>
                {contactInformation}/25
              </strong>

            </div>

            <div className="ats-progress">

              <div
                className="ats-progress-fill"
                style={{
                  width: `${getPercentage(
                    contactInformation,
                    25
                  )}%`,
                }}
              />

            </div>

          </div>


          {/* Structure */}

          <div className="ats-item">

            <div className="ats-item-header">

              <span>
                📄 Resume Structure
              </span>

              <strong>
                {resumeStructure}/40
              </strong>

            </div>

            <div className="ats-progress">

              <div
                className="ats-progress-fill"
                style={{
                  width: `${getPercentage(
                    resumeStructure,
                    40
                  )}%`,
                }}
              />

            </div>

          </div>


          {/* Length */}

          <div className="ats-item">

            <div className="ats-item-header">

              <span>
                📏 Resume Length
              </span>

              <strong>
                {resumeLength}/10
              </strong>

            </div>

            <div className="ats-progress">

              <div
                className="ats-progress-fill"
                style={{
                  width: `${getPercentage(
                    resumeLength,
                    10
                  )}%`,
                }}
              />

            </div>

          </div>


          {/* Skill Match */}

          <div className="ats-item">

            <div className="ats-item-header">

              <span>
                🧠 Skill Match
              </span>

              <strong>
                {skillMatch}/25
              </strong>

            </div>

            <div className="ats-progress">

              <div
                className="ats-progress-fill"
                style={{
                  width: `${getPercentage(
                    skillMatch,
                    25
                  )}%`,
                }}
              />

            </div>

          </div>

        </div>

      </section>


      {/* =====================================================
          MATCHED SKILLS
      ===================================================== */}

      <section className="skills-section">

        <div className="skills-card matched-skills-card">

          <div className="section-heading">

            <h2>
              ✅ Matched Skills
            </h2>

            <span className="skill-count matched-count">
              {matched_skills.length}
            </span>

          </div>


          <div className="skill-list">

            {matched_skills.length > 0 ? (

              matched_skills.map((skill, index) => (

                <span
                  className="skill-pill matched-pill"
                  key={index}
                >
                  {skill}
                </span>

              ))

            ) : (

              <p className="no-skills">
                No matched skills found.
              </p>

            )}

          </div>

        </div>


        {/* Missing Skills */}

        <div className="skills-card missing-skills-card">

          <div className="section-heading">

            <h2>
              ❌ Missing Skills
            </h2>

            <span className="skill-count missing-count">
              {missing_skills.length}
            </span>

          </div>


          <div className="skill-list">

            {missing_skills.length > 0 ? (

              missing_skills.map((skill, index) => (

                <span
                  className="skill-pill missing-pill"
                  key={index}
                >
                  {skill}
                </span>

              ))

            ) : (

              <p className="no-skills">
                🎉 No missing skills!
              </p>

            )}

          </div>

        </div>

      </section>


      {/* =====================================================
          CAREER RECOMMENDATIONS
      ===================================================== */}

      <section className="career-section">

        <div className="section-title">

          <h2>
            💼 Recommended Careers
          </h2>

          <p>
            Career paths based on your resume skills
          </p>

        </div>


        <div className="career-grid">

          {recommended_roles.length > 0 ? (

            recommended_roles.map((career, index) => (

              <div
                className="career-card"
                key={index}
              >

                <div className="career-number">
                  {index + 1}
                </div>


                <div className="career-content">

                  <h3>
                    {career.role ||
                      career.title ||
                      career.name ||
                      "Recommended Career"}
                  </h3>


                  {career.category && (

                    <p className="career-category">

                      <strong>
                        Category:
                      </strong>{" "}

                      {career.category}

                    </p>

                  )}


                  {(career.score !== undefined ||
                    career.match_score !== undefined) && (

                    <div className="career-score">

                      Match Score:{" "}

                      <strong>
                        {career.score ??
                          career.match_score}
                      </strong>

                    </div>

                  )}


                  {career.description && (

                    <p className="career-description">
                      {career.description}
                    </p>

                  )}

                </div>

              </div>

            ))

          ) : (

            <div className="no-careers">
              No career recommendations available.
            </div>

          )}

        </div>

      </section>


      {/* =====================================================
          RESUME FEEDBACK
      ===================================================== */}

      <section className="feedback-section">

        <div className="feedback-card">

          <div className="section-title">

            <h2>
              📝 Resume Feedback
            </h2>

            <p>
              Suggestions to improve your resume
            </p>

          </div>


          {feedback.length > 0 ? (

            <div className="feedback-list">

              {feedback.map((item, index) => (

                <div
                  className="feedback-item"
                  key={index}
                >

                  <span className="feedback-icon">
                    💡
                  </span>

                  <span>
                    {item}
                  </span>

                </div>

              ))}

            </div>

          ) : (

            <div className="feedback-success">

              🎉 Excellent resume!
              No major improvements required.

            </div>

          )}

        </div>

      </section>

    </div>
  );
}

export default ResultCard;