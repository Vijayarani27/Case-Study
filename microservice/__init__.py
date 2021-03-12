from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\USER\\VSworkspace\\CaseStudy\\Bank.sqlite3'
app.config['SECRET_KEY'] = 'your secret key'
# track_modifications = app.config['SQLALCHEMY_TRACK_MODIFICATIONS']

db = SQLAlchemy(app)
ma = Marshmallow(app)

from microservice import view
from microservice import model
from microservice import schema
from microservice import auth
from Loan import model



