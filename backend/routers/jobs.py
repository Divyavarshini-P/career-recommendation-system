from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

import io
import re

import pdfplumber
from docx import Document

from utils.ats_score import calculate_ats_score
from utils.learning_recommender import get_learning_recommendations
from utils.resume_feedback import generate_resume_feedback

# Skill normalization
from utils.skill_normalizer import (
    extract_normalized_skills,
    normalize_skills,
    compare_normalized_skills
)


# ============================================================
# OPTIONAL IMPORTS
# ============================================================

try:
    from utils.skill_extractor import extract_skills
except ImportError:
    extract_skills = None


try:
    from utils.semantic_matcher import semantic_match
except ImportError:
    semantic_match = None


try:
    from utils.career_recommender import recommend_careers
except ImportError:
    recommend_careers = None


try:
    from utils.powerbi_export import export_to_powerbi
except ImportError:
    export_to_powerbi = None


router = APIRouter()


# ============================================================
# COMMON SKILLS
# ============================================================

COMMON_SKILLS = [

    # Programming
    "python",
    "java",
    "javascript",
    "typescript",
    "c++",
    "c#",

    # Web
    "html",
    "css",
    "react",
    "react.js",
    "node.js",
    "angular",
    "vue",

    # Backend
    "fastapi",
    "spring boot",
    "django",
    "flask",
    "express",
    "rest api",
    "rest apis",
    "api development",

    # Databases
    "sql",
    "mysql",
    "postgresql",
    "oracle",
    "mongodb",
    "redis",

    # Version Control
    "git",
    "github",
    "gitlab",

    # Cloud
    "aws",
    "azure",
    "google cloud",
    "cloud computing",

    # DevOps
    "docker",
    "kubernetes",
    "ci/cd",

    # Data
    "pandas",
    "numpy",
    "excel",
    "power bi",
    "tableau",
    "matplotlib",
    "plotly",

    # AI / ML
    "machine learning",
    "deep learning",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "nlp",
    "natural language processing",
    "opencv",

    # DSA
    "data structures",
    "algorithms",
    "data structures and algorithms",
    "dsa",

    # Programming Concepts
    "object oriented programming",
    "oop",
    "problem solving",

    # Data Concepts
    "data analysis",
    "data analytics",
    "data visualization",
    "data preprocessing",
    "data cleaning",
    "exploratory data analysis",
    "eda",
    "statistics",
    "business intelligence",

    # Soft Skills
    "communication",
    "teamwork",

    # Methodologies
    "agile",
    "scrum",

    # Frontend
    "responsive web design",
    "react hooks",
    "react router",
    "redux",
    "tailwind css",
    "bootstrap",
    "material ui",
    "api integration",
    "web accessibility",
    "performance optimization",

    # Backend concepts
    "microservices",
    "jwt",
    "authentication",
    "authorization",
    "api authentication",

    # Business Analysis
    "business analysis",
    "requirements gathering",
    "requirement documentation",
    "stakeholder management",
    "process analysis",
    "critical thinking",
    "presentation skills",
    "documentation",
    "process mapping",
    "business requirements",

    # Tools
    "jira",
    "confluence",
    "powerpoint",

    # Other
    "linux",
    "figma"
]


# ============================================================
# REQUEST MODELS
# ============================================================

class JobRequest(BaseModel):
    resume_text: str
    job_description: str


class SkillGapRequest(BaseModel):
    resume_text: str
    job_description: str


class CareerRequest(BaseModel):
    resume_text: str


class FeedbackRequest(BaseModel):
    resume_text: str


class LearningRecommendationRequest(BaseModel):
    missing_skills: list[str]


# ============================================================
# FALLBACK SKILL EXTRACTION
# ============================================================

def fallback_extract_skills(text):

    if not text:
        return []

    text_lower = text.lower()

    found_skills = []

    for skill in COMMON_SKILLS:

        if skill.lower() in text_lower:

            found_skills.append(skill)

    return sorted(
        list(
            set(found_skills)
        )
    )


# ============================================================
# GET NORMALIZED SKILLS
# ============================================================

def get_skills(text):

    if not text:
        return []

    extracted_skills = []

    # --------------------------------------------------------
    # Existing skill extractor
    # --------------------------------------------------------

    if extract_skills is not None:

        try:

            result = extract_skills(text)

            if isinstance(result, list):

                extracted_skills = result

            elif isinstance(result, dict):

                extracted_skills = result.get(
                    "skills",
                    []
                )

        except Exception as e:

            print(
                f"Skill extractor warning: {e}"
            )

    # --------------------------------------------------------
    # Synonym-based normalization
    # --------------------------------------------------------

    normalized_skills = extract_normalized_skills(
        text,
        extracted_skills
    )

    # --------------------------------------------------------
    # Fallback
    # --------------------------------------------------------

    if not normalized_skills:

        normalized_skills = fallback_extract_skills(
            text
        )

        normalized_skills = normalize_skills(
            normalized_skills
        )

    return sorted(
        list(
            set(normalized_skills)
        )
    )


# ============================================================
# SEMANTIC MATCH SCORE
# ============================================================

def get_semantic_score(
    resume_text,
    job_description
):

    if semantic_match is not None:

        try:

            result = semantic_match(
                resume_text,
                job_description
            )

            if isinstance(
                result,
                (int, float)
            ):

                score = float(result)

                if score <= 1:

                    score *= 100

                return round(
                    min(
                        max(score, 0),
                        100
                    ),
                    2
                )

            if isinstance(
                result,
                dict
            ):

                score = result.get(
                    "score",
                    result.get(
                        "match_score",
                        result.get(
                            "similarity",
                            None
                        )
                    )
                )

                if score is not None:

                    score = float(score)

                    if score <= 1:

                        score *= 100

                    return round(
                        min(
                            max(score, 0),
                            100
                        ),
                        2
                    )

        except Exception as e:

            print(
                f"Semantic matcher warning: {e}"
            )

    return None


