#!/usr/bin/env python
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from flaskext.mysql import MySQL

app = Flask(__name__)
#@app.route('/')
app.config.from_object(Config)

#setup database
db = SQLAlchemy(app)

#engine = db.create_engine(f'mysql://{Config.MYSQL_DATABASE_USER}:{Config.MYSQL_DATABASE_PASSWORD}@{Config.MYSQL_DATABASE_HOST}:{Config.MYSQL_DATABASE_PORT}/{Config.MYSQL_DATABASE_DB}?charset=utf8&use_unicode=0', pool_recycle=3600)
#connection = engine.connect()

migrate = Migrate(app, db)

from app import routes, models

db.create_all()
db.session.commit()
