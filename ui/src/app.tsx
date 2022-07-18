import { CssBaseline, ThemeProvider } from '@mui/material'
import { HashRouter, Navigate, Route, Routes } from 'react-router-dom'
import { Dashboard } from './layouts/dashboard'
import { Datasets } from './pages/app/datasets'
import { Models } from './pages/app/models'
import { Login } from './pages/login'
import { Register } from './pages/register'
import { theme } from './theme'

export const App = () => (
  <ThemeProvider theme={theme}>
    <CssBaseline />
    <HashRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route index element={<Navigate to="/app/models" />} />
        <Route path="/app" element={<Dashboard />}>
          <Route path="models" element={<Models />} />
          <Route path="datasets" element={<Datasets />} />
        </Route>
      </Routes>
    </HashRouter>
  </ThemeProvider>
)
