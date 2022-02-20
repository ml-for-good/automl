import { HashRouter, Navigate, Route, Routes } from 'react-router-dom'
import { CssBaseline, ThemeProvider } from '@mui/material'
import { theme } from './theme'
import { Models } from './pages/models'
import { Datasets } from './pages/datasets'
import { Dashboard } from './layouts/dashboard'

export const App = () => (
  <HashRouter>
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Routes>
        <Route index element={<Navigate to="/app/models" />} />
        <Route path="/app" element={<Dashboard />}>
          <Route path="models" element={<Models />} />
          <Route path="datasets" element={<Datasets />} />
        </Route>
      </Routes>
    </ThemeProvider>
  </HashRouter>
)
