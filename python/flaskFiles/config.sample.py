#!/usr/bin/env python
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cig-Dashboard'
    #...
    MYSQL_DATABASE_USER = 'database_username'
    MYSQL_DATABASE_PASSWORD = 'user_password'
    MYSQL_DATABASE_DB = 'use_this_database'
    MYSQL_DATABASE_HOST='databasehost.com'
    MYSQL_DATABASE_PORT=3306
    SQLALCHEMY_DATABASE_URI = f"mysql://{MYSQL_DATABASE_USER}:{MYSQL_DATABASE_PASSWORD}@{MYSQL_DATABASE_HOST}/{MYSQL_DATABASE_DB}?charset=utf8&use_unicode=0"
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
