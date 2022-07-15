import { FC } from 'react'
import { Outlet } from 'react-router-dom'
import { AppBar, Box, Toolbar, Typography } from '@mui/material'
import { DashboardDrawer, DrawerHeader } from './drawer'
import { DashboardMenu } from './menu'

export const Dashboard: FC = () => (
  <Box sx={{ display: 'flex' }}>
    <AppBar position="fixed" sx={{ zIndex: theme => theme.zIndex.drawer + 1 }}>
      <Toolbar variant="dense">
        <Typography variant="h6" noWrap component="div">
          AutoML
        </Typography>
      </Toolbar>
    </AppBar>
    <DashboardDrawer open variant="permanent">
      <DrawerHeader />
      <DashboardMenu />
    </DashboardDrawer>
    <Box component="main" pt={6}>
      <Outlet />
    </Box>
  </Box>
)
