from datetime import datetime

import pytz

from src.db import db

timezone = pytz.timezone("Asia/Jakarta")


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now(tz=timezone))
    updated_at = db.Column(
        db.DateTime,
        default=datetime.now(tz=timezone),
        onupdate=datetime.now(tz=timezone),
    )
    deleted_at = db.Column(db.DateTime, nullable=True)

    def soft_delete(self):
        if self.deleted_at is not None:
            return
        self.deleted_at = datetime.now(tz=timezone)

    def undelete(self):
        self.deleted_at = None
        self.updated_at = datetime.now(tz=timezone)

    def hard_delete(self):
        db.session.delete(self)
