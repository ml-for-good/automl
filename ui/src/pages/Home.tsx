import { useState, useEffect } from 'react'
import { Button } from '@mui/material'
import httpRequest from '../utils/http'

export const Home = () => {
  const [count, setCount] = useState(0)

  useEffect(() => {
    httpRequest({
      method: 'get',
      url: '/demo',
      params: {
        count,
      }
    }).then(data => {
      console.log(data)
    }).catch(err => {
      console.log(err)
    })
  }, [])

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
