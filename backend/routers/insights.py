from fastapi import APIRouter
from pydantic import BaseModel

from utils.skill_extractor import extract_skills

router = APIRouter()


class InsightRequest(BaseModel):
    resume_text: str
    job_description: str


@router.post("/skill-gap")
def skill_gap(data: InsightRequest):

    resume_skills = set(
        extract_skills(data.resume_text)
    )

    job_skills = set(
        extract_skills(data.job_description)
    )

    matched_skills = sorted(
        list(
            resume_skills & job_skills
        )
    )

    missing_skills = sorted(
        list(
            job_skills - resume_skills
        )
    )

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }