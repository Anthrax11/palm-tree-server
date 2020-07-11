from flask import Flask
from flask_sqlalchemy import SQLAlchemy


"""Configuration parameters"""
app = Flask(__name__)
app.config['SECRET_KEY'] = '123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

from module import routes