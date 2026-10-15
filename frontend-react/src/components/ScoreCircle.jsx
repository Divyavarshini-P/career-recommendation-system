import { CircularProgressbar, buildStyles } from "react-circular-progressbar";
import "react-circular-progressbar/dist/styles.css";

function ScoreCircle({ score }) {
  return (
    <div
      style={{
        width: "180px",
        height: "180px",
        margin: "20px auto",
      }}
    >
      <CircularProgressbar
        value={score}
        text={`${score.toFixed(1)}%`}
        styles={buildStyles({
          textColor: "#1d3557",
          pathColor: "#2563eb",
          trailColor: "#e5e7eb",
          textSize: "14px",
        })}
      />
    </div>
  );
}

export default ScoreCircle;