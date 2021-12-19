from typing import Dict
import re
import requests
import uuid
from dataclasses import dataclass, field
from bs4 import BeautifulSoup
from models.model import Model

@dataclass(eq=False)
class Item(Model):
    collection:str = field(init=False, default="items")
    url:str
    tag_name:str
    query:str
    _id:str = field(default_factory=lambda: uuid.uuid4().hex)
    
    def __post_init__(self):
        self.price = None
        
    def load_price(self) -> None:
        response = requests.get(self.url, headers={'User-Agent': 'Mozilla/5.0'}, verify=True, timeout=10)
        content = response.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find(self.tag_name, self.query)
        string_price = element.text.strip()
        pattern = re.compile(r"(\d+,?\d*\.\d\d)")
        match = pattern.search(string_price)
        found_price = match.group(1)
        found_price = found_price.replace(",", "")
        self.price = float(found_price)
        return self.price
    
    def json(self) -> Dict:
        return {
            "_id" : self._id,
            "url" : self.url,
            "tag_name" : self.tag_name,
            "query" : self.query
        }