from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask import Flask

db:SQLAlchemy = SQLAlchemy()

def initDB(app: Flask):
    db.init_app(app)
    with app.app_context():
        db.create_all()

class Content(db.Model):
    id = Column(Integer, primary_key=True)
    detail = Column(String(64))
    def __init__(self, id, detail):
        self.id = id
        self.detail = detail
    
    def __repr__(self):
        return f'<Content {self.id}>'
    