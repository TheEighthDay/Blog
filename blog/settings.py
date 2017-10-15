#!/usr/bin/python
#coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class Config:
    HOST = 'localhost'
    PORT = 5000
    SECRET_KEY='gaibaj<>adabva46a76?>][5aaaAAFa5vd'
    #SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    #FLASK_MAIL_SENDER='Flask Admin 邮箱'
    #FLASK_ADMIN = 'Flask Admin'

    @staticmethod
    def init_app(app):
        pass
class DevelopmentConfig(Config):
    DEBUG=True
    MAIL_USERNAME='1985861426@qq.com'
    MAIL_SERVER='smtp.qq.com'
    MAIL_PASSWARD='WEI131494250'
    MAIL_PORT='465'
    #MAIL_USE_TLS =True
    SQLALCHEMY_DATABASE_URI='mysql://root:123456@127.0.0.1/flask_blog'
    SQLALCHEMY_TRACK_MODIFICATIONS=True

class TestingConfig(Config):  #继承DevelopmentConfig也行
    TESTING =True
    #SQLALCHEMY_DATABASE_URI='test用的数据库'
    #SQLALCHEMY_TRACK_MODIFICATIONS=True

config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'default':DevelopmentConfig
}
