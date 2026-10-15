
from urllib.parse import quote_plus


# ============================================================
# LEARNING RESOURCES
# Direct documentation and learning guides for each skill
# ============================================================

LEARNING_RESOURCES = {
    # Programming
    "python": {
        "title": "Python Official Tutorial",
        "url": "https://docs.python.org/3/tutorial/"
    },
    "java": {
        "title": "Java Tutorials",
        "url": "https://dev.java/learn/"
    },
    "javascript": {
        "title": "JavaScript Guide",
        "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide"
    },
    "typescript": {
        "title": "TypeScript Handbook",
        "url": "https://www.typescriptlang.org/docs/handbook/"
    },
    "c++": {
        "title": "Learn C++",
        "url": "https://www.learncpp.com/"
    },
    "c#": {
        "title": "C# Documentation",
        "url": "https://learn.microsoft.com/en-us/dotnet/csharp/"
    },

    # Frontend
    "html": {
        "title": "Learn HTML",
        "url": "https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content"
    },
    "css": {
        "title": "Learn CSS",
        "url": "https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics"
    },
    "react": {
        "title": "React Learn",
        "url": "https://react.dev/learn"
    },
    "react hooks": {
        "title": "React Hooks",
        "url": "https://react.dev/reference/react/hooks"
    },
    "react router": {
        "title": "React Router Tutorial",
        "url": "https://reactrouter.com/start/declarative/installation"
    },
    "redux": {
        "title": "Redux Toolkit Quick Start",
        "url": "https://redux.js.org/tutorials/quick-start"
    },
    "bootstrap": {
        "title": "Bootstrap Getting Started",
        "url": "https://getbootstrap.com/docs/5.3/getting-started/introduction/"
    },
    "tailwind css": {
        "title": "Tailwind CSS Documentation",
        "url": "https://tailwindcss.com/docs/installation"
    },
    "angular": {
        "title": "Angular Tutorials",
        "url": "https://angular.dev/tutorials"
    },
    "vue": {
        "title": "Vue Tutorial",
        "url": "https://vuejs.org/tutorial/"
    },
    "material ui": {
        "title": "Material UI Getting Started",
        "url": "https://mui.com/material-ui/getting-started/"
    },
    "vite": {
        "title": "Vite Guide",
        "url": "https://vite.dev/guide/"
    },
    "figma": {
        "title": "Figma Design Resources",
        "url": "https://help.figma.com/"
    },

    # Backend and APIs
    "node.js": {
        "title": "Node.js Learning Guide",
        "url": "https://nodejs.org/en/learn/getting-started/introduction-to-nodejs"
    },
    "express": {
        "title": "Express.js Getting Started",
        "url": "https://expressjs.com/en/starter/installing.html"
    },
    "fastapi": {
        "title": "FastAPI Tutorial",
        "url": "https://fastapi.tiangolo.com/tutorial/"
    },
    "django": {
        "title": "Django Tutorial",
        "url": "https://docs.djangoproject.com/en/stable/intro/tutorial01/"
    },
    "flask": {
        "title": "Flask Quickstart",
        "url": "https://flask.palletsprojects.com/en/stable/quickstart/"
    },
    "spring boot": {
        "title": "Spring Boot Guides",
        "url": "https://spring.io/guides"
    },
    "rest api": {
        "title": "REST API Concepts",
        "url": "https://developer.mozilla.org/en-US/docs/Glossary/REST"
    },
    "api": {
        "title": "HTTP and APIs",
        "url": "https://developer.mozilla.org/en-US/docs/Web/HTTP"
    },
    "json": {
        "title": "Learn JSON",
        "url": "https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/JSON"
    },

    # Databases and SQL
    "sql": {
        "title": "Query Data with SQL",
        "url": "https://learn.microsoft.com/en-us/training/paths/get-started-querying-with-transact-sql/"
    },
    "mysql": {
        "title": "MySQL Documentation",
        "url": "https://dev.mysql.com/doc/"
    },
    "postgresql": {
        "title": "PostgreSQL Tutorial",
        "url": "https://www.postgresql.org/docs/current/tutorial.html"
    },
    "oracle": {
        "title": "Oracle Database Documentation",
        "url": "https://docs.oracle.com/en/database/"
    },
    "mongodb": {
        "title": "MongoDB University",
        "url": "https://learn.mongodb.com/"
    },
    "nosql": {
        "title": "NoSQL Database Learning",
        "url": "https://www.mongodb.com/resources/basics/databases/nosql-explained"
    },
    "redis": {
        "title": "Redis University",
        "url": "https://university.redis.io/"
    },

    # Version control
    "git": {
        "title": "Pro Git Book",
        "url": "https://git-scm.com/book/en/v2"
    },
    "github": {
        "title": "GitHub Skills",
        "url": "https://skills.github.com/"
    },
    "gitlab": {
        "title": "GitLab Tutorials",
        "url": "https://docs.gitlab.com/tutorials/"
    },

    # Data analysis
    "pandas": {
        "title": "Pandas Getting Started",
        "url": "https://pandas.pydata.org/docs/getting_started/index.html"
    },
    "numpy": {
        "title": "NumPy Learn",
        "url": "https://numpy.org/learn/"
    },
    "excel": {
        "title": "Excel Help and Learning",
        "url": "https://support.microsoft.com/en-us/excel"
    },
    "power bi": {
        "title": "Power BI Learning Paths",
        "url": "https://learn.microsoft.com/en-us/training/powerplatform/power-bi"
    },
    "tableau": {
        "title": "Tableau Free Training",
        "url": "https://www.tableau.com/learn/training"
    },
    "matplotlib": {
        "title": "Matplotlib Tutorials",
        "url": "https://matplotlib.org/stable/tutorials/"
    },
    "plotly": {
        "title": "Plotly Python Tutorials",
        "url": "https://plotly.com/python/"
    },
    "seaborn": {
        "title": "Seaborn Tutorial",
        "url": "https://seaborn.pydata.org/tutorial.html"
    },
    "statistics": {
        "title": "Statistics and Probability",
        "url": "https://www.khanacademy.org/math/statistics-probability"
    },
    "data visualization": {
        "title": "Data Visualization with Power BI",
        "url": "https://learn.microsoft.com/en-us/training/paths/prepare-visualize-data-power-bi/"
    },
    "data cleaning": {
        "title": "Prepare Data with Power BI",
        "url": "https://learn.microsoft.com/en-us/training/paths/prepare-data-power-bi/"
    },
    "data preprocessing": {
        "title": "Prepare Data with Power BI",
        "url": "https://learn.microsoft.com/en-us/training/paths/prepare-data-power-bi/"
    },
    "exploratory data analysis": {
        "title": "Exploratory Data Analysis Learning",
        "url": "https://www.kaggle.com/learn"
    },
    "business intelligence": {
        "title": "Power BI Fundamentals",
        "url": "https://learn.microsoft.com/en-us/power-bi/fundamentals/"
    },
    "data analysis": {
        "title": "Data Analysis Courses",
        "url": "https://www.kaggle.com/learn"
    },
    "data analytics": {
        "title": "Data Analytics Courses",
        "url": "https://www.coursera.org/browse/data-science/data-analysis"
    },

    # AI and machine learning
    "machine learning": {
        "title": "Scikit-learn Getting Started",
        "url": "https://scikit-learn.org/stable/getting_started.html"
    },
    "scikit-learn": {
        "title": "Scikit-learn Tutorials",
        "url": "https://scikit-learn.org/stable/tutorial/index.html"
    },
    "deep learning": {
        "title": "Deep Learning Specialization Resources",
        "url": "https://www.deeplearning.ai/"
    },
    "tensorflow": {
        "title": "TensorFlow Tutorials",
        "url": "https://www.tensorflow.org/tutorials"
    },
    "pytorch": {
        "title": "PyTorch Tutorials",
        "url": "https://pytorch.org/tutorials/"
    },
    "nlp": {
        "title": "Hugging Face NLP Course",
        "url": "https://huggingface.co/learn/llm-course/chapter1/1"
    },
    "bert": {
        "title": "Hugging Face Transformers Course",
        "url": "https://huggingface.co/learn/llm-course/chapter1/1"
    },
    "transformers": {
        "title": "Hugging Face Transformers Course",
        "url": "https://huggingface.co/learn/llm-course/chapter1/1"
    },
    "opencv": {
        "title": "OpenCV Python Tutorials",
        "url": "https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html"
    },
    "computer vision": {
        "title": "Computer Vision Learning",
        "url": "https://huggingface.co/learn"
    },

    # Data engineering
    "data engineering": {
        "title": "Data Engineering Learning Resources",
        "url": "https://www.datacamp.com/category/data-engineering"
    },
    "pyspark": {
        "title": "PySpark Getting Started",
        "url": "https://spark.apache.org/docs/latest/api/python/getting_started/index.html"
    },
    "apache spark": {
        "title": "Apache Spark Quick Start",
        "url": "https://spark.apache.org/docs/latest/quick-start.html"
    },
    "spark sql": {
        "title": "Spark SQL Guide",
        "url": "https://spark.apache.org/docs/latest/sql-getting-started.html"
    },
    "etl": {
        "title": "ETL Learning Resources",
        "url": "https://learn.microsoft.com/en-us/training/"
    },
    "etl/elt": {
        "title": "ETL and ELT Learning Resources",
        "url": "https://learn.microsoft.com/en-us/training/"
    },
    "data pipelines": {
        "title": "Data Pipeline Learning Resources",
        "url": "https://learn.microsoft.com/en-us/training/"
    },
    "data warehousing": {
        "title": "Data Warehousing Learning Resources",
        "url": "https://learn.microsoft.com/en-us/training/"
    },

    # Cloud
    "aws": {
        "title": "AWS Skill Builder",
        "url": "https://skillbuilder.aws/"
    },
    "azure": {
        "title": "Microsoft Learn Azure Training",
        "url": "https://learn.microsoft.com/en-us/training/azure/"
    },
    "gcp": {
        "title": "Google Cloud Training",
        "url": "https://cloud.google.com/learn/training"
    },
    "cloud computing": {
        "title": "Cloud Computing Fundamentals",
        "url": "https://www.coursera.org/learn/cloud-computing"
    },
    "docker": {
        "title": "Docker Getting Started",
        "url": "https://docs.docker.com/get-started/"
    },
    "kubernetes": {
        "title": "Kubernetes Tutorials",
        "url": "https://kubernetes.io/docs/tutorials/"
    },
    "linux": {
        "title": "Linux Command Line Learning",
        "url": "https://ubuntu.com/tutorials/command-line-for-beginners"
    },

    # GenAI
    "generative ai": {
        "title": "Generative AI Learning",
        "url": "https://www.deeplearning.ai/short-courses/"
    },
    "llm": {
        "title": "Hugging Face LLM Course",
        "url": "https://huggingface.co/learn/llm-course/"
    },
    "rag": {
        "title": "RAG Tutorials",
        "url": "https://huggingface.co/learn"
    },
    "prompt engineering": {
        "title": "Prompt Engineering Guide",
        "url": "https://www.promptingguide.ai/"
    },

    # Professional skills
    "communication": {
        "title": "Communication Skills Learning",
        "url": "https://www.coursera.org/browse/personal-development/communication"
    },
    "problem solving": {
        "title": "Problem Solving Courses",
        "url": "https://www.coursera.org/browse/personal-development"
    },
    "analytical thinking": {
        "title": "Critical Thinking Courses",
        "url": "https://www.coursera.org/browse/personal-development"
    },
    "leadership": {
        "title": "Leadership Courses",
        "url": "https://www.coursera.org/browse/business/leadership-and-management"
    },
    "sales": {
        "title": "HubSpot Inbound Sales",
        "url": "https://academy.hubspot.com/courses/inbound-sales"
    },
    "email marketing": {
        "title": "HubSpot Email Marketing",
        "url": "https://academy.hubspot.com/courses/email-marketing-certification-en"
    },
}


