from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Flat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
