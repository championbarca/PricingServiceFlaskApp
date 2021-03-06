import uuid
from dataclasses import dataclass, field
from typing import Dict
from models.model import Model
import models.user.errors as UserErrors
from common.utils import Utils

@dataclass
class User(Model):
    collection:str = field(init=False, default="users")
    email:str
    password:str = field(repr=False)
    _id:str = field(default_factory=lambda: uuid.uuid4().hex)
    
    @classmethod
    def find_by_email(cls, email:str) -> "User":
        try:
            return cls.find_one_by('email', email)
        except TypeError:
            raise UserErrors.UserNotFoundError("A user with e-mail was not found")
        
    @classmethod
    def register_user(cls, email:str, password:str) -> "User":
        if not Utils.email_is_valid(email):
            raise UserErrors.InvalidEmailError("The e-mail does not have the right format.")
        
        try:
            user = cls.find_by_email(email)
            raise UserErrors.UserAlreadyRegisteredError("The e-mail you used to register already exists.")
        except UserErrors.UserNotFoundError:
            User(email, Utils.hash_password(password)).save_to_mongo()

        return True

    @classmethod
    def is_valid_login(cls, email:str, password:str) -> bool:
        user = cls.find_by_email(email)
        if not Utils.check_hashed_password(password, user.password):
            raise UserErrors.IncorrectPasswordError("Your password is incorrect.")
        
        return True

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "email": self.email,
            "password": self.password
        }