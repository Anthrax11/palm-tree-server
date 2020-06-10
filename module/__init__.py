from flask import Flask


"""Configuration parameters"""
app = Flask(__name__)
app.config['SECRET_KEY'] = '123'

from module import routes