import sqlalchemy as db
import os
from connector import *

connecttodatabase()

metadata_obj = sqlalchemy.MetaData()

users = db.Table(
    'users',
    metadata_obj,
    db.Column('UserID', db.Integer, primary_key=True, unique=True, autoincrement=True),
    db.Column('Name', db.String(255)),
    db.Column('GitHubUsername', db.String(255)),
    db.Column('Job', db.String(255), nullable=False)
)

Login = db.Table(
    db.Column('UserID', db.Integer, primary_key=True, unique=True, autoincrement=True),
    db.Column('Username', db.String(255), nullable=False),
    db.Column('Password', db.String(16), nullable=False)
)

Section = db.Table(
    db.Column('SectionID', db.Integer, primary_key=True, unique=True, autoincrement=True),
    db.Column('RepoURL', db.String(255))
)

UserSection = db.Table(
    db.Column('SectionID', db.Integer, nullable=False),
    db.Column('UserID', db.Integer, nullable=False)
)