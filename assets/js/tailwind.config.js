/* Tokens do Design System "Cyberpunk Glass & Neon Lime" (ver design.md).
   Carregado logo após o Tailwind Play CDN, antes de qualquer markup. */
tailwind.config = {
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
        morph: {
          '0%, 100%': { borderRadius: '30% 70% 70% 30% / 30% 30% 70% 70%' },
          '25%': { borderRadius: '58% 42% 75% 25% / 76% 46% 54% 24%' },
          '50%': { borderRadius: '50% 50% 33% 67% / 55% 27% 73% 45%' },
          '75%': { borderRadius: '33% 67% 58% 42% / 63% 68% 32% 37%' }
        },
        'gate-shake': {
          '10%, 90%': { transform: 'translateX(-1px)' },
          '20%, 80%': { transform: 'translateX(2px)' },
          '30%, 50%, 70%': { transform: 'translateX(-4px)' },
          '40%, 60%': { transform: 'translateX(4px)' }
        }
      },
      animation: {
        fadeIn: 'fadeIn 0.8s ease-out both',
        morph: 'morph 8s ease-in-out infinite',
        'morph-reverse': 'morph 8s ease-in-out infinite reverse'
      }
    }
  }
};