# ============================================================
# TECHNICAL SKILL MATCH
# ============================================================

def calculate_skill_match(
    resume_text,
    job_description
):

    resume_raw_skills = get_skills(
        resume_text
    )

    job_raw_skills = get_skills(
        job_description
    )

    comparison = compare_normalized_skills(
        resume_raw_skills,
        job_raw_skills
    )

    resume_skills = comparison[
        "resume_skills"
    ]

    job_skills = comparison[
        "job_skills"
    ]

    matched = comparison[
        "matched"
    ]

    missing = comparison[
        "missing"
    ]

    additional = comparison[
        "additional"
    ]

    if not job_skills:

        percentage = 0

    else:

        percentage = (
            len(matched)
            /
            len(job_skills)
        ) * 100

    return {

        "percentage":
            round(
                percentage,
                2
            ),

        "matched":
            matched,

        "missing":
            missing,

        "additional":
            additional,

        "resume_skills":
            resume_skills,

        "job_skills":
            job_skills
    }


# ============================================================
# PROJECT RELEVANCE
# ============================================================

def calculate_project_relevance(
    resume_text,
    job_description,
    matched_skills
):

    resume = resume_text.lower()
    jd = job_description.lower()

    if (
        "project" not in resume
        and
        "projects" not in resume
    ):

        return 0

    score = 30

    # Matched skills
    if matched_skills:

        score += min(
            len(matched_skills) * 8,
            40
        )

    # Relevant technologies
    tech_keywords = [

        "python",
        "java",
        "javascript",
        "react",
        "fastapi",
        "sql",
        "mongodb",
        "pandas",
        "numpy",
        "power bi",
        "machine learning",
        "nlp",
        "api",
        "html",
        "css"
    ]

    jd_technologies = [

        tech
        for tech in tech_keywords
        if tech in jd
    ]

    resume_technologies = [

        tech
        for tech in tech_keywords
        if tech in resume
    ]

    if jd_technologies:

        common = (
            set(jd_technologies)
            &
            set(resume_technologies)
        )

        score += min(
            len(common) * 6,
            30
        )

    return round(
        min(score, 100),
        2
    )


# ============================================================
# EXPERIENCE RELEVANCE
# ============================================================

def calculate_experience_relevance(
    resume_text,
    job_description
):

    resume = resume_text.lower()
    jd = job_description.lower()

    experience_keywords = [

        "experience",
        "internship",
        "intern",
        "work experience"
    ]

    if not any(
        keyword in resume
        for keyword in experience_keywords
    ):

        return 0

    score = 50

    important_terms = [

        "software",
        "development",
        "data",
        "analysis",
        "python",
        "java",
        "sql",
        "react",
        "fastapi",
        "power bi",
        "excel",
        "machine learning",
        "api",
        "testing",
        "database"
    ]

    matching_terms = 0

    for term in important_terms:

        if (
            term in jd
            and
            term in resume
        ):

            matching_terms += 1

    score += min(
        matching_terms * 7,
        50
    )

    return round(
        min(score, 100),
        2
    )


# ============================================================
# EDUCATION RELEVANCE
# ============================================================

def calculate_education_relevance(
    resume_text,
    job_description
):

    resume = resume_text.lower()
    jd = job_description.lower()

    education_keywords = [

        "education",
        "b.tech",
        "btech",
        "b.e",
        "bachelor",
        "degree",
        "university",
        "college"
    ]

    if not any(
        keyword in resume
        for keyword in education_keywords
    ):

        return 0

    score = 60

    relevant_degrees = [

        "computer science",
        "artificial intelligence",
        "data science",
        "information technology",
        "statistics",
        "mathematics",
        "business administration"
    ]

    resume_degree_match = any(
        degree in resume
        for degree in relevant_degrees
    )

    jd_degree_match = any(
        degree in jd
        for degree in relevant_degrees
    )

    if (
        resume_degree_match
        and
        jd_degree_match
    ):

        score = 100

    elif resume_degree_match:

        score = 85

    return score


# ============================================================
# COMPLETE MATCH SCORE BREAKDOWN
# ============================================================

