/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: ["class"],
  content: [
    './src/pages/**/*.{ts,tsx}',
    './src/components/**/*.{ts,tsx}',
    './src/app/**/*.{ts,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: {
          DEFAULT: "#4F46E5", // Indigo-600
          foreground: "#FFFFFF",
        },
        secondary: {
          DEFAULT: "#0EA5E9", // Sky-500
          foreground: "#FFFFFF",
        },
        oracle: {
          dark: "#0B0F19",
          card: "#111827",
          border: "#1F2937",
          accent: "#6366F1",
          gold: "#F59E0B"
        }
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
}
