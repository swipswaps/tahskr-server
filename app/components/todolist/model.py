from datetime import datetime

from components.base.model import Base
from db import db


class ToDoList(db.Model, Base):
    __tablename__ = "ToDoList"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("User.id"), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    created = db.Column(db.DateTime, nullable=False)

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

        self.created = datetime.utcnow()

        db.session.add(self)
        db.session.commit()