def calculate_match_score_breakdown(
    resume_text,
    job_description
):

    skill_result = calculate_skill_match(
        resume_text,
        job_description
    )

    matched_skills = skill_result[
        "matched"
    ]

    missing_skills = skill_result[
        "missing"
    ]

    additional_skills = skill_result[
        "additional"
    ]

    resume_skills = skill_result[
        "resume_skills"
    ]

    job_skills = skill_result[
        "job_skills"
    ]

    skill_percentage = skill_result[
        "percentage"
    ]

    # --------------------------------------------------------
    # SEMANTIC
    # --------------------------------------------------------

    semantic_percentage = get_semantic_score(
        resume_text,
        job_description
    )

    if semantic_percentage is None:

        semantic_percentage = (
            skill_percentage
        )

    # --------------------------------------------------------
    # PROJECT
    # --------------------------------------------------------

    project_percentage = (
        calculate_project_relevance(
            resume_text,
            job_description,
            matched_skills
        )
    )

    # --------------------------------------------------------
    # EXPERIENCE
    # --------------------------------------------------------

    experience_percentage = (
        calculate_experience_relevance(
            resume_text,
            job_description
        )
    )

    # --------------------------------------------------------
    # EDUCATION
    # --------------------------------------------------------

    education_percentage = (
        calculate_education_relevance(
            resume_text,
            job_description
        )
    )

    # --------------------------------------------------------
    # WEIGHTS
    # --------------------------------------------------------

    skill_weight = 40
    semantic_weight = 30
    project_weight = 15
    experience_weight = 10
    education_weight = 5

    # --------------------------------------------------------
    # WEIGHTED SCORES
    # --------------------------------------------------------

    skill_score = (
        skill_percentage
        *
        skill_weight
        /
        100
    )

    semantic_score = (
        semantic_percentage
        *
        semantic_weight
        /
        100
    )

    project_score = (
        project_percentage
        *
        project_weight
        /
        100
    )

    experience_score = (
        experience_percentage
        *
        experience_weight
        /
        100
    )

    education_score = (
        education_percentage
        *
        education_weight
        /
        100
    )

    total_score = (
        skill_score
        +
        semantic_score
        +
        project_score
        +
        experience_score
        +
        education_score
    )

    total_score = round(
        min(
            max(
                total_score,
                0
            ),
            100
        ),
        2
    )

    return {

        "total_score":
            total_score,

        "skill_match":
            round(
                skill_score,
                2
            ),

        "semantic_match":
            round(
                semantic_score,
                2
            ),

        "project_relevance":
            round(
                project_score,
                2
            ),

        "experience_relevance":
            round(
                experience_score,
                2
            ),

        "education_relevance":
            round(
                education_score,
                2
            ),

        "raw_percentages": {

            "skill_match":
                skill_percentage,

            "semantic_match":
                semantic_percentage,

            "project_relevance":
                project_percentage,

            "experience_relevance":
                experience_percentage,

            "education_relevance":
                education_percentage
        },

        "weights": {

            "skill_match":
                skill_weight,

            "semantic_match":
                semantic_weight,

            "project_relevance":
                project_weight,

            "experience_relevance":
                experience_weight,

            "education_relevance":
                education_weight
        },

        "resume_skills":
            resume_skills,

        "job_skills":
            job_skills,

        "matched_skills":
            matched_skills,

        "missing_skills":
            missing_skills,

        "additional_skills":
            additional_skills
    }


# ============================================================
# CAREER RECOMMENDATIONS
# ============================================================

def fallback_career_recommendations(
    resume_text
):

    skills = set(
        get_skills(resume_text)
    )

    careers = []

    if (
        "python" in skills
        or
        "pandas" in skills
        or
        "numpy" in skills
        or
        "sql" in skills
        or
        "data analysis" in skills
    ):

        careers.append(
            "Data Analyst"
        )

    if (
        "machine learning" in skills
        or
        "scikit-learn" in skills
        or
        "tensorflow" in skills
        or
        "pytorch" in skills
    ):

        careers.append(
            "Machine Learning Engineer"
        )

    if (
        "react" in skills
        or
        "javascript" in skills
        or
        "html" in skills
        or
        "css" in skills
    ):

        careers.append(
            "Frontend Developer"
        )

    if (
        "java" in skills
        or
        "spring boot" in skills
    ):

        careers.append(
            "Java Developer"
        )

    if (
        "fastapi" in skills
        or
        "rest api" in skills
        or
        "node.js" in skills
    ):

        careers.append(
            "Backend Developer"
        )

    if (
        "power bi" in skills
        or
        "tableau" in skills
        or
        "excel" in skills
        or
        "business intelligence" in skills
    ):

        careers.append(
            "Business/Data Analyst"
        )

    if (
        "business analysis" in skills
        or
        "requirements gathering" in skills
    ):

        careers.append(
            "Business Analyst"
        )

    if not careers:

        careers = [

            "Software Developer",

            "Data Analyst",

            "Business Analyst"
        ]

    return list(
        dict.fromkeys(
            careers
        )
    )


def get_career_recommendations(
    resume_text
):

    if recommend_careers is not None:

        try:

            result = recommend_careers(
                resume_text
            )

            if isinstance(
                result,
                list
            ):

                return result

            if isinstance(
                result,
                dict
            ):

                return result.get(
                    "recommended_roles",
                    result.get(
                        "careers",
                        []
                    )
                )

        except Exception as e:

            print(
                f"Career recommender warning: {e}"
            )

    return fallback_career_recommendations(
        resume_text
    )


# ============================================================
# JD-SPECIFIC RESUME STRENGTHS
# ============================================================