# ============================================================
# FALLBACK RESOURCE
# Uses a search for the actual missing skill, not a homepage
# ============================================================

def create_fallback(skill):
    query = quote_plus(f"{skill} official tutorial course")

    return {
        "skill": skill,
        "description": (
            f"Learn the fundamentals and practical applications "
            f"of {skill}."
        ),
        "resources": [
            {
                "title": f"Find a {skill} Course",
                "url": (
                    "https://www.google.com/search?q="
                    f"{query}"
                )
            }
        ]
    }


# ============================================================
# FIND RESOURCE
# ============================================================

def find_resource(skill):
    if not skill:
        return None

    skill_key = str(skill).strip().lower()
    skill_key = skill_key.replace("-", " ")
    skill_key = skill_key.replace("_", " ")
    skill_key = " ".join(skill_key.split())

    if skill_key in LEARNING_RESOURCES:
        return LEARNING_RESOURCES[skill_key]

    # Match common spelling variants
    aliases = {
        "react.js": "react",
        "reactjs": "react",
        "nodejs": "node.js",
        "node": "node.js",
        "express.js": "express",
        "powerbi": "power bi",
        "google cloud": "gcp",
        "google cloud platform": "gcp",
        "amazon web services": "aws",
        "microsoft azure": "azure",
        "sklearn": "scikit-learn",
        "ml": "machine learning",
        "genai": "generative ai",
        "gen ai": "generative ai",
        "eda": "exploratory data analysis",
        "postgres": "postgresql",
    }

    skill_key = aliases.get(skill_key, skill_key)

    if skill_key in LEARNING_RESOURCES:
        return LEARNING_RESOURCES[skill_key]

    # Match only a known alias that is a complete phrase.
    # Avoid broad substring matches such as "java" in "javascript".
    for key, resource in LEARNING_RESOURCES.items():
        if skill_key == key:
            return resource

    return None


# ============================================================
# GENERATE LEARNING RECOMMENDATIONS
# ============================================================

def generate_learning_recommendations(
    missing_skills,
    max_recommendations=10
):
    if not missing_skills:
        return []

    recommendations = []
    seen = set()

    for skill in missing_skills:
        if not skill:
            continue

        original_skill = str(skill).strip()
        normalized_skill = original_skill.lower()

        if normalized_skill in seen:
            continue

        seen.add(normalized_skill)

        resource = find_resource(original_skill)

        if resource:
            recommendation = {
                "skill": original_skill,
                "description": (
                    f"Learn and practise {original_skill}."
                ),
                "resources": [
                    {
                        "title": resource["title"],
                        "url": resource["url"]
                    }
                ]
            }
        else:
            recommendation = create_fallback(
                original_skill
            )

        recommendations.append(recommendation)

        if len(recommendations) >= max_recommendations:
            break

    return recommendations


# ============================================================
# PUBLIC FUNCTION USED BY jobs.py
# ============================================================

def get_learning_recommendations(
    missing_skills,
    max_recommendations=10
):
    return generate_learning_recommendations(
        missing_skills,
        max_recommendations
    )
