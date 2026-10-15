import re


# ============================================================
# SKILL ALIASES
# ============================================================

SKILL_ALIASES = {

    # ========================================================
    # PROGRAMMING
    # ========================================================

    "python": "python",
    "python3": "python",

    "java": "java",

    "javascript": "javascript",
    "javascript es6": "javascript",
    "js": "javascript",
    "es6": "javascript",

    "typescript": "typescript",
    "ts": "typescript",

    "c++": "c++",
    "cpp": "c++",

    "c#": "c#",
    "csharp": "c#",

    # ========================================================
    # WEB DEVELOPMENT
    # ========================================================

    "html": "html",
    "html5": "html",

    "css": "css",
    "css3": "css",

    "react": "react",
    "react.js": "react",
    "reactjs": "react",

    "react hooks": "react hooks",
    "react.js hooks": "react hooks",

    "react router": "react router",

    "redux": "redux",
    "redux toolkit": "redux",

    "angular": "angular",
    "angular.js": "angular",
    "angularjs": "angular",

    "vue": "vue",
    "vue.js": "vue",

    "bootstrap": "bootstrap",

    "tailwind": "tailwind css",
    "tailwind css": "tailwind css",

    "material ui": "material ui",
    "mui": "material ui",

    "vite": "vite",

    # ========================================================
    # BACKEND
    # ========================================================

    "node": "node.js",
    "nodejs": "node.js",
    "node.js": "node.js",

    "express": "express",
    "express.js": "express",

    "fastapi": "fastapi",
    "fast api": "fastapi",

    "django": "django",
    "flask": "flask",

    "spring boot": "spring boot",
    "spring": "spring boot",

    # ========================================================
    # API DEVELOPMENT
    # ========================================================

    "api": "api",
    "apis": "api",

    "rest api": "rest api",
    "rest apis": "rest api",

    "restful api": "rest api",
    "restful apis": "rest api",

    "api development": "api development",
    "api integration": "api integration",

    "json": "json",

    # ========================================================
    # DATABASES
    # ========================================================

    "sql": "sql",
    "sql server": "sql",
    "t-sql": "sql",
    "transact-sql": "sql",

    "mysql": "mysql",

    "postgres": "postgresql",
    "postgresql": "postgresql",

    "oracle": "oracle",
    "oracle sql": "oracle",

    "mongodb": "mongodb",
    "mongo": "mongodb",

    "redis": "redis",

    "nosql": "nosql",

    # ========================================================
    # VERSION CONTROL
    # ========================================================

    "git": "git",

    "github": "github",
    "git hub": "github",

    "gitlab": "gitlab",

    "bitbucket": "bitbucket",

    # ========================================================
    # DATA ANALYSIS
    # ========================================================

    "pandas": "pandas",

    "numpy": "numpy",

    "data analysis": "data analysis",
    "data analyst": "data analysis",

    "data analytics": "data analytics",

    "data visualization": "data visualization",
    "data viz": "data visualization",

    "data cleaning": "data cleaning",

    "data preprocessing": "data preprocessing",

    "exploratory data analysis":
        "exploratory data analysis",

    "eda": "exploratory data analysis",

    "statistics": "statistics",

    "statistical analysis": "statistics",

    "excel": "excel",
    "microsoft excel": "excel",

    "power bi": "power bi",
    "powerbi": "power bi",

    "tableau": "tableau",

    "matplotlib": "matplotlib",

    "plotly": "plotly",

    "seaborn": "seaborn",

    "business intelligence":
        "business intelligence",

    "bi": "business intelligence",

    # ========================================================
    # MACHINE LEARNING / AI
    # ========================================================

    "artificial intelligence":
        "artificial intelligence",

    "ai": "artificial intelligence",

    "machine learning":
        "machine learning",

    "ml": "machine learning",

    "deep learning":
        "deep learning",

    "dl": "deep learning",

    "scikit-learn":
        "scikit-learn",

    "sklearn":
        "scikit-learn",

    "tensorflow":
        "tensorflow",

    "pytorch":
        "pytorch",

    "nlp":
        "nlp",

    "natural language processing":
        "nlp",

    "computer vision":
        "computer vision",

    "opencv":
        "opencv",

    "bert":
        "bert",

    "transformers":
        "transformers",

    # ========================================================
    # DATA STRUCTURES / PROGRAMMING CONCEPTS
    # ========================================================

    "data structures":
        "data structures",

    "algorithms":
        "algorithms",

    "data structures and algorithms":
        "data structures and algorithms",

    "dsa":
        "data structures and algorithms",

    "object oriented programming":
        "object oriented programming",

    "object-oriented programming":
        "object oriented programming",

    "oop":
        "object oriented programming",

    "problem solving":
        "problem solving",

    "problem-solving":
        "problem solving",

    # ========================================================
    # CLOUD
    # ========================================================

    "aws": "aws",
    "amazon web services": "aws",

    "azure": "azure",
    "microsoft azure": "azure",

    "gcp": "gcp",
    "google cloud": "gcp",
    "google cloud platform": "gcp",

    "cloud computing":
        "cloud computing",

    # ========================================================
    # DEVOPS
    # ========================================================

    "docker": "docker",

    "kubernetes": "kubernetes",

    "ci/cd": "ci/cd",
    "cicd": "ci/cd",

    "continuous integration":
        "ci/cd",

    "continuous deployment":
        "ci/cd",

    # ========================================================
    # DATA ENGINEERING
    # ========================================================

    "data engineering":
        "data engineering",

    "etl":
        "etl",

    "elt":
        "etl/elt",

    "etl/elt":
        "etl/elt",

    "data pipeline":
        "data pipelines",

    "data pipelines":
        "data pipelines",

    "data warehouse":
        "data warehousing",

    "data warehousing":
        "data warehousing",

    "data lake":
        "data lake",

    "lakehouse":
        "lakehouse",

    "data lakehouse":
        "lakehouse",

    "data modeling":
        "data modeling",

    "dimensional modeling":
        "dimensional modeling",

    "star schema":
        "star schema",

    "snowflake schema":
        "snowflake schema",

    "pyspark":
        "pyspark",

    "spark":
        "apache spark",

    "apache spark":
        "apache spark",

    "spark sql":
        "spark sql",

    # ========================================================
    # GENERATIVE AI
    # ========================================================

    "generative ai":
        "generative ai",

    "genai":
        "generative ai",

    "gen ai":
        "generative ai",

    "llm":
        "llm",

    "large language model":
        "llm",

    "large language models":
        "llm",

    "rag":
        "rag",

    "retrieval augmented generation":
        "rag",

    "retrieval-augmented generation":
        "rag",

    "prompt engineering":
        "prompt engineering",

    # ========================================================
    # PROFESSIONAL SKILLS
    # ========================================================

    "communication":
        "communication",

    "verbal communication":
        "communication",

    "written communication":
        "communication",

    "teamwork":
        "teamwork",

    "team collaboration":
        "teamwork",

    "collaboration":
        "teamwork",

    "analytical thinking":
        "analytical thinking",

    "leadership":
        "leadership",

    "time management":
        "time management",

    # ========================================================
    # METHODOLOGIES
    # ========================================================

    "agile":
        "agile",

    "scrum":
        "scrum",

}