def generate_resume_strengths(
    resume_text,
    job_description,
    matched_skills,
    missing_skills
):

    resume = resume_text.lower()
    jd = job_description.lower()

    strengths = []

    # --------------------------------------------------------
    # MATCHED SKILLS
    # --------------------------------------------------------

    if matched_skills:

        important_matches = matched_skills[:6]

        skill_names = ", ".join(
            skill.title()
            for skill in important_matches
        )

        strengths.append(
            f"Your resume matches "
            f"{len(matched_skills)} skills "
            f"from the target role, including "
            f"{skill_names}."
        )

    # --------------------------------------------------------
    # ROLE GROUPS
    # --------------------------------------------------------

    role_groups = {

        "Frontend Development": [

            "react",
            "javascript",
            "html",
            "css",
            "typescript",
            "responsive web design",
            "redux",
            "tailwind css",
            "bootstrap"
        ],

        "Backend Development": [

            "python",
            "java",
            "fastapi",
            "spring boot",
            "django",
            "flask",
            "node.js",
            "rest api",
            "api development"
        ],

        "Data Analytics": [

            "python",
            "pandas",
            "numpy",
            "sql",
            "excel",
            "power bi",
            "tableau",
            "data analysis",
            "data visualization",
            "statistics"
        ],

        "Machine Learning": [

            "python",
            "machine learning",
            "scikit-learn",
            "tensorflow",
            "pytorch",
            "pandas",
            "numpy",
            "nlp"
        ],

        "Business Analysis": [

            "business analysis",
            "requirements gathering",
            "sql",
            "excel",
            "power bi",
            "data analysis",
            "stakeholder management",
            "documentation",
            "process analysis"
        ]
    }

    detected_role_group = None

    for role, skills in role_groups.items():

        jd_matches = 0

        for skill in skills:

            if skill in jd:

                jd_matches += 1

        if jd_matches >= 2:

            detected_role_group = role

            break

    # --------------------------------------------------------
    # ROLE-SPECIFIC STRENGTH
    # --------------------------------------------------------

    if detected_role_group:

        relevant_resume_skills = []

        for skill in role_groups[
            detected_role_group
        ]:

            if (
                skill in resume
                and
                skill in jd
            ):

                relevant_resume_skills.append(
                    skill
                )

        if relevant_resume_skills:

            display_skills = ", ".join(
                skill.title()
                for skill in relevant_resume_skills[:5]
            )

            strengths.append(
                f"Your resume demonstrates "
                f"{detected_role_group.lower()} "
                f"skills relevant to this position, "
                f"including {display_skills}."
            )

    # --------------------------------------------------------
    # PROJECT
    # --------------------------------------------------------

    if (
        "project" in resume
        or
        "projects" in resume
    ):

        strengths.append(
            "Your resume includes project experience "
            "that provides practical evidence of "
            "your technical skills."
        )

    # --------------------------------------------------------
    # EXPERIENCE
    # --------------------------------------------------------

    if any(
        keyword in resume
        for keyword in [

            "experience",
            "internship",
            "intern",
            "work experience"
        ]
    ):

        strengths.append(
            "Your resume includes practical experience "
            "that supports your application for the "
            "target role."
        )

    # --------------------------------------------------------
    # EDUCATION
    # --------------------------------------------------------

    if any(
        keyword in resume
        for keyword in [

            "education",
            "b.tech",
            "btech",
            "b.e",
            "bachelor",
            "university",
            "college"
        ]
    ):

        strengths.append(
            "Your educational background is included "
            "in the resume."
        )

    # --------------------------------------------------------
    # LINKEDIN
    # --------------------------------------------------------

    if "linkedin" in resume:

        strengths.append(
            "Your LinkedIn profile is included."
        )

    # --------------------------------------------------------
    # GITHUB
    # --------------------------------------------------------

    if "github" in resume:

        strengths.append(
            "Your GitHub profile is included "
            "for showcasing technical projects."
        )

    # --------------------------------------------------------
    # MISSING SKILLS CONTEXT
    # --------------------------------------------------------

    if missing_skills:

        important_missing = missing_skills[:4]

        missing_text = ", ".join(
            skill.title()
            for skill in important_missing
        )

        strengths.append(
            f"Your resume covers part of the "
            f"target skill set, while further "
            f"alignment could be developed around "
            f"{missing_text}."
        )

    # --------------------------------------------------------
    # REMOVE DUPLICATES
    # --------------------------------------------------------

    unique_strengths = []

    seen = set()

    for item in strengths:

        key = item.lower().strip()

        if key not in seen:

            seen.add(
                key
            )

            unique_strengths.append(
                item
            )

    return unique_strengths[:8]


# ============================================================
# KEYWORD ANALYSIS
# ============================================================

def generate_keyword_analysis(
    resume_text,
    job_description
):

    skill_result = calculate_skill_match(
        resume_text,
        job_description
    )

    return {

        "target_keywords":
            len(
                skill_result[
                    "job_skills"
                ]
            ),

        "resume_keywords":
            len(
                skill_result[
                    "resume_skills"
                ]
            ),

        "matched_keywords":
            len(
                skill_result[
                    "matched"
                ]
            ),

        "missing_keywords":
            len(
                skill_result[
                    "missing"
                ]
            ),

        "matched":
            skill_result[
                "matched"
            ],

        "missing":
            skill_result[
                "missing"
            ],

        "additional":
            skill_result[
                "additional"
            ]
    }


# ============================================================
# INTERVIEW QUESTION BANK
# ============================================================

