import React, { useState } from "react";
import MapView from "./components/MapView";
import Alerts from "./components/Alerts";
// import Chart from "./components/Chart"; // Keep commented until implemented

export default function App() {
  const [detections, setDetections] = useState([]);
  const [story, setStory] = useState("");

  // Optional: file upload handler (can enable later)
  /*
  const handleUpload = async (e) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch("http://localhost:8000/detect/", {
        method: "POST",
        body: formData,
      });
      const data = await res.json();
      setDetections(data.detections);
      setStory(data.story);
    } catch (err) {
      console.error("Upload failed", err);
    }
  };
  */

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-4">WildEye AI Dashboard</h1>

      {/* Optional file upload */}
      {/* <input type="file" onChange={handleUpload} className="my-2" /> */}

      {/* Alerts component */}
      <Alerts story={story} />

      {/* Map component */}
      <MapView detections={detections} />

      {/* Optional chart component */}
      {/* <Chart /> */}
    </div>
  );
}
