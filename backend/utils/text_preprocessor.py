import json
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SYNONYM_FILE = os.path.join(BASE_DIR, "data", "synonyms.json")

with open(SYNONYM_FILE, "r", encoding="utf-8") as file:
    SYNONYMS = json.load(file)


def normalize_text(text: str) -> str:
    """
    Replace abbreviations with full skill names.
    Example:
    ML -> Machine Learning
    JS -> JavaScript
    AI -> Artificial Intelligence
    """

    text = text.lower()

    for short, full in SYNONYMS.items():
        pattern = r"\b" + re.escape(short.lower()) + r"\b"
        text = re.sub(pattern, full.lower(), text)

    return text