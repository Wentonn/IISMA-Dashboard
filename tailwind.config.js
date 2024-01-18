/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./board/templates/**/*.html",
    "./board/static/src/**/*.js",
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}