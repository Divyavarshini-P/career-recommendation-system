import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

CAREER_FILE = os.path.join(
    BASE_DIR,
    "data",
    "careers.json"
)

with open(CAREER_FILE, "r", encoding="utf-8") as f:
    CAREERS = json.load(f)


def recommend_careers(user_skills):
    """
    Recommend top careers based on extracted skills.
    """

    recommendations = []

    user_skills = set(skill.lower() for skill in user_skills)

    for career, details in CAREERS.items():

        required = set(
            skill.lower()
            for skill in details["required_skills"]
        )

        preferred = set(
            skill.lower()
            for skill in details["preferred_skills"]
        )

        matched_required = len(
            user_skills & required
        )

        matched_preferred = len(
            user_skills & preferred
        )

        score = (
            matched_required * 2
            +
            matched_preferred
        )

        if score > 0:

            recommendations.append({

                "career": career,

                "category": details["category"],

                "description": details["description"],

                "match_score": score

            })

    recommendations.sort(
        key=lambda x: x["match_score"],
        reverse=True
    )

    return recommendations[:5]