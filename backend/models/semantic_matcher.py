from sentence_transformers import SentenceTransformer, util

# Load the Sentence Transformer model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_similarity(resume_text: str, job_description: str) -> float:
    """
    Calculate semantic similarity between a resume and a job description.
    Returns a score between 0 and 100.
    """

    resume_embedding = model.encode(
        resume_text,
        convert_to_tensor=True
    )

    job_embedding = model.encode(
        job_description,
        convert_to_tensor=True
    )

    similarity = util.cos_sim(
        resume_embedding,
        job_embedding
    )

    score = float(similarity[0][0]) * 100

    # Keep score within valid range
    score = max(0, min(score, 100))

    return round(score, 2)
