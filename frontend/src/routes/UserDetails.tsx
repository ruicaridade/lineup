import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import User from "../models/User";

interface Props {
  user?: User;
}

const UserDetails = (props: Props) => {
  const { id } = useParams<{ id: string }>();
  const [user, setUser] = useState<User | undefined>(props.user);

  // Here we're re-fetching the user, but we could as easily pass in a pre-fetched user from the table via
  // react-router's history.push().
  useEffect(() => {
    if (!user) {
      fetch(`${process.env.REACT_APP_API_URL!}/users/${id}`)
        .then((res) => res.json())
        .then((data) => {
          setUser(data as User); // Dangerous.
        });
    }
  }, [user, id]);

  return (
    <div className="flex justify-center mt-32">
      {user ? (
        <div className="flex flex-col justify-center items-center">
          <img
            alt="Avatar"
            src={user?.avatarUrl}
            className="w-40 h-40 rounded-full"
          />
          <h2 className="text-center mt-2 text-xl font-semibold text-gray-700">
            {user?.firstName} {user?.lastName}
          </h2>
          <p>
            ✉️{" "}
            <a href={`mailto:${user?.email}`} className="text-blue-500">
              {user?.email}
            </a>
          </p>
        </div>
      ) : (
        <h1 className="text-xl text-gray-700">Loading...</h1>
      )}
    </div>
  );
};

export default UserDetails;
