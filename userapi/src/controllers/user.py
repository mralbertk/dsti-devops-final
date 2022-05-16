import base64
import hashlib


class User:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __repr__(self):
        return f"User: {self.last_name}, {self.first_name} - {self.email}"

    @property
    def hash_id(self):
        user_hash = f"{self.first_name}{self.last_name}{self.email}"
        user_hash = hashlib.md5(user_hash.encode('ascii')).digest()
        user_hash = base64.b64encode(user_hash)
        return user_hash

    @property
    def details(self):
        user_details = {"first_name": self.first_name,
                        "last_name": self.last_name,
                        "email": self.email}
        return user_details

