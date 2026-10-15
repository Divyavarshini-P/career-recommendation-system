import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
  CategoryScale,
  LinearScale,
  BarElement,
} from "chart.js";

import { Doughnut, Bar } from "react-chartjs-2";

import "../styles/ResultCard.css";


// =====================================================
// Register Chart.js Components
// =====================================================

ChartJS.register(
  ArcElement,
  Tooltip,
  Legend,
  CategoryScale,
  LinearScale,
  BarElement
);


// =====================================================
// Analysis Chart
// =====================================================

function AnalysisChart({ result }) {

  if (!result) {
    return null;
  }


  // ===================================================
  // Skills Data
  // ===================================================

  const matchedSkills =
    result.matched_skills || [];

  const missingSkills =
    result.missing_skills || [];


  // ===================================================
  // Career Data
  // ===================================================

  const careers =
    result.recommended_roles || [];


  // ===================================================
  // Doughnut Chart
  // ===================================================

  const skillsData = {

    labels: [
      "Matched Skills",
      "Missing Skills"
    ],

    datasets: [

      {
        data: [
          matchedSkills.length,
          missingSkills.length
        ],

        backgroundColor: [
          "#10B981",
          "#EF4444"
        ],

        borderColor: [
          "#059669",
          "#DC2626"
        ],

        borderWidth: 2,

        hoverOffset: 12
      }

    ]

  };


  // ===================================================
  // Career Names
  // ===================================================

  const careerNames =
    careers.map(
      (career) =>
        career.career
    );


  // ===================================================
  // Career Scores
  // ===================================================

  const careerScores =
    careers.map(
      (career) =>
        career.match_score || 0
    );


  // ===================================================
  // Career Chart
  // ===================================================

  const careerData = {

    labels: careerNames,

    datasets: [

      {
        label: "Career Match",

        data: careerScores,

        backgroundColor: [
          "#2563EB",
          "#7C3AED",
          "#F59E0B",
          "#EC4899",
          "#06B6D4",
          "#10B981"
        ],

        borderColor: [
          "#1D4ED8",
          "#6D28D9",
          "#D97706",
          "#DB2777",
          "#0891B2",
          "#059669"
        ],

        borderWidth: 2,

        borderRadius: 8,

        barThickness: 55
      }

    ]

  };


  // ===================================================
  // Doughnut Options
  // ===================================================

  const doughnutOptions = {

    responsive: true,

    maintainAspectRatio: false,

    plugins: {

      legend: {

        position: "top",

        labels: {

          padding: 20,

          usePointStyle: true,

          font: {
            size: 14
          }

        }

      },

      tooltip: {

        callbacks: {

          label: function (context) {

            const label =
              context.label || "";

            const value =
              context.raw || 0;

            return ` ${label}: ${value}`;

          }

        }

      }

    },

    cutout: "60%"

  };


  // ===================================================
  // Career Bar Options
  // ===================================================

  const barOptions = {

    responsive: true,

    maintainAspectRatio: false,

    plugins: {

      legend: {

        position: "top",

        labels: {

          usePointStyle: true,

          padding: 20,

          font: {
            size: 14
          }

        }

      },

      tooltip: {

        callbacks: {

          label: function (context) {

            return ` Match Score: ${context.raw}`;

          }

        }

      }

    },

    scales: {

      y: {

        beginAtZero: true,

        ticks: {

          stepSize: 1

        },

        title: {

          display: true,

          text: "Match Score"

        }

      },

      x: {

        ticks: {

          maxRotation: 30,

          minRotation: 0

        }

      }

    }

  };


  // ===================================================
  // UI
  // ===================================================

  return (

    <div className="analysis-charts">


      {/* =================================================
          Skills Analysis
      ================================================= */}

      <div className="chart-card">

        <h2>
          🧠 Skills Analysis
        </h2>

        <div className="chart-container">

          <Doughnut
            data={skillsData}
            options={doughnutOptions}
          />

        </div>

      </div>


      {/* =================================================
          Career Recommendation
      ================================================= */}

      <div className="chart-card">

        <h2>
          💼 Career Recommendation Score
        </h2>

        <div className="chart-container">

          {careers.length > 0 ? (

            <Bar
              data={careerData}
              options={barOptions}
            />

          ) : (

            <p className="no-chart-data">
              No career recommendations available.
            </p>

          )}

        </div>

      </div>


    </div>

  );

}


export default AnalysisChart;