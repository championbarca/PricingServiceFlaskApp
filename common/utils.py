import re
from passlib.hash import pbkdf2_sha512

class Utils:
    @staticmethod
    def email_is_valid(email:str) -> bool:
        email_address_pattern = re.compile(r'^[\w-]+@([\w-]+\.)+[\w]+$')
        return True if email_address_pattern.match(email) else False

    @staticmethod
    def hash_password(passowrd: str) ->str:
        return pbkdf2_sha512.encrypt(passowrd)
    
    @staticmethod
    def check_hashed_password(password:str, hashed_password:str) -> bool:
        return pbkdf2_sha512.verify(password, hashed_password)
    
    