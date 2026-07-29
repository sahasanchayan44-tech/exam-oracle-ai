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
        border: "#222E28",
        input: "#222E28",
        ring: "#10B981",
        background: "#0C0F0E",
        foreground: "#F3F4F6",
        primary: {
          DEFAULT: "#10B981", // Mint Emerald
          foreground: "#FFFFFF",
        },
        accent: {
          DEFAULT: "#F59E0B", // Warm Gold
          foreground: "#000000",
        },
        onyx: {
          bg: "#0C0F0E",
          card: "#141A17",
          border: "#222E28",
          emerald: "#10B981",
          gold: "#F59E0B"
        }
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
}
