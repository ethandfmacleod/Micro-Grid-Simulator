import { useDispatch, useSelector } from 'react-redux'
import type { RootState, AppDispatch } from './store'

// See also: https://redux-toolkit.js.org/tutorials/typescript#define-typed-hooks

// Use throughout your app instead of plain `useDispatch` and `useSelector`
export const useAppDispatch = useDispatch.withTypes<AppDispatch>()
export const useAppSelector = useSelector.withTypes<RootState>()