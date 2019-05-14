#!/usr/bin/env python
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cig-Dashboard'
    #...
    MYSQL_DATABASE_USER = 'sgroot'
    MYSQL_DATABASE_PASSWORD = 'sC1I%5Ea75rpe9SzqZ'
    MYSQL_DATABASE_DB = 'test-dashboard'
    MYSQL_DATABASE_HOST='SG-TestDash-550-master.servers.mongodirector.com'
    MYSQL_DATABASE_PORT=3306
    SQLALCHEMY_DATABASE_URI = f"mysql://{MYSQL_DATABASE_USER}:{MYSQL_DATABASE_PASSWORD}@{MYSQL_DATABASE_HOST}/{MYSQL_DATABASE_DB}?charset=utf8&use_unicode=0"
    SQLALCHEMY_POOL_RECYCLE = 300
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
