import { useParams } from 'react-router-dom';

export function useUrlParam(param: string) {
    const { [param]: value } = useParams();
    return value;
}