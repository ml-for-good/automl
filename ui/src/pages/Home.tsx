import { useState } from 'react'
import { Button } from '@mui/material'

export const Home = () => {
  const [count, setCount] = useState(0)

  return (
    <Button
      color="primary"
      variant="contained"
      onClick={() => setCount((count) => count + 1)}
      sx={{ margin: '20px' }}
    >
      count is: {count}
    </Button>
  )
}
