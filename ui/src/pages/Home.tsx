import { useState, useEffect } from 'react'
import { Button } from '@mui/material'
import { axiosInstance } from '../utils/http'

export const Home = () => {
  const [count, setCount] = useState(0)

  useEffect(() => {
    axiosInstance({
      method: 'get',
      url: '/demo',
      params: {
        count,
      }
    }).then(data => {
      // eslint-disable-next-line no-console
      console.log(data)
    }).catch(err => {
      // eslint-disable-next-line no-console
      console.log(err)
    })
  }, [])

  return (
    <Button
      color="primary"
      variant="contained"
      onClick={() => setCount(v => v + 1)}
      sx={{ margin: '20px' }}
    >
      count is:
      {count}
    </Button>
  )
}
