import { FC } from 'react'
import { Link, Outlet, useLocation } from 'react-router-dom'
import { Home, TableView } from '@mui/icons-material'
import {
  Box,
  Drawer,
  List,
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Typography,
} from '@mui/material'

const drawerWidth = '250px'

export const Dashboard: FC = () => {
  const location = useLocation()
  const sidebar = [
    {
      path: 'models',
      text: 'Home',
      icon: <Home />,
    },
    {
      path: 'datasets',
      text: 'Datasets',
      icon: <TableView />,
    },
  ]

  return (
    <>
      <Drawer
        open
        sx={{
          width: drawerWidth,
          '& > .MuiDrawer-paper': {
            width: drawerWidth,
          },
        }}
        variant="persistent"
      >
        <Box
          sx={{
            textAlign: 'center',
            paddingTop: '2rem',
            paddingBottom: '1rem',
          }}
        >
          <Typography
            variant="h5"
            sx={{ letterSpacing: '0.2em', userSelect: 'none', width: '100%' }}
          >
            AutoML
          </Typography>
        </Box>
        <List sx={{ width: '100%' }}>
          {sidebar.map(it => (
            <ListItem key={it.text}>
              <ListItemButton
                to={it.path}
                component={Link}
                disableRipple
                selected={location.pathname.startsWith(`/app/${it.path}`)}
              >
                <ListItemIcon>{it.icon}</ListItemIcon>
                <ListItemText primary={it.text} />
              </ListItemButton>
            </ListItem>
          ))}
        </List>
      </Drawer>
      <Box component="main" sx={{ paddingLeft: drawerWidth }}>
        <Outlet />
      </Box>
    </>
  )
}
