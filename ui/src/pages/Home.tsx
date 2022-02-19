import { useState, ChangeEvent } from 'react'
import PropTypes from 'prop-types'
import {
  Radio,
  RadioGroup,
  FormControlLabel,
  FormControl,
  FormLabel,
  Container,
  Box,
  Paper,
  Card,
  CardContent,
  Typography,
  Button,
  CardActions,
  Grid,
} from '@mui/material'

import AddIcon from '@mui/icons-material/Add'

interface IProject {
  id: number
  performance: string
  dataset: string
  target: string
}

interface IProjectCardInfoProps {
  label: string
  value: string | number
}

const ProjectCardInfo = ({ label, value }: IProjectCardInfoProps) => (
  <Grid
    container
    spacing={2}
    alignItems="center"
    justifyContent="space-between"
  >
    <Grid item>
      <Typography sx={{ fontSize: 14 }} color="text.secondary">
        {label}
      </Typography>
    </Grid>
    <Grid item>
      <Typography variant="h6">{value}</Typography>
    </Grid>
  </Grid>
)

ProjectCardInfo.propTypes = {
  label: PropTypes.string.isRequired,
  value: PropTypes.string.isRequired,
}

interface IProjectCardProps {
  project: IProject
}

const ProjectCard = ({ project }: IProjectCardProps) => {
  interface ICardContent {
    label: string
    key: keyof IProject
  }
  return (
    <Card sx={{ minWidth: 375 }}>
      <CardContent>
        {(
          [
            { label: 'Performance', key: 'performance' },
            { label: 'DataSet', key: 'dataset' },
            { label: 'Target', key: 'target' },
          ] as ICardContent[]
        ).map(item => (
          <ProjectCardInfo
            key={item.key}
            label={item.label}
            value={project[item.key]}
          />
        ))}
      </CardContent>
      <CardActions>
        <Button size="large">View</Button>
      </CardActions>
    </Card>
  )
}

ProjectCard.propTypes = {
  project: PropTypes.shape({
    id: PropTypes.number.isRequired,
    performance: PropTypes.string.isRequired,
    dataset: PropTypes.string.isRequired,
    target: PropTypes.string.isRequired,
  }).isRequired,
}

export const Home = () => {
  const [statusValue, setStatusValue] = useState('')

  const handleStatusChange = (event: ChangeEvent<HTMLInputElement>) => {
    setStatusValue((event.target as HTMLInputElement).value)
  }

  return (
    <Container maxWidth="xl">
      <Box sx={{ pt: 3, pb: 3 }}>
        <Grid container spacing={20} alignItems="center">
          <Grid item>
            <FormControl>
              <FormLabel id="filtered-radio-buttons-group-label">
                Filtered by
              </FormLabel>
              <RadioGroup
                row
                aria-labelledby="filtered-radio-buttons-group-label"
                name="row-radio-buttons-group"
                value={statusValue}
                onChange={handleStatusChange}
              >
                <FormControlLabel
                  value="in_draft"
                  control={<Radio />}
                  label="In Draft"
                />
                <FormControlLabel
                  value="in_training"
                  control={<Radio />}
                  label="In Training"
                />
                <FormControlLabel
                  value="ready"
                  control={<Radio />}
                  label="Ready"
                />
                <FormControlLabel
                  value="in_review"
                  control={<Radio />}
                  label="In Review"
                />
                <FormControlLabel
                  value="error"
                  control={<Radio />}
                  label="Error"
                />
                <FormControlLabel
                  value="warning"
                  control={<Radio />}
                  label="Warning"
                />
              </RadioGroup>
            </FormControl>
          </Grid>

          <Grid item>
            <Button size="large" variant="contained" startIcon={<AddIcon />}>
              Create New Model
            </Button>
          </Grid>
        </Grid>
      </Box>
      <Box
        sx={{
          display: 'flex',
          flexWrap: 'wrap',
          ml: -1,
          '& > :not(style)': {
            m: 1,
          },
        }}
      >
        {(
          [
            { id: 1, performance: 'Great', dataset: 'a.csv', target: 'Price' },
            { id: 2, performance: 'Bad', dataset: 'b.csv', target: 'Distance' },
            { id: 3, performance: 'Great', dataset: 'c.csv', target: 'Price' },
            { id: 4, performance: 'Great', dataset: 'd.csv', target: 'Price' },
            { id: 5, performance: 'Great', dataset: 'a.csv', target: 'Price' },
            { id: 6, performance: 'Great', dataset: 'a.csv', target: 'Price' },
            { id: 7, performance: 'Great', dataset: 'a.csv', target: 'Price' },
          ] as IProject[]
        ).map(project => (
          <Paper key={project.id}>
            <ProjectCard project={project} />
          </Paper>
        ))}
      </Box>
    </Container>
  )
}
