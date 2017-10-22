#coding:utf-8
import Image  
import os
addr='/home/tkb/tiankaibin/Blog/blog/blog/static/images/me.jpg'
img = Image.open(addr)
out = img.resize((800, 570), Image.ANTIALIAS)  
out.save(addr)
