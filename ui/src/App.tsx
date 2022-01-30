import { Link, Route, Routes, useLocation } from 'react-router-dom'
import { Box, CssBaseline, Drawer, List, ListItem, ListItemButton, ListItemIcon, ListItemText, ThemeProvider, Typography } from '@mui/material'
import {
  HomeOutlined as HomeIcon,
  TableViewOutlined as TableViewIcon,
} from '@mui/icons-material'
import { theme } from './theme'
import { Home } from './pages/Home'
import { Datasets } from './pages/Datasets'

const drawerWidth = '250px'

export const App = () => {
  const location = useLocation()
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Drawer
        open
        sx={{
          width: drawerWidth,
          '& > .MuiDrawer-paper': {
            width: drawerWidth
          }
        }}
        variant="persistent"
      >
        <Box sx={{ textAlign: 'center', paddingTop: '2rem', paddingBottom: '1rem' }}>
          <Typography variant="h5" sx={{ letterSpacing: '0.3em', userSelect: 'none', width: '100%' }}>
            AutoML
          </Typography>
        </Box>
        <List sx={{ width: '100%' }}>
          <ListItem>
            <ListItemButton
              to="/"
              component={Link}
              disableRipple
              selected={location.pathname === '/'}
            >
              <ListItemIcon>
                <HomeIcon />
              </ListItemIcon>
              <ListItemText primary="Home" />
            </ListItemButton>
          </ListItem>
          <ListItem>
            <ListItemButton
              to="/datasets"
              component={Link}
              disableRipple
              selected={location.pathname === '/datasets'}
            >
              <ListItemIcon>
                <TableViewIcon />
              </ListItemIcon>
              <ListItemText primary="Datasets" />
            </ListItemButton>
          </ListItem>
        </List>
      </Drawer>
      <Box component="main" sx={{ paddingLeft: drawerWidth }}>
        <Routes>
          <Route index element={<Home />} />
          <Route path="/datasets" element={<Datasets />} />
        </Routes>
      </Box>
    </ThemeProvider>
  )
}