QUESTION_BANK = {

    "python": [

        "What is the difference between a list, tuple and set in Python?",

        "Explain Python functions and default arguments.",

        "What is object-oriented programming in Python?"
    ],

    "java": [

        "Explain the four principles of OOP in Java.",

        "What is the difference between ArrayList and LinkedList?",

        "What is exception handling in Java?"
    ],

    "sql": [

        "What is the difference between INNER JOIN and LEFT JOIN?",

        "What is normalization in databases?",

        "Write a SQL query to find duplicate records."
    ],

    "javascript": [

        "What is the difference between var, let and const?",

        "What are JavaScript promises?",

        "Explain the event loop in JavaScript."
    ],

    "react": [

        "What are React components?",

        "What is the difference between props and state?",

        "What are React hooks?"
    ],

    "typescript": [

        "What is TypeScript?",

        "What are interfaces in TypeScript?",

        "What is the difference between TypeScript and JavaScript?"
    ],

    "git": [

        "What is Git and why is it used?",

        "What is the difference between git merge and git rebase?",

        "Explain the Git branching workflow."
    ],

    "github": [

        "What is a pull request?",

        "How do you resolve a Git merge conflict?",

        "How is GitHub different from Git?"
    ],

    "docker": [

        "What is Docker?",

        "What is the difference between a Docker image and container?",

        "What is a Dockerfile?"
    ],

    "aws": [

        "What is cloud computing?",

        "What are some commonly used AWS services?",

        "What is the difference between EC2 and S3?"
    ],

    "azure": [

        "What is Microsoft Azure?",

        "What are common Azure services?",

        "What is the difference between Azure and AWS?"
    ],

    "mongodb": [

        "What is MongoDB?",

        "How is MongoDB different from a relational database?",

        "What are collections and documents?"
    ],

    "fastapi": [

        "What is FastAPI?",

        "What is an API endpoint?",

        "How does FastAPI validate request data?"
    ],

    "rest api": [

        "What are the HTTP methods used in REST APIs?",

        "What is the difference between GET and POST?",

        "What is a RESTful API?"
    ],

    "data structures": [

        "What is the difference between an array and linked list?",

        "How does a stack work?",

        "What is binary search?"
    ],

    "pandas": [

        "What is Pandas and why is it used in data analysis?",

        "What is the difference between a Series and DataFrame?",

        "How do you handle missing values using Pandas?"
    ],

    "numpy": [

        "What is NumPy?",

        "What is a NumPy array?",

        "Why is NumPy faster than normal Python lists?"
    ],

    "power bi": [

        "What is Power BI?",

        "What is the difference between a report and dashboard in Power BI?",

        "What is DAX?"
    ],

    "excel": [

        "What are PivotTables in Excel?",

        "What is the difference between VLOOKUP and XLOOKUP?",

        "How can Excel be used for data analysis?"
    ],

    "tableau": [

        "What is Tableau?",

        "What are dashboards in Tableau?",

        "How do filters work in Tableau?"
    ],

    "statistics": [

        "What is the difference between mean, median and mode?",

        "What is standard deviation?",

        "What is the difference between correlation and causation?"
    ],

    "business analysis": [

        "What is business analysis?",

        "How do you gather requirements from stakeholders?",

        "What is the difference between functional and non-functional requirements?"
    ],

    "requirements gathering": [

        "What techniques can be used for requirements gathering?",

        "How do you handle conflicting stakeholder requirements?",

        "How do you validate business requirements?"
    ]
}


# ============================================================
# INTERVIEW QUESTIONS
# ============================================================

def generate_interview_questions(
    job_description,
    resume_text
):

    job_skills = get_skills(
        job_description
    )

    questions = []

    for skill in job_skills:

        if skill in QUESTION_BANK:

            for question in QUESTION_BANK[
                skill
            ]:

                questions.append({

                    "category":
                        "Technical",

                    "skill":
                        skill,

                    "question":
                        question
                })

    if (
        "project" in resume_text.lower()
        or
        "projects" in resume_text.lower()
    ):

        questions.append({

            "category":
                "Project",

            "skill":
                "Resume",

            "question":
                "Explain one of the major projects mentioned in your resume."
        })

    if (
        "internship" in resume_text.lower()
        or
        "intern" in resume_text.lower()
    ):

        questions.append({

            "category":
                "Experience",

            "skill":
                "Resume",

            "question":
                "What did you learn during your internship?"
        })

    questions.extend([

        {
            "category":
                "HR",

            "skill":
                "General",

            "question":
                "Tell me about yourself."
        },

        {
            "category":
                "HR",

            "skill":
                "General",

            "question":
                "Why are you interested in this role?"
        },

        {
            "category":
                "HR",

            "skill":
                "General",

            "question":
                "Describe a challenge you faced and how you solved it."
        }
    ])

    unique_questions = []

    seen = set()

    for item in questions:

        question = item[
            "question"
        ]

        if question not in seen:

            seen.add(
                question
            )

            unique_questions.append(
                item
            )

    return unique_questions[:20]


# ============================================================
# UPLOAD RESUME
# ============================================================

@router.post("/upload-resume")
async def upload_resume(
    file: UploadFile = File(...)
):

    if not file.filename:

        raise HTTPException(
            status_code=400,
            detail="No file selected."
        )

    filename = file.filename.lower()

    if not (
        filename.endswith(".pdf")
        or
        filename.endswith(".docx")
    ):

        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are supported."
        )

    try:

        contents = await file.read()

        if not contents:

            raise HTTPException(
                status_code=400,
                detail="Uploaded file is empty."
            )

        resume_text = ""

        # ----------------------------------------------------
        # PDF
        # ----------------------------------------------------

        if filename.endswith(".pdf"):

            with pdfplumber.open(
                io.BytesIO(contents)
            ) as pdf:

                pages = []

                for page in pdf.pages:

                    pages.append(
                        page.extract_text()
                        or ""
                    )

                resume_text = "\n".join(
                    pages
                )

        # ----------------------------------------------------
        # DOCX
        # ----------------------------------------------------

        else:

            document = Document(
                io.BytesIO(contents)
            )

            paragraphs = []

            for paragraph in document.paragraphs:

                if paragraph.text.strip():

                    paragraphs.append(
                        paragraph.text
                    )

            resume_text = "\n".join(
                paragraphs
            )

        resume_text = resume_text.strip()

        if not resume_text:

            raise HTTPException(
                status_code=400,
                detail="Could not extract text from resume."
            )

        return {

            "status":
                "success",

            "filename":
                file.filename,

            "resume_text":
                resume_text,

            "text":
                resume_text,

            "message":
                "Resume uploaded and text extracted successfully."
        }

    except HTTPException:

        raise

    except Exception as e:

        print(
            f"Resume upload error: {e}"
        )

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ============================================================
# MATCH JOB
# ============================================================

