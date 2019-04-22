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


migrate = Migrate(app, db)

from app import routes, models

db.create_all()
db.session.commit()
