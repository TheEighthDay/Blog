#!/usr/bin/python
#coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')
#sys.path.append("/home/tkb/tiankaibin/blog")

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from settings import config

app = Flask(__name__)
app.config.from_object(config['default'])
db = SQLAlchemy(app)


from blog import views, models

