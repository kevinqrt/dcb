import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  darkMode: 'class',
  theme: {
     extend: {colors: {
      '0': '#292E33',
      '1': '#191919', '2': '#FAF9F6', '3': '#3383FF', '4': '#e8e8e8', '5': '#E2DFD2',
      '1-dark': '#3D454C', '2-dark': '#2D8DE6', '3-dark': '#4D6780', '4-dark': '#191919'
    }
    ,
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'gradient-conic':
          'conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))',
      },
    },
  },
  plugins: [require("daisyui")],
}
export default config
