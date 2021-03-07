"""
Normally I'd start new projects with a structure similar to Django: with the ORM model as the center piece.

However, using an external API poses and interesting challenge: we can no longer assume our data is always tied to
a database. We could just simply ignore it and use the model classes anyways, but that wouldn't be as fun :)

Instead, I've opted to experiment a bit with the repository pattern which is admittedly fairly common in other
languages, but not so common in Python-land. Seems like a decent way to abstract the data layer from our domain, at
least on paper.

This strips our models off of ORM-related attributes and turns them into simple Python objects which means we can no
longer benefit from spawning a query builder directly in our model class. Luckily SQLAlchemy has our back, and provides
way to map existing tables to Python objects via "imperative mappings", as demonstrated in the docs:

https://docs.sqlalchemy.org/en/14/orm/mapping_styles.html#imperative-a-k-a-classical-mappings

I know this is a bit of a tangent, but thought I'd leave this here as I found it farly interesting.
"""
from typing import List, Tuple

import requests

from lineup import settings
from lineup.auth.models import User
from lineup.core.exceptions import NotFoundError
from lineup.core.utilities import import_class


class UserRepository:
    def all(self, limit: int, page: int) -> Tuple[List[User], int, int]:
        raise NotImplementedError()

    def find_by_id(self, instance_id: int) -> User:
        raise NotImplementedError()


# --- Examples

# noinspection PyAbstractClass
class UserSpoofModelRepository(UserRepository):
    pass


# noinspection PyAbstractClass
class UserSqlAlchemyRepository(UserRepository):
    pass

# ---


class UserApiRepository(UserRepository):
    """
    Example implementation of a Repository for the `User` model.

    Uses https://reqres.in/api/users as the data source.

    I'm deliberately not handling API errors, other than 404s, to keep this simple.
    """

    def all(self, limit: int = 6, page: int = 0) -> Tuple[List[User], int, int]:
        """
        Retrieves a paginated list of `User` instances, sorted by id.

        Args:
            limit: Maximum number of instances per page. Must be a number higher than 0.
            page: The number of the page to fetch.

        Raises:
            HTTPStatusError: The API responded with an error.

        Returns:
            A tuple consisting of the list of users, the total count and the current page number.
        """
        res = requests.get(
            url='https://reqres.in/api/users',
            params={
                'page': page,
                'per_page': limit
            }
        )

        # if not res.ok:
        #     > Who needs error handling, anyways? :)
        res.raise_for_status()

        resources = res.json()

        users = []
        for node in resources['data']:
            users.append(
                User(
                    id=node['id'],
                    email=node['email'],
                    first_name=node['first_name'],
                    last_name=node['last_name'],
                    avatar_url=node['avatar'],
                )
            )

        return users, resources['total'], resources['page']

    def find_by_id(self, instance_id: int) -> User:
        """
        Retrieves an `User` instance by id.

        Raises:
            NotFoundError: `User` with matching id not found.
            HTTPStatusError: The API responded with an error.

        Returns:
            An `User` instance with a matching id.
        """
        res = requests.get(
            url=f'https://reqres.in/api/users/{instance_id}'
        )

        if not res.ok:
            if res.status_code == requests.codes.NOT_FOUND:
                raise NotFoundError()  # Gets caught by our handler and automatically returns a proper 404 response.
            else:
                res.raise_for_status()

        resources = res.json()

        user = User(
            id=resources['data']['id'],
            email=resources['data']['email'],
            first_name=resources['data']['first_name'],
            last_name=resources['data']['last_name'],
            avatar_url=resources['data']['avatar']
        )

        return user


try:
    Repository = import_class(settings.REPOSITORIES.get('users'))
except ImportError:
    Repository = UserApiRepository  # Fallback
