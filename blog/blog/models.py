#!/usr/bin/python
#coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')
#sys.path.append("/home/tkb/tiankaibin/blog")

from blog import db
from flask import render_template, redirect, flash, url_for, request


class Blog(db.Model):
    """blog"""
    __tablename__='blog'
    id =  db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80),  nullable=True)
    time = db.Column(db.String(80),  nullable=True)
    content = db.Column(db.Text,  nullable=True)
    is_valid = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return '<Blog %r>' % self.title

class Diary(db.Model):
    """diary"""
    __tablename__='diary'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=True)
    time = db.Column(db.String(80), nullable=True)
    content = db.Column(db.Text, nullable=True)
    picture = db.Column(db.String(80), nullable=True)
    is_valid = db.Column(db.Boolean, default=True)


    def __repr__(self):
        return '<Diary %r>' % self.title