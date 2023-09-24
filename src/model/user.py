from src.db import db
from src.model.base_model import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    email = db.Column(db.String(120), nullable=True)
    first_name = db.Column(db.String(120), nullable=True)
    last_name = db.Column(db.String(120), nullable=True)
    avatar = db.Column(db.String(120), nullable=True)

    def __init__(self, email, first_name, last_name, avatar, id=None):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.avatar = avatar
        if id is not None:
            self.id = id

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "avatar": self.avatar,
        }
