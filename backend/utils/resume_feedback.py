# backend/utils/resume_feedback.py

import re


def normalize_text(text):
    """Convert text to lowercase for easier matching."""
    return text.lower().strip()


def has_any(text, keywords):
    """Check whether any keyword exists in the text."""
    return any(
        keyword.lower() in text
        for keyword in keywords
    )


def generate_resume_feedback(
    resume_text,
    job_description,
    matched_skills,
    missing_skills
):
    """
    Generate resume improvement suggestions
    based on the actual job description and resume.
    """

    resume = normalize_text(resume_text)
    jd = normalize_text(job_description)

    feedback = []

    # ========================================================
    # 1. JOB-SPECIFIC MISSING SKILLS
    # ========================================================

    if missing_skills:

        important_missing = missing_skills[:8]

        skills_text = ", ".join(
            skill.title()
            for skill in important_missing
        )

        feedback.append(
            f"Consider strengthening or highlighting "
            f"these skills required by the target role: "
            f"{skills_text}. Only include skills you "
            f"actually have or are currently learning."
        )

    # ========================================================
    # 2. MATCHED SKILLS
    # ========================================================

    if matched_skills:

        matched_text = ", ".join(
            skill.title()
            for skill in matched_skills[:6]
        )

        feedback.append(
            f"Your resume already matches important "
            f"job requirements such as {matched_text}. "
            f"Make these skills more visible by connecting "
            f"them to your projects, internship, or experience."
        )

    # ========================================================
    # 3. DATA ANALYST SPECIFIC FEEDBACK
    # ========================================================

    data_analyst_keywords = [
        "data analyst",
        "data analysis",
        "data analytics",
        "business intelligence",
        "power bi",
        "tableau",
        "data visualization"
    ]

    if has_any(jd, data_analyst_keywords):

        if "sql" in jd and "sql" not in resume:

            feedback.append(
                "SQL is relevant to this Data Analyst role. "
                "If you have used SQL in projects or coursework, "
                "highlight the queries, joins, filtering, or "
                "database work you performed."
            )

        if (
            "power bi" in jd
            and "power bi" not in resume
        ):

            feedback.append(
                "Power BI is mentioned in the target role. "
                "If you have dashboard or visualization experience, "
                "highlight it clearly; otherwise consider learning "
                "Power BI."
            )

        if (
            "excel" in jd
            and "excel" not in resume
        ):

            feedback.append(
                "Excel is relevant to this Data Analyst position. "
                "If applicable, mention formulas, PivotTables, "
                "lookup functions, or reporting work."
            )

        if (
            "pandas" in jd
            and "pandas" not in resume
        ):

            feedback.append(
                "Pandas is required by the target role. "
                "If you have used it for data cleaning or analysis, "
                "include it in your skills or project descriptions."
            )

        if (
            "data visualization" in jd
            and not has_any(
                resume,
                [
                    "matplotlib",
                    "plotly",
                    "power bi",
                    "tableau",
                    "visualization"
                ]
            )
        ):

            feedback.append(
                "Add evidence of data visualization experience, "
                "such as dashboards, charts, Matplotlib, Plotly, "
                "Power BI, or Tableau, when applicable."
            )

        if (
            "statistics" in jd
            and "statistics" not in resume
        ):

            feedback.append(
                "Statistics is relevant to the target Data Analyst "
                "role. If you have studied or applied statistics, "
                "mention concepts such as descriptive statistics, "
                "probability, or hypothesis testing."
            )

    # ========================================================
    # 4. SOFTWARE ENGINEER SPECIFIC FEEDBACK
    # ========================================================

    software_keywords = [
        "software engineer",
        "software developer",
        "software development",
        "backend developer",
        "frontend developer"
    ]

    if has_any(jd, software_keywords):

        if (
            "git" in jd
            and "git" not in resume
            and "github" not in resume
        ):

            feedback.append(
                "Git/GitHub is required for this role. "
                "If you have used version control in your projects, "
                "add Git and GitHub to the relevant skills or project."
            )

        if (
            "rest api" in jd
            and not has_any(
                resume,
                [
                    "rest api",
                    "rest apis",
                    "api development"
                ]
            )
        ):

            feedback.append(
                "REST API development is relevant to this role. "
                "If applicable, describe any API you developed, "
                "integrated, or tested in your projects."
            )

        if (
            "data structures" in jd
            and "data structures" not in resume
            and "dsa" not in resume
        ):

            feedback.append(
                "Data Structures and Algorithms are required. "
                "If you have practiced DSA, include it in your "
                "technical skills or preparation section."
            )

        if (
            "react" in jd
            and "react" not in resume
        ):

            feedback.append(
                "React.js is mentioned in the target role. "
                "If you have frontend project experience, "
                "highlight your React components, state management, "
                "routing, or API integration."
            )

        if (
            "docker" in jd
            and "docker" not in resume
        ):

            feedback.append(
                "Docker is listed as a preferred skill. "
                "Consider learning containerization and mention it "
                "only after gaining practical experience."
            )

        if (
            "aws" in jd
            and "aws" not in resume
        ):

            feedback.append(
                "AWS is listed as a preferred skill. "
                "Consider adding a small cloud deployment project "
                "after gaining practical AWS experience."
            )

    # ========================================================
    # 5. PROJECT FEEDBACK
    # ========================================================

    if not has_any(
        resume,
        [
            "project",
            "projects"
        ]
    ):

        feedback.append(
            "Add relevant academic or personal projects "
            "that demonstrate skills required by the target role."
        )

    else:

        # Check whether project descriptions contain results
        if not re.search(
            r"\b\d+%|\b\d+\+|\b\d+\s*(users|records|datasets|projects)",
            resume
        ):

            feedback.append(
                "Strengthen project descriptions with measurable "
                "results where possible, such as accuracy, dataset "
                "size, number of records, users, or performance improvement."
            )

    # ========================================================
    # 6. EXPERIENCE / INTERNSHIP
    # ========================================================

    if not has_any(
        resume,
        [
            "experience",
            "internship",
            "intern",
            "work experience"
        ]
    ):

        feedback.append(
            "If you have internship or practical experience, "
            "include it with specific responsibilities and technologies used."
        )

    # ========================================================
    # 7. CONTACT INFORMATION
    # ========================================================

    if not re.search(
        r"[\w\.-]+@[\w\.-]+\.\w+",
        resume
    ):

        feedback.append(
            "Add a professional email address to your resume."
        )

    if "linkedin" not in resume:

        feedback.append(
            "Include your LinkedIn profile if available."
        )

    # ========================================================
    # 8. RESUME LENGTH
    # ========================================================

    word_count = len(
        resume.split()
    )

    if word_count < 200:

        feedback.append(
            "Your resume appears short. Add relevant project, "
            "internship, technical, and achievement details."
        )

    # ========================================================
    # 9. FALLBACK
    # ========================================================

    if not feedback:

        feedback.append(
            "Your resume covers the main requirements detected "
            "for this role. Continue tailoring project descriptions "
            "and keywords to the specific job description."
        )

    # Remove duplicate feedback
    unique_feedback = []

    seen = set()

    for item in feedback:

        key = item.lower().strip()

        if key not in seen:

            seen.add(key)

            unique_feedback.append(item)

    return unique_feedback[:10]