/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {},
  },
  fontSize: {
    'responsive': 'clamp(1.2rem, 4vw + 1rem, 6rem)',
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: [
      {
        mytheme: {
          "primary": "#21284E",
          "secondary": "#8BC8FF",
          "accent": "#5367FE",
          "neutral": "#121318",
          "base-100": "#F0F0F0",
        },
      },
      "dark",
      "light",
    ],
  },
}

