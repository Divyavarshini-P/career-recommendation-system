import json
import os

import spacy
from spacy.matcher import PhraseMatcher

from utils.text_preprocessor import normalize_text

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SKILLS_FILE = os.path.join(
    BASE_DIR,
    "data",
    "skills.json"
)

with open(SKILLS_FILE, "r", encoding="utf-8") as file:
    skills_data = json.load(file)

# Collect all skills
ALL_SKILLS = []

for category in skills_data.values():
    ALL_SKILLS.extend(category)

# Remove duplicates
ALL_SKILLS = sorted(list(set(ALL_SKILLS)))

# Create Phrase Matcher
matcher = PhraseMatcher(
    nlp.vocab,
    attr="LOWER"
)

patterns = [
    nlp.make_doc(skill)
    for skill in ALL_SKILLS
]

matcher.add(
    "SKILLS",
    patterns
)


def extract_skills(text: str):
    """
    Extract technical skills from resume/job description.
    """

    text = normalize_text(text)

    doc = nlp(text)

    matches = matcher(doc)

    found = set()

    for _, start, end in matches:

        found.add(
            doc[start:end].text.title()
        )

    return sorted(list(found))