@router.post("/match-job")
async def match_job(
    request: JobRequest
):

    breakdown = calculate_match_score_breakdown(
        request.resume_text,
        request.job_description
    )

    return {

        "status":
            "success",

        "match_score":
            breakdown["total_score"],

        "match_breakdown":
            breakdown,

        "resume_skills":
            breakdown["resume_skills"],

        "job_skills":
            breakdown["job_skills"],

        "matched_skills":
            breakdown["matched_skills"],

        "missing_skills":
            breakdown["missing_skills"],

        "additional_skills":
            breakdown["additional_skills"]
    }


# ============================================================
# SKILL GAP
# ============================================================

@router.post("/skill-gap")
async def skill_gap(
    request: SkillGapRequest
):

    skill_result = calculate_skill_match(
        request.resume_text,
        request.job_description
    )

    return {

        "status":
            "success",

        "resume_skill_count":
            len(
                skill_result[
                    "resume_skills"
                ]
            ),

        "job_skill_count":
            len(
                skill_result[
                    "job_skills"
                ]
            ),

        "matched_skill_count":
            len(
                skill_result[
                    "matched"
                ]
            ),

        "missing_skill_count":
            len(
                skill_result[
                    "missing"
                ]
            ),

        "matched_skills":
            skill_result[
                "matched"
            ],

        "missing_skills":
            skill_result[
                "missing"
            ],

        "additional_skills":
            skill_result[
                "additional"
            ]
    }


# ============================================================
# RECOMMEND CAREER
# ============================================================

@router.post("/recommend-career")
async def recommend_career(
    request: CareerRequest
):

    careers = get_career_recommendations(
        request.resume_text
    )

    return {

        "status":
            "success",

        "recommended_roles":
            careers
    }


# ============================================================
# RESUME FEEDBACK
# ============================================================

@router.post("/resume-feedback")
async def resume_feedback(
    request: FeedbackRequest
):

    feedback = generate_resume_feedback(
        request.resume_text,
        "",
        [],
        []
    )

    return {

        "status":
            "success",

        "feedback":
            feedback
    }


# ============================================================
# LEARNING RECOMMENDATIONS
# ============================================================

@router.post(
    "/learning-recommendations"
)
async def learning_recommendations(
    request: LearningRecommendationRequest
):

    recommendations = (
        get_learning_recommendations(
            request.missing_skills
        )
    )

    return {

        "status":
            "success",

        "missing_skills":
            request.missing_skills,

        "recommendations":
            recommendations
    }


# ============================================================
# ANALYZE RESUME
# ============================================================

@router.post("/analyze-resume")
async def analyze_resume(
    request: JobRequest
):

    resume_text = request.resume_text

    job_description = (
        request.job_description
    )

    # --------------------------------------------------------
    # MATCH SCORE BREAKDOWN
    # --------------------------------------------------------

    match_breakdown = (
        calculate_match_score_breakdown(
            resume_text,
            job_description
        )
    )

    match_score = (
        match_breakdown[
            "total_score"
        ]
    )

    resume_skills = (
        match_breakdown[
            "resume_skills"
        ]
    )

    job_skills = (
        match_breakdown[
            "job_skills"
        ]
    )

    matched_skills = (
        match_breakdown[
            "matched_skills"
        ]
    )

    missing_skills = (
        match_breakdown[
            "missing_skills"
        ]
    )

    additional_skills = (
        match_breakdown[
            "additional_skills"
        ]
    )

    # --------------------------------------------------------
    # ATS
    # --------------------------------------------------------

    try:

        ats_result = calculate_ats_score(
            resume_text,
            matched_skills,
            missing_skills
        )

    except Exception as e:

        print(
            f"ATS score warning: {e}"
        )

        ats_result = {

            "score":
                0,

            "rating":
                "Needs Improvement",

            "feedback":
                [],

            "breakdown":
                {}
        }

    # --------------------------------------------------------
    # CAREER
    # --------------------------------------------------------

    recommended_roles = (
        get_career_recommendations(
            resume_text
        )
    )

    # --------------------------------------------------------
    # LEARNING
    # --------------------------------------------------------

    learning_recommendations = (
        get_learning_recommendations(
            missing_skills
        )
    )

    # --------------------------------------------------------
    # STRENGTHS
    # --------------------------------------------------------

    strengths = generate_resume_strengths(

        resume_text,

        job_description,

        matched_skills,

        missing_skills
    )

    # --------------------------------------------------------
    # KEYWORDS
    # --------------------------------------------------------

    keyword_analysis = (
        generate_keyword_analysis(
            resume_text,
            job_description
        )
    )

    # --------------------------------------------------------
    # INTERVIEW
    # --------------------------------------------------------

    interview_questions = (
        generate_interview_questions(
            job_description,
            resume_text
        )
    )

    # --------------------------------------------------------
    # FEEDBACK
    # --------------------------------------------------------

    feedback = generate_resume_feedback(

        resume_text,

        job_description,

        matched_skills,

        missing_skills
    )

    # --------------------------------------------------------
    # SKILL GAP CHART
    # --------------------------------------------------------

    skill_gap_chart = {

        "matched":
            len(matched_skills),

        "missing":
            len(missing_skills)
    }

    # --------------------------------------------------------
    # SUMMARY
    # --------------------------------------------------------

    summary = {

        "resume_skills":
            len(resume_skills),

        "job_skills":
            len(job_skills),

        "matched_skills":
            len(matched_skills),

        "missing_skills":
            len(missing_skills),

        "match_score":
            match_score,

        "ats_score":
            ats_result.get(
                "score",
                0
            ),

        "ats_rating":
            ats_result.get(
                "rating",
                "Needs Improvement"
            )
    }

    # --------------------------------------------------------
    # FINAL RESULT
    # --------------------------------------------------------

    result = {

        "status":
            "success",

        "summary":
            summary,

        "match_score":
            match_score,

        "match_breakdown":
            match_breakdown,

        "ats_score":
            ats_result.get(
                "score",
                0
            ),

        "ats_rating":
            ats_result.get(
                "rating",
                "Needs Improvement"
            ),

        "ats_breakdown":
            ats_result.get(
                "breakdown",
                {}
            ),

        "ats_feedback":
            ats_result.get(
                "feedback",
                []
            ),

        "resume_skill_count":
            len(resume_skills),

        "job_skill_count":
            len(job_skills),

        "matched_skill_count":
            len(matched_skills),

        "missing_skill_count":
            len(missing_skills),

        "matched_skills":
            matched_skills,

        "missing_skills":
            missing_skills,

        "additional_skills":
            additional_skills,

        "skill_gap_chart":
            skill_gap_chart,

        "recommended_roles":
            recommended_roles,

        "strengths":
            strengths,

        "keyword_analysis":
            keyword_analysis,

        "learning_recommendations":
            learning_recommendations,

        "feedback":
            feedback,

        "interview_questions":
            interview_questions
    }

    # --------------------------------------------------------
    # POWER BI
    # --------------------------------------------------------

    if export_to_powerbi is not None:

        try:

            export_to_powerbi(
                result
            )

        except Exception as e:

            print(
                f"Power BI export warning: {e}"
            )

    return result


# ============================================================
# DOWNLOAD PDF REPORT
# ============================================================

@router.post(
    "/download-report"
)
async def download_report(
    request: dict
):

    try:

        from reportlab.lib.pagesizes import A4

        from reportlab.platypus import (
            SimpleDocTemplate,
            Paragraph,
            Spacer,
            Table,
            TableStyle
        )

        from reportlab.lib import colors

        from reportlab.lib.styles import (
            getSampleStyleSheet
        )

        from reportlab.lib.enums import (
            TA_CENTER
        )

        buffer = io.BytesIO()

        document = SimpleDocTemplate(

            buffer,

            pagesize=A4,

            rightMargin=40,

            leftMargin=40,

            topMargin=40,

            bottomMargin=40
        )

        styles = getSampleStyleSheet()

        title_style = styles[
            "Title"
        ]

        title_style.alignment = (
            TA_CENTER
        )

        heading_style = styles[
            "Heading2"
        ]

        normal_style = styles[
            "BodyText"
        ]

        story = []

        # ----------------------------------------------------
        # TITLE
        # ----------------------------------------------------

        story.append(
            Paragraph(
                "AI Career Recommendation Report",
                title_style
            )
        )

        story.append(
            Spacer(1, 20)
        )

        # ----------------------------------------------------
        # SUMMARY
        # ----------------------------------------------------

        story.append(
            Paragraph(
                "Analysis Summary",
                heading_style
            )
        )

        summary = request.get(
            "summary",
            {}
        )

        score_data = [

            [
                "Job Match",
                f"{summary.get(
                    'match_score',
                    request.get(
                        'match_score',
                        0
                    )
                )}%"
            ],

            [
                "ATS Score",
                f"{summary.get(
                    'ats_score',
                    request.get(
                        'ats_score',
                        0
                    )
                )}%"
            ],

            [
                "Matched Skills",
                str(
                    summary.get(
                        "matched_skills",
                        request.get(
                            "matched_skill_count",
                            0
                        )
                    )
                )
            ],

            [
                "Missing Skills",
                str(
                    summary.get(
                        "missing_skills",
                        request.get(
                            "missing_skill_count",
                            0
                        )
                    )
                )
            ]
        ]

        table = Table(
            score_data,
            colWidths=[
                220,
                220
            ]
        )

        table.setStyle(
            TableStyle([

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey
                ),

                (
                    "BACKGROUND",
                    (0, 0),
                    (0, -1),
                    colors.lightgrey
                ),

                (
                    "PADDING",
                    (0, 0),
                    (-1, -1),
                    8
                )
            ])
        )

        story.append(
            table
        )

        story.append(
            Spacer(1, 20)
        )

        # ----------------------------------------------------
        # MATCH BREAKDOWN
        # ----------------------------------------------------

        story.append(
            Paragraph(
                "Job Match Score Breakdown",
                heading_style
            )
        )

        breakdown = request.get(
            "match_breakdown",
            {}
        )

        breakdown_data = [

            [
                "Factor",
                "Score"
            ],

            [
                "Technical Skill Match",
                f"{breakdown.get(
                    'skill_match',
                    0
                )}/40"
            ],

            [
                "Semantic JD Match",
                f"{breakdown.get(
                    'semantic_match',
                    0
                )}/30"
            ],

            [
                "Project Relevance",
                f"{breakdown.get(
                    'project_relevance',
                    0
                )}/15"
            ],

            [
                "Experience Relevance",
                f"{breakdown.get(
                    'experience_relevance',
                    0
                )}/10"
            ],

            [
                "Education Relevance",
                f"{breakdown.get(
                    'education_relevance',
                    0
                )}/5"
            ],

            [
                "Total",
                f"{breakdown.get(
                    'total_score',
                    0
                )}/100"
            ]
        ]

        breakdown_table = Table(
            breakdown_data,
            colWidths=[
                300,
                140
            ]
        )

        breakdown_table.setStyle(
            TableStyle([

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey
                ),

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.lightgrey
                ),

                (
                    "BACKGROUND",
                    (0, -1),
                    (-1, -1),
                    colors.lightgrey
                ),

                (
                    "PADDING",
                    (0, 0),
                    (-1, -1),
                    8
                )
            ])
        )

        story.append(
            breakdown_table
        )

        story.append(
            Spacer(1, 20)
        )

        # ----------------------------------------------------
        # MATCHED SKILLS
        # ----------------------------------------------------

        story.append(
            Paragraph(
                "Matched Skills",
                heading_style
            )
        )

        matched_text = ", ".join(
            request.get(
                "matched_skills",
                []
            )
        )

        story.append(
            Paragraph(
                matched_text or "None",
                normal_style
            )
        )

        story.append(
            Spacer(1, 12)
        )

        # ----------------------------------------------------
        # MISSING SKILLS
        # ----------------------------------------------------

        story.append(
            Paragraph(
                "Missing Skills",
                heading_style
            )
        )

        missing_text = ", ".join(
            request.get(
                "missing_skills",
                []
            )
        )

        story.append(
            Paragraph(
                missing_text or "None",
                normal_style
            )
        )

        story.append(
            Spacer(1, 12)
        )

        # ----------------------------------------------------
        # ADDITIONAL SKILLS
        # ----------------------------------------------------

        story.append(
            Paragraph(
                "Additional Resume Skills",
                heading_style
            )
        )

        additional_text = ", ".join(
            request.get(
                "additional_skills",
                []
            )
        )

        story.append(
            Paragraph(
                additional_text or "None",
                normal_style
            )
        )

        story.append(
            Spacer(1, 12)
        )

        # ----------------------------------------------------
        # CAREER ROLES
        # ----------------------------------------------------

        story.append(
            Paragraph(
                "Recommended Career Roles",
                heading_style
            )
        )

        for role in request.get(
            "recommended_roles",
            []
        ):

            if isinstance(
                role,
                dict
            ):

                role_text = role.get(
                    "role",
                    role.get(
                        "title",
                        ""
                    )
                )

            else:

                role_text = str(
                    role
                )

            story.append(
                Paragraph(
                    f"• {role_text}",
                    normal_style
                )
            )

        story.append(
            Spacer(1, 12)
        )

        # ----------------------------------------------------
        # STRENGTHS
        # ----------------------------------------------------

        story.append(
            Paragraph(
                "Resume Strengths",
                heading_style
            )
        )

        for item in request.get(
            "strengths",
            []
        ):

            story.append(
                Paragraph(
                    f"• {item}",
                    normal_style
                )
            )

        story.append(
            Spacer(1, 12)
        )

        # ----------------------------------------------------
        # FEEDBACK
        # ----------------------------------------------------

        story.append(
            Paragraph(
                "Resume Improvement Suggestions",
                heading_style
            )
        )

        for item in request.get(
            "feedback",
            []
        ):

            story.append(
                Paragraph(
                    f"• {item}",
                    normal_style
                )
            )

        story.append(
            Spacer(1, 12)
        )

        # ----------------------------------------------------
        # LEARNING
        # ----------------------------------------------------

        story.append(
            Paragraph(
                "Recommended Learning",
                heading_style
            )
        )

        learning_items = request.get(
            "learning_recommendations",
            []
        )

        for item in learning_items:

            if isinstance(
                item,
                dict
            ):

                topic = item.get(
                    "topic",
                    ""
                )

                skill = item.get(
                    "skill",
                    ""
                )

                story.append(
                    Paragraph(
                        f"• {topic} "
                        f"(Missing skill: {skill})",
                        normal_style
                    )
                )

            else:

                story.append(
                    Paragraph(
                        f"• {item}",
                        normal_style
                    )
                )

        story.append(
            Spacer(1, 12)
        )

        # ----------------------------------------------------
        # INTERVIEW
        # ----------------------------------------------------

        story.append(
            Paragraph(
                "Interview Preparation",
                heading_style
            )
        )

        questions = request.get(
            "interview_questions",
            []
        )

        for index, item in enumerate(
            questions,
            start=1
        ):

            if isinstance(
                item,
                dict
            ):

                question = item.get(
                    "question",
                    ""
                )

                category = item.get(
                    "category",
                    ""
                )

                story.append(
                    Paragraph(
                        f"{index}. "
                        f"[{category}] "
                        f"{question}",
                        normal_style
                    )
                )

            else:

                story.append(
                    Paragraph(
                        f"{index}. {item}",
                        normal_style
                    )
                )

        # ----------------------------------------------------
        # BUILD PDF
        # ----------------------------------------------------

        document.build(
            story
        )

        buffer.seek(0)

        return StreamingResponse(

            buffer,

            media_type="application/pdf",

            headers={

                "Content-Disposition":
                    "attachment; "
                    "filename="
                    "career_analysis_report.pdf"
            }
        )

    except Exception as e:

        print(
            f"PDF report error: {e}"
        )

        raise HTTPException(

            status_code=500,

            detail=(
                "Could not generate "
                f"report: {str(e)}"
            )
        )