# ============================================================
# NORMALIZE TEXT
# ============================================================

def normalize_text(text):
    """
    Normalize text so that skill matching becomes
    more reliable.
    """

    if not text:
        return ""

    text = str(text).lower()

    # Normalize Unicode dashes
    text = text.replace("–", "-")
    text = text.replace("—", "-")

    # Normalize underscores
    text = text.replace("_", " ")

    # Normalize multiple spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# ============================================================
# NORMALIZE SINGLE SKILL
# ============================================================

def normalize_skill(skill):
    """
    Convert a skill/alias into its standard skill name.
    """

    if not skill:
        return None

    skill = normalize_text(skill)

    # Direct alias match
    if skill in SKILL_ALIASES:
        return SKILL_ALIASES[skill]

    # Small formatting cleanup
    skill = skill.replace(" .js", ".js")

    if skill in SKILL_ALIASES:
        return SKILL_ALIASES[skill]

    # Return cleaned original if no alias exists
    return skill


# ============================================================
# NORMALIZE SKILL LIST
# ============================================================

def normalize_skills(skills):
    """
    Normalize a list of skills and remove duplicates.
    """

    if not skills:
        return []

    normalized = []
    seen = set()

    for skill in skills:

        value = normalize_skill(skill)

        if not value:
            continue

        if value not in seen:

            normalized.append(value)

            seen.add(value)

    return normalized


