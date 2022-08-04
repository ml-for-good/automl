import { format } from 'date-fns'

export const datetimeFormat = (datetime: string | number | Date) => {
  const t =
    typeof datetime === 'string' || typeof datetime === 'number'
      ? new Date(datetime)
      : datetime
  return format(t, 'yyyy/MM/dd HH:mm:ss')
}
