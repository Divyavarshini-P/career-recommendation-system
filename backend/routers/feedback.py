from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class FeedbackRequest(BaseModel):
    resume_text: str


@router.post("/resume-feedback")
def resume_feedback(data: FeedbackRequest):

    text = data.resume_text.lower()

    suggestions = []

    # Resume length
    if len(text.split()) < 150:
        suggestions.append(
            "Add more content to your resume."
        )

    # Projects
    if "project" not in text:
        suggestions.append(
            "Include project details."
        )

    # Experience
    if "experience" not in text:
        suggestions.append(
            "Add work experience."
        )

    # Achievements
    if "achievement" not in text:
        suggestions.append(
            "Mention achievements."
        )

    # Skills
    if "skill" not in text:
        suggestions.append(
            "Add a dedicated skills section."
        )

    # Certifications
    if "certification" not in text:
        suggestions.append(
            "Include relevant certifications."
        )

    # Education
    if "education" not in text:
        suggestions.append(
            "Mention your educational background."
        )

    # Contact
    if "@" not in text:
        suggestions.append(
            "Add your email address."
        )

    if len(suggestions) == 0:
        suggestions.append(
            "Excellent resume! No major improvements required."
        )

    return {
        "suggestions": suggestions
    }