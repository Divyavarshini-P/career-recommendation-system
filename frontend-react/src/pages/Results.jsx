import React from "react";
import { useNavigate } from "react-router-dom";
import "./Results.css";

function Results() {
  const navigate = useNavigate();

  let result = null;

  try {
    result = JSON.parse(
      localStorage.getItem("analysisResult") || "null"
    );
  } catch (error) {
    console.error("Invalid analysis result:", error);
  }

  if (!result) {
    return (
      <div className="results-page">
        <div className="no-results">
          <div className="no-results-icon">⚠️</div>

          <h2>No Analysis Found</h2>

          <p>
            Please analyze your resume first to view your results.
          </p>

          <button
            className="back-button"
            onClick={() => navigate("/analyze")}
          >
            Go to Resume Analysis
          </button>
        </div>
      </div>
    );
  }

  const atsScore = result.ats_score ?? 0;
  const atsBreakdown = result.ats_breakdown || {};

  const matchedSkills = Array.isArray(result.matched_skills)
    ? result.matched_skills
    : [];

  const missingSkills = Array.isArray(result.missing_skills)
    ? result.missing_skills
    : [];

  const additionalSkills = Array.isArray(result.additional_skills)
    ? result.additional_skills
    : [];

  const learningRecommendations = Array.isArray(
    result.learning_recommendations
  )
    ? result.learning_recommendations
    : [];

  const recommendedRoles = Array.isArray(
    result.recommended_roles
  )
    ? result.recommended_roles
    : [];

  const feedback = Array.isArray(result.feedback)
    ? result.feedback
    : [];

  const strengths = Array.isArray(result.strengths)
    ? result.strengths
    : [];

  const interviewQuestions = Array.isArray(
    result.interview_questions
  )
    ? result.interview_questions
    : [];

  const getAtsValue = (key) => {
    const value = atsBreakdown[key];

    if (
      typeof value === "number" ||
      typeof value === "string"
    ) {
      return value;
    }

    return 0;
  };

  const formatNumber = (value) => {
    if (typeof value !== "number") {
      return value ?? 0;
    }

    return Number.isInteger(value)
      ? value
      : value.toFixed(2);
  };

  const downloadReport = async () => {
    const API_URL = "http://127.0.0.1:8000";

    try {
      const response = await fetch(
        `${API_URL}/download-report`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(result),
        }
      );

      if (!response.ok) {
        throw new Error(
          `Report generation failed: ${response.status}`
        );
      }

      const blob = await response.blob();

      const url = window.URL.createObjectURL(blob);

      const link = document.createElement("a");

      link.href = url;

      link.download =
        "career_analysis_report.pdf";

      document.body.appendChild(link);

      link.click();

      document.body.removeChild(link);

      window.URL.revokeObjectURL(url);
    } catch (error) {
      console.error(
        "Report download error:",
        error
      );

      alert(
        "Could not download the report. Please make sure the backend is running."
      );
    }
  };

  return (
    <div className="results-page">

      {/* =====================================================
          HEADER
      ===================================================== */}

      <div className="results-header">

        <div className="results-header-content">

          <div className="results-header-icon">
            📊
          </div>

          <div>
            <h1>
              Resume Analysis Results
            </h1>

            <p>
              AI-powered analysis of your resume
              against the selected job description.
            </p>
          </div>

        </div>

        <button
          className="new-analysis-button"
          onClick={() => navigate("/analyze")}
        >
          🔄 New Analysis
        </button>

      </div>


      {/* =====================================================
          ANALYSIS SUMMARY
      ===================================================== */}

      <section className="results-section">

        <div className="section-title">

          <span className="section-icon">
            📋
          </span>

          <div>
            <h2>
              Analysis Summary
            </h2>

            <p>
              Overview of your resume analysis
            </p>
          </div>

        </div>

        <div className="summary-grid">

          <div className="summary-card">

            <span className="summary-label">
              Job Match
            </span>

            <strong className="summary-value">
              {formatNumber(
                result.match_score ?? 0
              )}
              %
            </strong>

          </div>


          <div className="summary-card">

            <span className="summary-label">
              ATS Score
            </span>

            <strong className="summary-value">
              {atsScore}
              <small>/100</small>
            </strong>

          </div>


          <div className="summary-card">

            <span className="summary-label">
              Matched Skills
            </span>

            <strong className="summary-value">
              {result.matched_skill_count ??
                matchedSkills.length}
            </strong>

          </div>


          <div className="summary-card">

            <span className="summary-label">
              Missing Skills
            </span>

            <strong className="summary-value">
              {result.missing_skill_count ??
                missingSkills.length}
            </strong>

          </div>

        </div>

      </section>


      {/* =====================================================
          JOB MATCH BREAKDOWN
      ===================================================== */}

      {result.match_breakdown && (

        <section className="results-section">

          <div className="section-title">

            <span className="section-icon">
              🎯
            </span>

            <div>

              <h2>
                Job Match Score Breakdown
              </h2>

              <p>
                How closely your resume matches
                the selected job description.
              </p>

            </div>

          </div>


          <div className="match-breakdown-grid">

            <div className="breakdown-item">
              <span>
                Technical Skill Match
              </span>

              <strong>
                {formatNumber(
                  result.match_breakdown.skill_match ??
                    0
                )}
                /40
              </strong>
            </div>


            <div className="breakdown-item">
              <span>
                Semantic JD Match
              </span>

              <strong>
                {formatNumber(
                  result.match_breakdown.semantic_match ??
                    0
                )}
                /30
              </strong>
            </div>


            <div className="breakdown-item">
              <span>
                Project Relevance
              </span>

              <strong>
                {formatNumber(
                  result.match_breakdown.project_relevance ??
                    0
                )}
                /15
              </strong>
            </div>


            <div className="breakdown-item">
              <span>
                Experience Relevance
              </span>

              <strong>
                {formatNumber(
                  result.match_breakdown.experience_relevance ??
                    0
                )}
                /10
              </strong>
            </div>


            <div className="breakdown-item">
              <span>
                Education Relevance
              </span>

              <strong>
                {formatNumber(
                  result.match_breakdown.education_relevance ??
                    0
                )}
                /5
              </strong>
            </div>

          </div>


          <div className="breakdown-total">

            <span>
              Total Match Score
            </span>

            <strong>
              {formatNumber(
                result.match_breakdown.total_score ??
                  result.match_score ??
                  0
              )}
              %
            </strong>

          </div>

        </section>

      )}


      {/* =====================================================
          ATS SCORE
      ===================================================== */}

      <section className="results-section">

        <div className="section-title">

          <span className="section-icon">
            📊
          </span>

          <div>

            <h2>
              ATS Score Breakdown
            </h2>

            <p>
              Resume compatibility with
              Applicant Tracking Systems.
            </p>

          </div>

        </div>


        <div className="overall-ats-score">

          <div className="ats-score-label">

            <span>
              Overall ATS Score
            </span>

            <small>
              Resume ATS Compatibility
            </small>

          </div>


          <div className="ats-score-value">

            <strong>
              {atsScore}
            </strong>

            <span>
              / 100
            </span>

          </div>

        </div>


        <div className="ats-breakdown-grid">

          <div className="ats-breakdown-card">

            <span>
              Contact Information
            </span>

            <strong>
              {getAtsValue(
                "contact_information"
              )}
            </strong>

            <small>
              / 25
            </small>

          </div>


          <div className="ats-breakdown-card">

            <span>
              Resume Structure
            </span>

            <strong>
              {getAtsValue(
                "resume_structure"
              )}
            </strong>

            <small>
              / 40
            </small>

          </div>


          <div className="ats-breakdown-card">

            <span>
              Resume Length
            </span>

            <strong>
              {getAtsValue(
                "resume_length"
              )}
            </strong>

            <small>
              / 10
            </small>

          </div>


          <div className="ats-breakdown-card">

            <span>
              Skill Match
            </span>

            <strong>
              {getAtsValue(
                "skill_match"
              )}
            </strong>

            <small>
              / 25
            </small>

          </div>

        </div>

      </section>


      {/* =====================================================
          ATS RATING
      ===================================================== */}

      {result.ats_rating && (

        <section className="results-section">

          <div className="rating-box">

            <div>

              <span className="rating-label">
                ATS Rating
              </span>

              <h3>
                {result.ats_rating}
              </h3>

            </div>

            <div className="rating-score">
              {atsScore}/100
            </div>

          </div>

        </section>

      )}


      {/* =====================================================
          MATCHED SKILLS
      ===================================================== */}

      <section className="results-section">

        <div className="section-title">

          <span className="section-icon">
            ✅
          </span>

          <div>

            <h2>
              Matched Skills
            </h2>

            <p>
              Skills detected in both your resume
              and the job description.
            </p>

          </div>

        </div>


        {matchedSkills.length > 0 ? (

          <div className="skills-container">

            {matchedSkills.map(
              (skill, index) => (

                <span
                  className="skill-tag matched-skill"
                  key={`${skill}-${index}`}
                >
                  ✓ {skill}
                </span>

              )
            )}

          </div>

        ) : (

          <p className="empty-message">
            No matched skills detected.
          </p>

        )}

      </section>


      {/* =====================================================
          MISSING SKILLS
      ===================================================== */}

      <section className="results-section">

        <div className="section-title">

          <span className="section-icon">
            ⚠️
          </span>

          <div>

            <h2>
              Missing Skills
            </h2>

            <p>
              Skills required by the job description
              that were not detected in your resume.
            </p>

          </div>

        </div>


        {missingSkills.length > 0 ? (

          <div className="skills-container">

            {missingSkills.map(
              (skill, index) => (

                <span
                  className="skill-tag missing-skill"
                  key={`${skill}-${index}`}
                >
                  + {skill}
                </span>

              )
            )}

          </div>

        ) : (

          <p className="success-message">
            🎉 No major missing skills detected.
          </p>

        )}

      </section>


      {/* =====================================================
          ADDITIONAL SKILLS
      ===================================================== */}

      {additionalSkills.length > 0 && (

        <section className="results-section">

          <div className="section-title">

            <span className="section-icon">
              ➕
            </span>

            <div>

              <h2>
                Additional Resume Skills
              </h2>

              <p>
                Skills found in your resume that
                were not specifically required by
                the selected JD.
              </p>

            </div>

          </div>


          <div className="skills-container">

            {additionalSkills.map(
              (skill, index) => (

                <span
                  className="skill-tag additional-skill"
                  key={`${skill}-${index}`}
                >
                  {skill}
                </span>

              )
            )}

          </div>

        </section>

      )}


      {/* =====================================================
          SKILL GAP
      ===================================================== */}

      {result.skill_gap_chart && (

        <section className="results-section">

          <div className="section-title">

            <span className="section-icon">
              📈
            </span>

            <div>

              <h2>
                Skill Gap Analysis
              </h2>

              <p>
                Comparison between your existing
                skills and required skills.
              </p>

            </div>

          </div>


          <div className="skill-gap-summary">

            <div className="gap-stat matched-gap">

              <span>
                Matched
              </span>

              <strong>
                {result.matched_skill_count ??
                  matchedSkills.length}
              </strong>

            </div>


            <div className="gap-stat missing-gap">

              <span>
                Missing
              </span>

              <strong>
                {result.missing_skill_count ??
                  missingSkills.length}
              </strong>

            </div>

          </div>

        </section>

      )}


      {/* =====================================================
          RESUME STRENGTHS
      ===================================================== */}

      {strengths.length > 0 && (

        <section className="results-section">

          <div className="section-title">

            <span className="section-icon">
              💪
            </span>

            <div>

              <h2>
                Resume Strengths
              </h2>

              <p>
                Strengths identified from your resume.
              </p>

            </div>

          </div>


          <div className="feedback-list">

            {strengths.map(
              (strength, index) => (

                <div
                  className="feedback-item positive"
                  key={index}
                >

                  <span>
                    ✓
                  </span>

                  <p>
                    {strength}
                  </p>

                </div>

              )
            )}

          </div>

        </section>

      )}


      {/* =====================================================
          KEYWORD ANALYSIS
      ===================================================== */}

      {result.keyword_analysis && (

        <section className="results-section">

          <div className="section-title">

            <span className="section-icon">
              🔎
            </span>

            <div>

              <h2>
                Resume Keyword Analysis
              </h2>

              <p>
                Keywords detected from your resume
                and job description.
              </p>

            </div>

          </div>


          <div className="keyword-analysis">

            {Object.entries(
              result.keyword_analysis
            ).map(
              ([key, value]) => (

                <div
                  className="keyword-item"
                  key={key}
                >

                  <span>
                    {key
                      .replaceAll("_", " ")
                      .replace(
                        /\b\w/g,
                        (char) =>
                          char.toUpperCase()
                      )}
                  </span>

                  <strong>
                    {Array.isArray(value)
                      ? value.length
                      : value}
                  </strong>

                </div>

              )
            )}

          </div>

        </section>

      )}


      {/* =====================================================
          RECOMMENDED LEARNING
      ===================================================== */}

      {learningRecommendations.length > 0 && (

        <section className="results-section learning-section">

          <div className="section-title">

            <span className="section-icon">
              📚
            </span>

            <div>

              <h2>
                Recommended Learning
              </h2>

              <p>
                Skills and courses recommended
                based on your analysis.
              </p>

            </div>

          </div>


          <div className="learning-grid">

            {learningRecommendations.map(
              (item, index) => {

                const skill =
                  item?.skill ||
                  item?.topic ||
                  item?.title ||
                  "Learning Topic";

                const description =
                  item?.description ||
                  `Learn the fundamentals and practical applications of ${skill}.`;

                const resources =
                  Array.isArray(item?.resources)
                    ? item.resources
                    : [];

                const resource =
                  resources.find(
                    (entry) =>
                      entry &&
                      typeof entry === "object" &&
                      Boolean(
                        entry.url ||
                        entry.link
                      )
                  );

                const courseTitle =
                  resource?.title ||
                  resource?.name ||
                  "Start Learning";

                const courseUrl =
                  resource?.url ||
                  resource?.link ||
                  null;

                return (

                  <div
                    className="learning-card"
                    key={`${skill}-${index}`}
                  >

                    <div className="learning-card-top">

                      <div className="learning-icon">
                        📘
                      </div>

                      <div className="learning-heading">

                        <h3>
                          {skill}
                        </h3>

                        <span className="learning-label">
                          Recommended Skill
                        </span>

                      </div>

                    </div>


                    <p className="learning-description">
                      {description}
                    </p>


                    {courseUrl ? (

                      <div className="course-box">

                        <div className="course-info">

                          <span className="course-icon">
                            🎓
                          </span>

                          <div>

                            <span className="course-label">
                              Recommended Course
                            </span>

                            <strong>
                              {courseTitle}
                            </strong>

                          </div>

                        </div>


                        <a
                          href={courseUrl}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="start-course-button"
                        >
                          Start Course ↗
                        </a>

                      </div>

                    ) : (

                      <div className="course-box no-course">

                        <div className="course-info">

                          <span className="course-icon">
                            📖
                          </span>

                          <div>

                            <span className="course-label">
                              Learning Path
                            </span>

                            <strong>
                              Fundamentals &amp; Practice
                            </strong>

                          </div>

                        </div>

                      </div>

                    )}

                  </div>

                );
              }
            )}

          </div>

        </section>

      )}


      {/* =====================================================
          CAREER ROLES
      ===================================================== */}

      {recommendedRoles.length > 0 && (

        <section className="results-section">

          <div className="section-title">

            <span className="section-icon">
              🚀
            </span>

            <div>

              <h2>
                Recommended Career Roles
              </h2>

              <p>
                Career roles identified from
                your skills and resume.
              </p>

            </div>

          </div>


          <div className="career-grid">

            {recommendedRoles.map(
              (role, index) => {

                const roleName =
                  typeof role === "string"
                    ? role
                    : role?.role ||
                      role?.title ||
                      role?.name ||
                      "Career Role";

                return (

                  <div
                    className="career-card"
                    key={index}
                  >

                    <span className="career-number">
                      {index + 1}
                    </span>

                    <h3>
                      {roleName}
                    </h3>

                    {typeof role ===
                      "object" &&
                      role?.match_score !==
                        undefined && (

                        <p>
                          Match:{" "}
                          <strong>
                            {role.match_score}%
                          </strong>
                        </p>

                    )}

                  </div>

                );
              }
            )}

          </div>

        </section>

      )}


      {/* =====================================================
          RESUME FEEDBACK
      ===================================================== */}

      {feedback.length > 0 && (

        <section className="results-section">

          <div className="section-title">

            <span className="section-icon">
              💡
            </span>

            <div>

              <h2>
                Resume Improvement Suggestions
              </h2>

              <p>
                Suggestions to improve your resume
                for the selected role.
              </p>

            </div>

          </div>


          <div className="feedback-list">

            {feedback.map(
              (item, index) => (

                <div
                  className="feedback-item"
                  key={index}
                >

                  <span>
                    💡
                  </span>

                  <p>
                    {typeof item === "string"
                      ? item
                      : item?.message ||
                        item?.text ||
                        item?.suggestion ||
                        "Resume improvement suggestion"}
                  </p>

                </div>

              )
            )}

          </div>

        </section>

      )}


      {/* =====================================================
          INTERVIEW PREPARATION
      ===================================================== */}

      {interviewQuestions.length > 0 && (

        <section className="results-section">

          <div className="section-title">

            <span className="section-icon">
              🎤
            </span>

            <div>

              <h2>
                Interview Preparation
              </h2>

              <p>
                Questions to help you prepare
                for the selected role.
              </p>

            </div>

          </div>


          <div className="interview-list">

            {interviewQuestions.map(
              (question, index) => (

                <div
                  className="interview-item"
                  key={index}
                >

                  <span>
                    Q{index + 1}
                  </span>

                  <p>
                    {typeof question ===
                    "string"
                      ? question
                      : question?.question ||
                        question?.text ||
                        "Interview question"}
                  </p>

                </div>

              )
            )}

          </div>

        </section>

      )}


      {/* =====================================================
          ACTIONS
      ===================================================== */}

      <section className="results-actions">

        <button
          className="download-button"
          onClick={downloadReport}
        >
          📥 Download Full Analysis Report
        </button>


        <button
          className="new-analysis-button bottom-button"
          onClick={() =>
            navigate("/analyze")
          }
        >
          🔄 Analyze Another Resume
        </button>

      </section>

    </div>
  );
}

export default Results;