"use client";

import { useEffect, useState } from "react";

export default function Home() {
  const [status, setStatus] = useState("Checking...");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/")
      .then((res) => res.json())
      .then((data) => {
        setStatus(data.status);
      })
      .catch(() => {
        setStatus("Backend Offline");
      });
  }, []);

  return (
    <main className="min-h-screen bg-gray-950 text-white flex flex-col items-center justify-center">
      <h1 className="text-5xl font-bold mb-6">
        🎬 AI Video Generator
      </h1>

      <p className="text-xl text-gray-300 mb-6">
        Professional AI Video Creation Platform
      </p>

      <div className="mb-8">
        <span className="text-lg">
          Backend Status: <strong>{status}</strong>
        </span>
      </div>

      <div className="grid grid-cols-2 gap-4">
        <button className="bg-blue-600 px-6 py-3 rounded-lg hover:bg-blue-700">
          💬 AI Chat
        </button>

        <button className="bg-purple-600 px-6 py-3 rounded-lg hover:bg-purple-700">
          ✍️ Script Writer
        </button>

        <button className="bg-green-600 px-6 py-3 rounded-lg hover:bg-green-700">
          🖼️ Image Generator
        </button>

        <button className="bg-red-600 px-6 py-3 rounded-lg hover:bg-red-700">
          🎥 Text to Video
        </button>
      </div>
    </main>
  );
}