import { Link, useLocation } from 'react-router-dom'
import { AutoAwesomeMosaic, Home, TableView } from '@mui/icons-material'
import {
  List,
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
} from '@mui/material'

const sidebarItems = [
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
  {
    path: 'namespaces',
    text: 'Namespaces',
    icon: <AutoAwesomeMosaic />,
  },
]

export const DashboardMenu = () => {
  const location = useLocation()
  return (
    <List sx={{ width: '100%' }} dense>
      {sidebarItems.map(it => (
        <ListItem dense key={it.text}>
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
  )
}
