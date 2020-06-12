"""
The flask application package.
"""
import logging
from flask.logging import create_logger
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
from logging.handlers import RotatingFileHandler
import os
import sys
from .ascii_header import header
from logging.config import dictConfig

app = Flask(__name__)
app.config.from_object(Config)

# Add any logging levels and handlers with app.logger
handler = logging.StreamHandler(stream=sys.stdout) #'ext://sys.stdout')
handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s"))
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)
app.logger.info('Microblog startup') 

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views

