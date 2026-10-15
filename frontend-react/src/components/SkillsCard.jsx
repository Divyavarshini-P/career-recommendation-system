import "../styles/SkillsCard.css";

function SkillsCard({ title, skills, color }) {
  return (
    <div className="skills-card">

      <h3>{title}</h3>

      <div className="skills-container">

        {skills.length > 0 ? (

          skills.map((skill, index) => (

            <span
              key={index}
              className={`skill-chip ${color}`}
            >
              {skill}
            </span>

          ))

        ) : (

          <p>No Skills</p>

        )}

      </div>

    </div>
  );
}

export default SkillsCard;