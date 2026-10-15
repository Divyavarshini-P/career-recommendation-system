import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "../styles/ResumeForm.css";

const API_URL = "http://127.0.0.1:8000";

function ResumeForm() {
  const navigate = useNavigate();

  const [file, setFile] = useState(null);
  const [resumeText, setResumeText] = useState("");
  const [jobDescription, setJobDescription] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // ==========================================
  // FILE SELECTION
  // ==========================================

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];

    if (!selectedFile) return;

    const fileName = selectedFile.name.toLowerCase();

    if (
      !fileName.endsWith(".pdf") &&
      !fileName.endsWith(".docx")
    ) {
      setError("Please upload a PDF or DOCX file.");
      setFile(null);
      return;
    }

    // 5 MB limit
    if (selectedFile.size > 5 * 1024 * 1024) {
      setError("File size should be less than 5 MB.");
      setFile(null);
      return;
    }

    setError("");
    setFile(selectedFile);

    // Clear pasted resume when a file is selected
    setResumeText("");
  };

  // ==========================================
  // REMOVE FILE
  // ==========================================

  const removeFile = () => {
    setFile(null);

    const input = document.getElementById("resume-file");

    if (input) {
      input.value = "";
    }
  };

  // ==========================================
  // ANALYZE
  // ==========================================

  const handleAnalyze = async () => {
    setError("");

    if (!file && !resumeText.trim()) {
      setError(
        "Please upload your resume or paste your resume text."
      );
      return;
    }

    if (!jobDescription.trim()) {
      setError("Please enter the job description.");
      return;
    }

    setLoading(true);

    try {
      let extractedResumeText = resumeText.trim();

      // ==========================================
      // UPLOAD RESUME
      // ==========================================

      if (file) {
        const formData = new FormData();

        formData.append("file", file);

        const uploadResponse = await fetch(
          `${API_URL}/upload-resume`,
          {
            method: "POST",
            body: formData,
          }
        );

        if (!uploadResponse.ok) {
          let message = "Unable to upload resume.";

          try {
            const errorData = await uploadResponse.json();

            if (errorData.detail) {
              message = errorData.detail;
            }
          } catch (e) {
            console.error(e);
          }

          throw new Error(message);
        }

        const uploadData = await uploadResponse.json();

        extractedResumeText =
          uploadData.resume_text ||
          uploadData.text ||
          "";

        if (!extractedResumeText.trim()) {
          throw new Error(
            "Resume uploaded, but no text was extracted."
          );
        }
      }

      // ==========================================
      // ANALYZE RESUME
      // ==========================================

      const analysisResponse = await fetch(
        `${API_URL}/analyze-resume`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            resume_text: extractedResumeText,
            job_description: jobDescription.trim(),
          }),
        }
      );

      if (!analysisResponse.ok) {
        let message = "Resume analysis failed.";

        try {
          const errorData = await analysisResponse.json();

          if (errorData.detail) {
            message = errorData.detail;
          }
        } catch (e) {
          console.error(e);
        }

        throw new Error(message);
      }

      const result = await analysisResponse.json();

      // ==========================================
      // SAVE RESULT
      // ==========================================

      const completeResult = {
        ...result,
        resume_text: extractedResumeText,
        job_description: jobDescription.trim(),
        filename: file ? file.name : "Pasted Resume",
      };

      localStorage.setItem(
        "analysisResult",
        JSON.stringify(completeResult)
      );

      localStorage.setItem(
        "resumeText",
        extractedResumeText
      );

      localStorage.setItem(
        "jobDescription",
        jobDescription.trim()
      );

      // ==========================================
      // GO TO RESULTS
      // ==========================================

      navigate("/results");

    } catch (err) {
      console.error("Analysis Error:", err);

      setError(
        err.message ||
        "Unable to connect to FastAPI backend."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="resume-form-page">

      {/* ========================================
          PAGE HEADER
      ======================================== */}

      <div className="analyzer-header">

        <div className="analyzer-header-icon">
          🚀
        </div>

        <div>
          <h1>AI Resume Analyzer</h1>

          <p>
            Upload your resume and compare it with a job
            description using AI-powered analysis.
          </p>
        </div>

      </div>


      {/* ========================================
          MAIN CONTENT
      ======================================== */}

      <div className="analyzer-container">

        {/* ======================================
            RESUME CARD
        ====================================== */}

        <div className="analyzer-card">

          <div className="card-heading">

            <div>
              <h2>Upload Your Resume</h2>

              <p>
                Upload your PDF or DOCX resume.
              </p>
            </div>

          </div>


          {/* ====================================
              UPLOAD AREA
          ==================================== */}

          <label
            htmlFor="resume-file"
            className={`resume-upload ${
              file ? "selected" : ""
            }`}
          >

            <div className="upload-icon">
              {file ? "✅" : "📄"}
            </div>

            <h3>
              {file
                ? file.name
                : "Drag & Drop or Choose Resume"}
            </h3>

            <p>
              PDF or DOCX • Maximum size: 5 MB
            </p>

            <span className="browse-btn">
              {file
                ? "Choose Another File"
                : "Browse Resume"}
            </span>

          </label>


          <input
            id="resume-file"
            type="file"
            accept=".pdf,.docx"
            onChange={handleFileChange}
            hidden
          />


          {/* ====================================
              SELECTED FILE
          ==================================== */}

          {file && (
            <div className="file-selected-box">

              <div>
                <strong>
                  📄 {file.name}
                </strong>

                <small>
                  Resume ready for analysis
                </small>
              </div>

              <button
                type="button"
                onClick={removeFile}
              >
                Remove
              </button>

            </div>
          )}


          {/* ====================================
              DIVIDER
          ==================================== */}

          <div className="divider">
            <span>OR</span>
          </div>


          {/* ====================================
              PASTE RESUME
          ==================================== */}

          <div className="input-group">

            <label>
              📝 Paste Resume Text
            </label>

            <p>
              You can also paste your resume content
              directly.
            </p>

            <textarea
              className="resume-textarea"
              value={resumeText}
              onChange={(e) => {
                setResumeText(e.target.value);

                if (e.target.value.trim()) {
                  setFile(null);

                  const input =
                    document.getElementById(
                      "resume-file"
                    );

                  if (input) {
                    input.value = "";
                  }
                }
              }}
              placeholder="Paste your complete resume text here..."
            />

            <div className="character-count">
              {resumeText.length} characters
            </div>

          </div>

        </div>


        {/* ======================================
            JOB DESCRIPTION CARD
        ====================================== */}

        <div className="analyzer-card">

          <div className="card-heading">

            <div>
              <h2>Job Description</h2>

              <p>
                Paste the job description you want to
                target.
              </p>
            </div>

          </div>


          {/* ====================================
              JOB DESCRIPTION
          ==================================== */}

          <div className="input-group">

            <div className="jd-title-row">

              <label>
                💼 Target Job Description
              </label>

              <span>
                Required
              </span>

            </div>


            <textarea
              className="jd-textarea"
              value={jobDescription}
              onChange={(e) =>
                setJobDescription(e.target.value)
              }
              placeholder={`Paste the job description here...

Example:

Software Engineer

Required Skills:
• Python
• Java
• SQL
• React.js
• Git
• REST APIs
• Problem Solving

Qualifications:
• Bachelor's degree
• Good communication skills
• Software development knowledge`}
            />


            <div className="character-count">
              {jobDescription.length} characters
            </div>

          </div>


          {/* ====================================
              AI INFORMATION
          ==================================== */}

          <div className="ai-info">

            <div className="ai-icon">
              ✨
            </div>

            <div>

              <strong>
                AI-powered analysis
              </strong>

              <p>
                Your resume will be compared with the
                job description to identify matched
                skills, missing skills, ATS score and
                suitable career roles.
              </p>

            </div>

          </div>

        </div>

      </div>


      {/* ========================================
          ERROR MESSAGE
      ======================================== */}

      {error && (
        <div className="error-message">

          <span>
            ⚠️
          </span>

          <div>

            <strong>
              Analysis Error
            </strong>

            <p>
              {error}
            </p>

          </div>

        </div>
      )}


      {/* ========================================
          ANALYZE BUTTON
      ======================================== */}

      <div className="analyze-button-container">

        <button
          type="button"
          className="analyze-button"
          onClick={handleAnalyze}
          disabled={loading}
        >

          {loading ? (
            <>
              <span className="loading-spinner"></span>
              Analyzing Resume...
            </>
          ) : (
            <>
              🚀 Analyze Resume
            </>
          )}

        </button>

        <p>
          AI will analyze your resume against the
          selected job description.
        </p>

      </div>

    </div>
  );
}

export default ResumeForm;