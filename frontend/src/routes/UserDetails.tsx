import { useParams } from "react-router-dom";

interface Params {
  id: string;
}

const UserDetails = () => {
  const { id } = useParams<Params>();
  return <h1>User: {id}</h1>;
};

export default UserDetails;
