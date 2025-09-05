import React from "react";

export default function Alerts({ story }) {
  return (
    <div className="p-3 bg-gray-100 rounded-xl shadow">
      <h2 className="font-bold">AI Report</h2>
      <p>{story || "Upload an image to get started."}</p>
    </div>
  );
}
