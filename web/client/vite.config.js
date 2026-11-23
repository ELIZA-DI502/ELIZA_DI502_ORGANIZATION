import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// In development (npm run dev), the page runs on Vite and /api goes to the web backend on port 3000.
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: { "/api": "http://localhost:3000" },
    fs: { allow: ["..", "../../../config"] },   // config/personal-data.json is shared with the RAG service (D3)
  },
});
