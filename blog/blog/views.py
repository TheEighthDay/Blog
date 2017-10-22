#!/usr/bin/python
#coding=utf-8
import os
import Image
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import render_template, redirect, flash, url_for, request, abort
from werkzeug.utils import secure_filename
from blog import  db, app
from forms import LoginForm,AddBlogForm,ContactForm,AddDiaryForm
from models import Blog,Diary
from Email import send
from identifycode import gene_code

@app.route('/', methods=['GET'])
def index():
    """ index """
    diarys = Diary.query.filter_by(is_valid=True).all()
    blogs = Blog.query.filter_by(is_valid=True).all()
    return render_template('index.html',blogs=blogs,diarys=diarys)

@app.route('/blog/', methods=['GET'])
def blog():
    """ blog """
    blogs=Blog.query.filter_by(is_valid=True).all()
    return render_template('blog.html',blogs=blogs)

@app.route('/blogcontent/<int:pk>', methods=['GET'])
def blogcontent(pk):
    """ blogcontent """
    if (type(pk)!=int):
        return render_template('404.html')
    blog_obj=Blog.query.filter_by(id=pk).first()
    blogs=Blog.query.filter_by(is_valid=True).all()
    return render_template('blogcontent.html',blog_obj=blog_obj,blogs=blogs)



@app.route('/lifestyle/', methods=['GET'])
def lifestyle():
    """ lifestyle """
    diarys = Diary.query.filter_by(is_valid=True).all()
    return render_template('lifestyle.html',diarys=diarys)

@app.route('/lifestylecontent/<int:pk>', methods=['GET'])
def lifestylecontent(pk):
    """ blogcontent """
    if (type(pk)!=int):
        return render_template('404.html')
    diary_obj=Diary.query.filter_by(id=pk).first()
    diarys=Diary.query.filter_by(is_valid=True).all()
    return render_template('lifestylecontent.html',diarys=diarys,diary_obj=diary_obj)


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

text=''
i=0
@app.route('/admin',methods=['GET', 'POST'])
def admin():
    """ 后台增加 """
    global text
    global i
    pas=False
    add = AddBlogForm()
    add2 = AddDiaryForm()
    form=LoginForm()
    blogs = Blog.query.filter_by(is_valid=True).all()
    diarys = Diary.query.filter_by(is_valid = True).all()
    if (request.method != 'POST'):
         text,image = gene_code()
         i+=1
         image.save('blog/static/images/idencode'+str(i)+'.png')  # 保存验证码图片
         if(os.path.exists(os.path.dirname(__file__)+'/static/images/idencode'+str(i-1)+'.png')):
             print ('1')
             os.remove(os.path.dirname(__file__)+'/static/images/idencode'+str(i-1)+'.png')
         else:
             print('0');

    identify = request.form.get('identify', '')
    if form.validate_on_submit() and identify==text:
            pas = True
    if add.validate_on_submit():
        if(add2.picture.data):
            pas = True
            flash('Successful')
            f = add2.picture.data
            filename = secure_filename(f.filename)
            addr = 'blog/static/images/diary/' + filename
            f.save(addr)
            img = Image.open(addr)
            out = img.resize((800, 570), Image.ANTIALIAS)  # resize image with high-quality
            out.save(addr)
            diary = Diary(
                title=add2.data['title'],
                time=add2.data['time'],
                content=add2.data['content'],
                is_valid=True,
                picture=addr
            )
            db.session.add(diary)
            db.session.commit()

        else:
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



    return render_template('admin.html', form=form, pas=pas, add=add,blogs=blogs,i=str(i),add2=add2,diarys=diarys)




@app.route('/admin/blog/<int:pk>',methods=[ 'POST'])
def admin_blog_manage(pk):
    """ blog微博 """
    if(type(pk)!=int):
        return '404'
    blog = Blog.query.filter_by(id=pk, is_valid=1).first()
    if blog is None:
        return '404'
    blog.is_valid = 0
    db.session.add(blog)
    db.session.commit()
    return '201'
@app.route('/admin/diary/<int:pk>',methods=[ 'POST'])
def admin_diary_manage(pk):
    """ blog微博 """
    if(type(pk)!=int):
        return '404'
    diary = Diary.query.filter_by(id=pk, is_valid=1).first()
    if diary is None:
        return '404'
    diary.is_valid = 0
    db.session.add(diary)
    db.session.commit()
    return '201'
