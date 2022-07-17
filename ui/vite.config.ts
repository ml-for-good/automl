/* eslint-disable import/no-default-export */
/* eslint-disable import/no-extraneous-dependencies */
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import viteEslint from 'vite-plugin-eslint'
import viteSvgr from 'vite-plugin-svgr'
import autoprefixer from 'autoprefixer'
import cssnano from 'cssnano'
import * as path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  resolve: {
    alias: {
      '@': path.join(__dirname, './src'),
    },
  },
  css: {
    postcss: {
      plugins: [
        autoprefixer({
          overrideBrowserslist: ['chrome > 50', 'ff > 30', 'ie 11'],
        }),
        cssnano(),
      ],
    },
  },
  plugins: [
    react({
      babel: {
        plugins: ['babel-plugin-styled-components', '@emotion/babel-plugin'],
      },
      jsxImportSource: '@emotion/react',
    }),
    viteEslint(),
    viteSvgr(),
  ],
  assetsInclude: ['.png', '.svg'],
})
