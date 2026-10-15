import { useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Results from "./pages/Results.jsx";
import Navbar from "./components/Navbar";

import Home from "./pages/Home";
import Analyze from "./pages/Analyze";
import About from "./pages/About";

import "./App.css";

function App() {

  const [analysisResult, setAnalysisResult] = useState(null);

  return (
    <BrowserRouter>

      <Navbar />

      <Routes>

        {/* Home */}
        <Route
          path="/"
          element={<Home />}
        />

        {/* Analyze */}
        <Route
          path="/analyze"
          element={
            <Analyze
              setAnalysisResult={setAnalysisResult}
            />
          }
        />

        {/* Results */}
        <Route
          path="/results"
          element={
            <Results
              result={analysisResult}
            />
          }
        />

        {/* About */}
        <Route
          path="/about"
          element={<About />}
        />

      </Routes>

    </BrowserRouter>
  );
}

export default App;