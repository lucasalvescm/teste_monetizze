from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
db = SQLAlchemy(app)

# from loteria_app.loteria.views import loteria

# app.register_blueprint(loteria)

db.create_all()

from loteria_app.loteria import views
