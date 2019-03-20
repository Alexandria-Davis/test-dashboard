from datetime import datetime
from app import db

class TestInfo(db.Model):
    suiteName = db.Column(db.String(64), primary_key=True)
    testCase = db.Column(db.String(64), index=True, unique=False)
    testRunName = db.Column(db.Integer, index=True, unique=False)
    totalTests = db.Column(db.Integer, index=True, unique=False)
    numErrors = db.Column(db.Integer, index=True, unique=False)
    failedTest = db.Column(db.Integer, index=True, unique=False)
    numSkipped = db.Column(db.Integer, index=True, unique=False)
    totalDuration = db.Column(db.DateTime, index=True, unique=False)
    error = db.Column(db.Boolean, index=True, unique=False)
    fail = db.Column(db.Boolean, index=True, unique=False)
    skipped = db.Column(db.Boolean, index=True, unique=False)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<TestInfo {}>'.format(self.username)
