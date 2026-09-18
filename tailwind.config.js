/* Tokens do Design System "Cyberpunk Glass & Neon Lime" (ver design.md).
   O CSS final é compilado para assets/css/tailwind.css com `npm run build:css`
   (o GitHub Action .github/workflows/build-css.yml faz isso sozinho a cada push). */
module.exports = {
  content: ['./index.html', './pt/*.html', './en/*.html', './assets/js/*.js'],
  theme: {
    extend: {
      colors: {
        ink: '#050505',
        surface: '#111111',
        lime: '#CCFF00',
        brand: { DEFAULT: '#B7E500', hover: '#B3E600' }
      },
      fontFamily: {
        montserrat: ['Montserrat', 'sans-serif'],
        jakarta: ['"Plus Jakarta Sans"', 'sans-serif']
      },
      keyframes: {
        fadeIn: {
          from: { opacity: '0', transform: 'translateY(10px)' },
          to: { opacity: '1', transform: 'none' }
        },
        'gate-shake': {
          '10%, 90%': { transform: 'translateX(-1px)' },
          '20%, 80%': { transform: 'translateX(2px)' },
          '30%, 50%, 70%': { transform: 'translateX(-4px)' },
          '40%, 60%': { transform: 'translateX(4px)' }
        }
      },
      animation: {
        fadeIn: 'fadeIn 0.8s ease-out both'
      }
    }
  },
  plugins: []
};
