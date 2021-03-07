from dataclasses import dataclass

from lineup.core.utilities import Serializable


@dataclass
class User(Serializable):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar_url: str
