#!/usr/bin/python
#coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')


from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileRequired,FileAllowed
from wtforms import StringField, PasswordField, SubmitField, TextAreaField,FileField
from wtforms.validators import DataRequired, ValidationError
from md5salt import create_md5
from blog import app

class LoginForm(FlaskForm):
    """ 登录表单 """
    password = PasswordField(label='password', validators=[DataRequired("Please input password")],
        description="Please input password",
        render_kw={"required": "required", "class": "form-control"})
    submit = SubmitField('Submit', render_kw={
            'class': 'btn btn-info'
        })

    def validate_password(self, field):
         password = field.data
         if (str(create_md5(password,app.config['SECRET_KEY']))!='2c3982347e888ac1ba188e11be21b082'):
             raise ValidationError("123456")
         return password

class AddBlogForm(FlaskForm):
    """增加blog表单"""
    title = StringField(label="Title", validators=[DataRequired("Please input title")],
                        render_kw={"required": 'required', "placeholder": "Please input title","class": 'form-control'})
    time = StringField(label="Time", validators=[DataRequired("Please input time")],
                render_kw={"required": 'required', "placeholder": "Please input time","class": 'form-control'})

    content = TextAreaField(label='blog', validators=[DataRequired('Please input blog')],
                            description="Please input blog",
                            render_kw={"required": "required", "class": "form-control","cols":'60',"rows":'10'})
    submit = SubmitField('Submit', render_kw={
        'class': 'btn btn-info',"placeholder": "Submit"},)

class AddDiaryForm(FlaskForm):
    """增加blog表单"""
    title = StringField(label="Title", validators=[DataRequired("Please input title")],
                        render_kw={"required": 'required', "placeholder": "Please input title","class": 'form-control'})
    time = StringField(label="Time", validators=[DataRequired("Please input time")],
                render_kw={"required": 'required', "placeholder": "Please input time","class": 'form-control'})

    content = TextAreaField(label='blog', validators=[DataRequired('Please input blog')],
                            description="Please input blog",
                            render_kw={"required": "required", "class": "form-control","cols":'60',"rows":'10'})
    picture = FileField(label="Picture", validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Submit', render_kw={
        'class': 'btn btn-info',"placeholder": "Submit"},)


class ContactForm(FlaskForm):
    """联系email表单"""
    email = StringField(label="Your Email", validators=[DataRequired()],
                        render_kw={"required": 'required',"class": 'form-control'})
    phone = StringField(label="Your QQ", validators=[DataRequired()],
                        render_kw={"required": 'required',"class": 'form-control'})
    message = TextAreaField(label='Message', validators=[DataRequired()],
                            render_kw={"required": "required","class": 'form-control',"cols":'30',"rows":'10'})
    submit = SubmitField('Send Massage', render_kw={
        'class': 'btn btn-primary',"placeholder": "Send Massage"},)
