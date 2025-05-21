import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
    server: {
      host: '0.0.0.0',
      proxy: {
        '/api': {
          target: 'http://backend:5000',
          changeOrigin: true,
          rewrite: path => path
        }
      },
      allowedHosts: [
        'silaeder.codingprojects.ru',
        '.silaeder.codingprojects.ru' // Включает поддомены
      ]
  }
})
