import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
    plugins: [react(), tailwindcss()],

    // server: {
    //     host: "192.168.1.33",
    //     port: 1000,
    // },
});
