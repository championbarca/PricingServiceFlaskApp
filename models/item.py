from typing import Dict
import re
from typing import Dict
import requests
from bs4 import BeautifulSoup

class Item:
    def __init__(self, url:str, tag_name:str, query:Dict) -> None:
        self.url = url
        self.tag_name = tag_name
        self.query = query
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