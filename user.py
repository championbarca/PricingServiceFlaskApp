from typing import Dict
import uuid
from dataclasses import dataclass, field

@dataclass
class User:
    username:str
    password:str = field(compare=False, repr=False)
    _id:str = field(default_factory=lambda: uuid.uuid4().hex)

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "username": self.username
        }