# ============================================================
# COURSE RECOMMENDER
# ============================================================

def recommend_courses(missing_skills):
    """
    Recommend learning resources based on missing skills.
    """

    course_database = {

        "python": {
            "course": "Python for Data Analysis",
            "platform": "Coursera",
            "level": "Beginner"
        },

        "sql": {
            "course": "SQL for Data Analysis",
            "platform": "Coursera",
            "level": "Beginner"
        },

        "excel": {
            "course": "Excel Skills for Data Analytics",
            "platform": "Coursera",
            "level": "Beginner"
        },

        "power bi": {
            "course": "Microsoft Power BI Data Analyst",
            "platform": "Microsoft Learn",
            "level": "Intermediate"
        },

        "statistics": {
            "course": "Statistics for Data Science",
            "platform": "Coursera",
            "level": "Beginner"
        },

        "machine learning": {
            "course": "Machine Learning Fundamentals",
            "platform": "Coursera",
            "level": "Intermediate"
        },

        "nlp": {
            "course": "Natural Language Processing",
            "platform": "Coursera",
            "level": "Intermediate"
        },

        "java": {
            "course": "Java Programming",
            "platform": "Oracle",
            "level": "Beginner"
        },

        "javascript": {
            "course": "JavaScript Fundamentals",
            "platform": "freeCodeCamp",
            "level": "Beginner"
        },

        "react": {
            "course": "React Fundamentals",
            "platform": "freeCodeCamp",
            "level": "Intermediate"
        },

        "react.js": {
            "course": "React Fundamentals",
            "platform": "freeCodeCamp",
            "level": "Intermediate"
        },

        "html": {
            "course": "HTML and Web Development",
            "platform": "freeCodeCamp",
            "level": "Beginner"
        },

        "css": {
            "course": "CSS Fundamentals",
            "platform": "freeCodeCamp",
            "level": "Beginner"
        },

        "git": {
            "course": "Git and GitHub Fundamentals",
            "platform": "GitHub",
            "level": "Beginner"
        },

        "github": {
            "course": "Git and GitHub Fundamentals",
            "platform": "GitHub",
            "level": "Beginner"
        },

        "docker": {
            "course": "Docker Fundamentals",
            "platform": "Docker",
            "level": "Intermediate"
        },

        "aws": {
            "course": "AWS Cloud Fundamentals",
            "platform": "AWS",
            "level": "Beginner"
        },

        "mongodb": {
            "course": "MongoDB Basics",
            "platform": "MongoDB University",
            "level": "Beginner"
        },

        "rest api": {
            "course": "REST API Development",
            "platform": "freeCodeCamp",
            "level": "Intermediate"
        },

        "data structures": {
            "course": "Data Structures and Algorithms",
            "platform": "GeeksforGeeks",
            "level": "Intermediate"
        },

        "algorithms": {
            "course": "Algorithms and Problem Solving",
            "platform": "GeeksforGeeks",
            "level": "Intermediate"
        }
    }

    recommendations = []

    for skill in missing_skills:

        skill_name = str(skill).lower().strip()

        if skill_name in course_database:

            course = course_database[skill_name]

            recommendations.append({
                "skill": skill,
                "course": course["course"],
                "platform": course["platform"],
                "level": course["level"]
            })

    return recommendations