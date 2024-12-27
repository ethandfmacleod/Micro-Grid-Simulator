import { useLocation, useParams } from 'react-router-dom';

export function useUrlParam(param: string) {
    const { [param]: value } = useParams();
    return value;
}

export const useCurrentObject = () => {
    const location = useLocation();
    const searchParams = new URLSearchParams(location.search);
    return searchParams.get("node");
};