# ============================================================
# EXTRACT NORMALIZED SKILLS
# ============================================================

def extract_normalized_skills(
    text,
    skills_list=None
):
    """
    Extract skills from text.

    If skills_list is provided, those skills are checked
    against the text.

    If skills_list is empty or unavailable, the complete
    alias dictionary is used.
    """

    if not text:
        return []

    normalized_text = normalize_text(text)

    # --------------------------------------------------------
    # Build candidate skill list
    # --------------------------------------------------------

    candidates = []

    if skills_list:

        candidates.extend(
            skills_list
        )

    # Always include known aliases.
    # This makes the extractor more robust even when
    # the external skill extractor misses a skill.
    candidates.extend(
        SKILL_ALIASES.keys()
    )

    # Remove duplicates while preserving order
    unique_candidates = []

    seen_candidates = set()

    for skill in candidates:

        if not skill:
            continue

        normalized_candidate = normalize_text(
            skill
        )

        if not normalized_candidate:
            continue

        if normalized_candidate in seen_candidates:
            continue

        seen_candidates.add(
            normalized_candidate
        )

        unique_candidates.append(
            normalized_candidate
        )

    detected = []

    # --------------------------------------------------------
    # Search skills
    # --------------------------------------------------------

    for skill in unique_candidates:

        pattern = re.escape(skill)

        try:

            found = re.search(
                rf"(?<!\w){pattern}(?!\w)",
                normalized_text,
                re.IGNORECASE
            )

        except re.error:

            found = None

        if found:

            normalized_skill_name = (
                normalize_skill(skill)
            )

            if normalized_skill_name:

                detected.append(
                    normalized_skill_name
                )

    return normalize_skills(
        detected
    )


# ============================================================
# COMPARE RESUME AND JD SKILLS
# ============================================================

def compare_normalized_skills(
    resume_skills,
    jd_skills
):
    """
    Compare resume skills with JD skills.

    IMPORTANT:
    The return structure is compatible with the
    existing jobs.py file.
    """

    # --------------------------------------------------------
    # Normalize resume skills
    # --------------------------------------------------------

    normalized_resume = normalize_skills(
        resume_skills
    )

    # --------------------------------------------------------
    # Normalize JD skills
    # --------------------------------------------------------

    normalized_job = normalize_skills(
        jd_skills
    )

    # Convert to sets for comparison
    resume_set = set(
        normalized_resume
    )

    job_set = set(
        normalized_job
    )

    # --------------------------------------------------------
    # Matched skills
    # --------------------------------------------------------

    matched = sorted(
        resume_set.intersection(
            job_set
        )
    )

    # --------------------------------------------------------
    # Missing skills
    # --------------------------------------------------------

    missing = sorted(
        job_set.difference(
            resume_set
        )
    )

    # --------------------------------------------------------
    # Additional resume skills
    # --------------------------------------------------------

    additional = sorted(
        resume_set.difference(
            job_set
        )
    )

    # --------------------------------------------------------
    # RETURN FORMAT
    # --------------------------------------------------------

    return {

        # Existing jobs.py expects these
        "resume_skills":
            sorted(
                list(resume_set)
            ),

        "job_skills":
            sorted(
                list(job_set)
            ),

        "matched":
            matched,

        "missing":
            missing,

        "additional":
            additional
    }