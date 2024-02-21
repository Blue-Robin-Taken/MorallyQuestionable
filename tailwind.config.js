/** @type {import('tailwindcss').Config} */
const colors = require('tailwindcss/colors')
module.exports = {
  content: './templates/*.html',
  theme: {
    extend: {
    fontFamily:{
        'kode':['Kode Mono']
    }
    },
  },
  plugins: [],
}