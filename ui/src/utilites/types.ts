export interface PaginationQuery {
  limit?: number
  offset?: number
}

export interface PaginationResponseBody<T> extends Required<PaginationQuery> {
  total: number
  payload: T[]
}
