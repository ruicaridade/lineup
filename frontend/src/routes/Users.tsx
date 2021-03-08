import React, { useEffect, useState } from "react";
import { useHistory } from "react-router-dom";
import User from "../models/User";

interface ParentProps {
  children: React.ReactNode;
}

// We could extract these atomic components as their own "Table" component for more re-usability.
const TableHeader = (props: ParentProps) => {
  return <th className="py-4 px-3">{props.children}</th>;
};

const TableColumn = (props: ParentProps) => {
  return <td className="py-4 px-3">{props.children}</td>;
};

const Users = () => {
  const history = useHistory();
  const [users, setUsers] = useState<User[]>([]);

  useEffect(() => {
    fetch(`${process.env.REACT_APP_API_URL!}/users`)
      .then((res) => res.json())
      .then((data) => {
        setUsers(data.items.map((item: object) => item as User)); // Dangerous.
      });
  }, []);

  return (
    <div className="flex justify-center">
      <table className="w-full mt-32 shadow-lg">
        <thead className="bg-gray-300">
          <tr className="text-left">
            <TableHeader>Name</TableHeader>
            <TableHeader>E-mail</TableHeader>
          </tr>
        </thead>
        <tbody className="bg-gray-100">
          {users.map((user, i) => {
            return (
              <tr
                className={`cursor-pointer ${i % 2 === 0 ? "bg-gray-200" : ""}`}
                onClick={() => history.push(`/users/${user.id}`)}
                key={i}
              >
                <TableColumn>
                  <div className="flex items-center">
                    <img
                      alt="Avatar"
                      src={user.avatarUrl}
                      className="object-cover w-12 h-12 rounded-full mr-3"
                    />
                    <span>
                      {user.firstName} {user.lastName}
                    </span>
                  </div>
                </TableColumn>
                <TableColumn>{user.email}</TableColumn>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
};

export default Users;
