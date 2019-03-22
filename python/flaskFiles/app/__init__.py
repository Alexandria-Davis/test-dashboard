from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from flaskext.mysql import MySQL

app = Flask(__name__)
app.config.from_object(Config)

#setup database
db = SQLAlchemy(app)

engine = db.create_engine('mysql://test-user:test-password@localhost/test-dashboard?charset=utf8&use_unicode=0', pool_recycle=3600)
connection = engine.connect()

migrate = Migrate(app, db)

from app import routes, models

db.create_all()
db.session.commit()
