import os
import pandas as pd


# =========================================================
# Export Resume Analysis for Power BI
# =========================================================

def export_analysis(
    match_score,
    matched_skills,
    missing_skills,
    careers,
    feedback
):

    # -----------------------------------------------------
    # Create exports folder
    # -----------------------------------------------------

    export_folder = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "exports"
    )

    os.makedirs(
        export_folder,
        exist_ok=True
    )


    # -----------------------------------------------------
    # CSV file path
    # -----------------------------------------------------

    csv_path = os.path.join(
        export_folder,
        "analysis_results.csv"
    )


    # -----------------------------------------------------
    # Prepare career names
    # -----------------------------------------------------

    career_names = []

    for career in careers:

        if isinstance(career, dict):

            career_names.append(
                career.get(
                    "career",
                    ""
                )
            )

        else:

            career_names.append(
                str(career)
            )


    # -----------------------------------------------------
    # Prepare data
    # -----------------------------------------------------

    data = {

        "match_score": [
            match_score
        ],

        "matched_skills": [
            ", ".join(
                map(
                    str,
                    matched_skills
                )
            )
        ],

        "missing_skills": [
            ", ".join(
                map(
                    str,
                    missing_skills
                )
            )
        ],

        "recommended_careers": [
            ", ".join(
                career_names
            )
        ],

        "feedback": [
            " | ".join(
                map(
                    str,
                    feedback
                )
            )
        ]
    }


    # -----------------------------------------------------
    # Convert to DataFrame
    # -----------------------------------------------------

    df = pd.DataFrame(
        data
    )


    # -----------------------------------------------------
    # Export CSV
    # -----------------------------------------------------

    df.to_csv(
        csv_path,
        index=False
    )


    print(
        f"Analysis exported successfully: {csv_path}"
    )


    return {
        "success": True,
        "file": csv_path
    }