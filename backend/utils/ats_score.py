import re


# ============================================================
# ATS RESUME SCORE
# ============================================================

def calculate_ats_score(
    resume_text,
    matched_skills,
    missing_skills
):
    """
    Calculate ATS Resume Score from 0-100.

    Score Breakdown:
        Contact Information : 25
        Resume Structure    : 40
        Resume Length       : 10
        Skill Match         : 25

    Total                  : 100
    """

    # ========================================================
    # NORMALIZE RESUME TEXT
    # ========================================================

    text = resume_text.lower()

    # Replace multiple spaces/newlines with one space
    text = re.sub(
        r'\s+',
        ' ',
        text
    ).strip()


    # ========================================================
    # INITIAL VALUES
    # ========================================================

    contact_score = 0
    structure_score = 0
    length_score = 0
    skill_score = 0

    feedback = []


    # ========================================================
    # 1. CONTACT INFORMATION - 25 MARKS
    # ========================================================

    # --------------------------------------------------------
    # Email - 10 Marks
    # --------------------------------------------------------

    email_pattern = (
        r'[\w\.-]+@[\w\.-]+\.\w+'
    )

    if re.search(
        email_pattern,
        text
    ):

        contact_score += 10

    else:

        feedback.append(
            "Add a professional email address."
        )


    # --------------------------------------------------------
    # Phone Number - 5 Marks
    # --------------------------------------------------------

    phone_patterns = [

        r'\b[6-9]\d{9}\b',

        r'\+91[\s-]?[6-9]\d{9}',

        r'\+91[\s-]?\d{10}'

    ]

    phone_found = any(
        re.search(
            pattern,
            text
        )
        for pattern in phone_patterns
    )

    if phone_found:

        contact_score += 5

    else:

        feedback.append(
            "Add a valid phone number."
        )


    # --------------------------------------------------------
    # LinkedIn - 5 Marks
    # --------------------------------------------------------

    linkedin_keywords = [

        "linkedin.com",

        "linkedin",

        "linked in"

    ]

    linkedin_found = any(
        keyword in text
        for keyword in linkedin_keywords
    )

    if linkedin_found:

        contact_score += 5

    else:

        feedback.append(
            "Include your LinkedIn profile."
        )


    # --------------------------------------------------------
    # GitHub - 5 Marks
    # --------------------------------------------------------

    github_keywords = [

        "github.com",

        "github",

        "git hub"

    ]

    github_found = any(
        keyword in text
        for keyword in github_keywords
    )

    if github_found:

        contact_score += 5

    else:

        feedback.append(
            "Include your GitHub profile."
        )


    # ========================================================
    # 2. RESUME STRUCTURE - 40 MARKS
    # ========================================================

    # Multiple keywords are used because different resumes
    # use different section names.
    #
    # Example:
    # "Projects" -> Projects
    # "Academic Projects" -> Projects
    # "Internship" -> Experience
    # "Work Experience" -> Experience

    section_patterns = {

        "Education": [

            "education",

            "academic background",

            "academic qualification",

            "qualification",

            "qualifications",

            "b.tech",

            "b.e.",

            "b.e ",

            "bachelor",

            "degree",

            "university",

            "college",

            "school"

        ],


        "Skills": [

            "skills",

            "technical skills",

            "technical expertise",

            "technical knowledge",

            "technologies",

            "programming languages",

            "core skills"

        ],


        "Projects": [

            "project",

            "projects",

            "academic project",

            "academic projects",

            "personal project",

            "personal projects",

            "mini project",

            "mini projects",

            "major project",

            "major projects"

        ],


        "Experience": [

            "experience",

            "work experience",

            "professional experience",

            "internship",

            "internships",

            "intern",

            "data analyst intern",

            "work history",

            "employment"

        ],


        "Certifications": [

            "certification",

            "certifications",

            "certificate",

            "certificates",

            "courses",

            "training",

            "professional certification"

        ],


        "Achievements": [

            "achievement",

            "achievements",

            "award",

            "awards",

            "hackathon",

            "hackathons",

            "accomplishment",

            "accomplishments",

            "honors",

            "honour"

        ]

    }


    # Marks for each section

    section_marks = {

        "Education": 7,

        "Skills": 7,

        "Projects": 7,

        "Experience": 7,

        "Certifications": 6,

        "Achievements": 6

    }


    # Check every section

    for section, keywords in section_patterns.items():

        section_found = any(

            keyword in text

            for keyword in keywords

        )

        if section_found:

            structure_score += section_marks[section]

        else:

            # Only give feedback if the section is actually missing
            feedback.append(
                f"Add a {section} section."
            )


    # ========================================================
    # 3. RESUME LENGTH - 10 MARKS
    # ========================================================

    words = len(
        text.split()
    )


    if words >= 300:

        length_score = 10

    elif words >= 200:

        length_score = 8

    elif words >= 150:

        length_score = 5

    else:

        length_score = 2

        feedback.append(
            "Resume is too short. "
            "Add more relevant details."
        )


    # ========================================================
    # 4. SKILL MATCH - 25 MARKS
    # ========================================================

    # Make sure these are lists
    matched_skills = (
        matched_skills
        if matched_skills
        else []
    )

    missing_skills = (
        missing_skills
        if missing_skills
        else []
    )


    total_skills = (

        len(matched_skills)

        +

        len(missing_skills)

    )


    if total_skills > 0:

        skill_percentage = (

            len(matched_skills)

            /

            total_skills

        )

        skill_score = round(

            skill_percentage * 25

        )

    else:

        skill_score = 0


    # Give feedback only when skills are actually missing

    if missing_skills:

        feedback.append(
            "Improve your missing technical skills."
        )


    # ========================================================
    # 5. FINAL SCORE
    # ========================================================

    score = (

        contact_score

        +

        structure_score

        +

        length_score

        +

        skill_score

    )


    # Never allow score above 100

    score = min(

        round(score),

        100

    )


    # ========================================================
    # 6. ATS RATING
    # ========================================================

    if score >= 90:

        rating = "Excellent"

    elif score >= 75:

        rating = "Very Good"

    elif score >= 60:

        rating = "Good"

    elif score >= 40:

        rating = "Average"

    else:

        rating = "Needs Improvement"


    # ========================================================
    # 7. RETURN RESULT
    # ========================================================

    return {

        "score": score,

        "rating": rating,

        "feedback": feedback,

        "breakdown": {

            "contact_information":
                contact_score,

            "resume_structure":
                structure_score,

            "resume_length":
                length_score,

            "skill_match":
                skill_score

        }

    }