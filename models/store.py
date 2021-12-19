from typing import Dict
import uuid
from models.model import Model


class Store(Model):
    collection = "stores"

    def __init__(self, name:str, url_prefix:str, tag_name:str, query: Dict, _id:str = None):
        super().__init__()
        self.name = name
        self.url_prefix = url_prefix
        self.tag_name = tag_name
        self.query = query
        self._id = _id or uuid.uuid4().hex
