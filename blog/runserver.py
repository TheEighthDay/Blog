#!/usr/bin/python
#coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from blog import app

if __name__ == '__main__':
    app.run()