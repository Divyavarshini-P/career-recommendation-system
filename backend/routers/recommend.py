from fastapi import APIRouter
from pydantic import BaseModel

from utils.skill_extractor import extract_skills
from models.career_recommender import recommend_careers

router = APIRouter()


class RecommendRequest(BaseModel):
    resume_text: str


@router.post("/recommend-career")
def recommend_career(data: RecommendRequest):

    # Extract skills from resume
    skills = extract_skills(data.resume_text)

    # Get AI-based career recommendations
    careers = recommend_careers(skills)

    return {
        "skills": skills,
        "recommended_roles": careers
    }