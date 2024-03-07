import os

from flask import Flask, render_template
from models import db, Flat


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://postgres:{os.environ['POSTGRES_PASSWORD']}@postgres_database:5432/postgres"
db.init_app(app)

@app.route("/")
def index():
    flats = Flat.query.all()
    return render_template("index.html", flats=flats)
