#from flask_mongoengine import MongoEngine
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)
#db = MongoEngine()
#db.init_app(app)
'''
import os
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://thhnotdmgcunwz:415d6dc5b0c3955c85c96ce04d2393b1257f77b0dd1277c8646ebc5466b9523e@ec2-3-230-61-252.compute-1.amazonaws.com:5432/da47drr0meiv51'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY = SECRET_KEY'] = os.urandom(16).hex()
app.config['JWT_TOKEN_LOCATION'] = ['headers', 'query_string', 'cookies']
app.config['JWT_COOKIE_SECURE'] = False
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
app.config['TRACK_USAGE_COOKIE'] = False
'''
