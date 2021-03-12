from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\USER\\VSworkspace\\CaseStudy\\Bank.sqlite3'
app.config['SECRET_KEY'] = 'your secret key'
# track_modifications = app.config['SQLALCHEMY_TRACK_MODIFICATIONS']

db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

from Loan import view
from Loan import model
from Loan import schema
from Loan import auth
from microservice import model