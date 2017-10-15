#!/usr/bin/python
#coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import render_template, redirect, flash, url_for, request, abort
from werkzeug.utils import secure_filename
from blog import  db, app
from forms import LoginForm,AddBlogForm,ContactForm
from models import Blog
from Email import send

@app.route('/', methods=['GET'])
def index():
    """ index """
    return render_template('index.html')

@app.route('/blog/', methods=['GET'])
def blog():
    """ blog """
    return render_template('blog.html')

@app.route('/blogcontent/', methods=['GET'])
def blogcontent():
    """ blogcontent """
    return render_template('blogcontent.html')

@app.route('/lifestyle/', methods=['GET'])
def lifestyle():
    """ lifestyle """
    return render_template('lifestyle.html')


@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    """ contact """
    form=ContactForm()
    if form.validate_on_submit():
        words=('email'+':'+form.data['email']+'\n'+'phone'+':'+form.data['phone']+'\n'+form.data['message'])
        if (send(words)):
            flash('I will send e-mail to you')
        else:
            flash('Failed to send')

    return render_template('contact.html',form=form)

@app.route('/admin/add',methods=['GET', 'POST'])
def admin_add():
    """ 后台增加 """
    pas=False
    add = AddBlogForm()
    form=LoginForm()
    if form.validate_on_submit():
        pas=True
    if add.validate_on_submit():
        pas=True
        blog = Blog(
            title = add.data['title'],
            time = add.data['time'],
            content =add.data['content'],
            is_valid = True
        )
        db.session.add(blog)
        db.session.commit()
        flash('Successful')


    return render_template('admin_add.html', form=form, pas=pas, add=add)

@app.route('/admin/delete',methods=['GET', 'POST'])
def admin_delete():
    """后台删除"""
    pas = False
    form = LoginForm()
    blogs = Blog.query.filter_by(is_valid=True).all()
    if form.validate_on_submit():
        pas = True

    return render_template('admin_delete.html', form=form, pas=pas,blogs=blogs)


@app.route('/admin/blog/<int:pk>',methods=[ 'POST'])
def admin_blog_manage(pk):
    """ blog微博 """
    blog = Blog.query.filter_by(id=pk, is_valid=1).first()
    if blog is None:
        return '404'
    blog.is_valid = 0
    db.session.add(blog)
    db.session.commit()
    return '201'
