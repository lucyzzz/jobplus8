# -*- coding:utf-8 -*-
from datetime import datetime
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin

db = SQLAlchemy()


class Base(db.Model):
    """ 所有 model 的一个基类，默认添加了时间戳
    """
    # 表示不要把这个类当作 Model 类
    __abstract__ = True
    # 设置了 default 和 onupdate 这俩个时间戳都不需要自己去维护
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,
                        default=datetime.utcnow,
                        onupdate=datetime.utcnow)

class User(Base,UserMixin):
    __tablename__ = 'user'

    ROLE_JOBSEEKER = 10
    ROLE_COMPANY = 20
    ROLE_ADMIN = 30

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True,index=True, nullable=False)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    _password = db.Column('password', db.String(256), nullable=False)
    role = db.Column(db.SmallInteger, default=ROLE_JOBSEEKER)

    @property
    def password(self):
        """ Python 风格的 getter """
        return self._password

    @password.setter
    def password(self, orig_password):
        """ Python 风格的 setter, 这样设置 user.password 就会
        自动为 password 生成哈希值存入 _password 字段
        """
        self._password = generate_password_hash(orig_password)

    def check_password(self, password):
        """ 判断用户输入的密码和存储的 hash 密码是否相等
        """
        return check_password_hash(self._password, password)

    def __repr__(self):
        return '<User:{}>'.format(self.username)

    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    @property
    def is_company(self):
        return self.role == self.ROLE_COMPANY


class jobseekerinfo(Base):
    __tablename__ = "jobseekerinfo"
    userid = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    name = db.Column(db.String(80),index=True)
    sex = db.Column(db.String(80))
    #birthday = db.Column(db.string(60))
    nativeplace = db.Column(db.String(30))
    phone = db.Column(db.String(30))
    resume = db.Column(db.String(256))#简历地址

class companyinfo(Base):
    __tablename__ = "companyinfo"

    companyid = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    company_name = db.Column(db.String(256),index=True)
    company_logo = db.Column(db.String(256),index=True)
    company_website = db.Column(db.String(256),index=True)
    company_profile = db.Column(db.String(256),index=True)
    company_address = db.Column(db.String(256),index=True)
    company_details = db.Column(db.String(256),index=True)


class job(Base):
    __tablename__ = "job"

    id = db.Column(db.Integer, primary_key=True)
    companyid = db.Column(db.Integer, db.ForeignKey('companyinfo.companyid'))
    jobtitle = db.Column(db.String(256),index=True)
    jobstatus = db.Column(db.Boolean,index=True)
    salaryrange = db.Column(db.String(256),index=True)
    ExperienceRequirement = db.Column(db.String(100),index=True)
    address = db.Column(db.String(256),index=True)           #地址
    JobDescriptions = db.Column(db.String(256),index=True) #职位描述
    jobrequirements = db.Column(db.String(256),index=True)  #职位要求


class Send(Base):
    __tablename__ = "Send"
    id = db.Column(db.Integer, primary_key=True)
    jobseekerid = db.Column(db.Integer, db.ForeignKey('jobseekerinfo.userid'), primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), primary_key=True)
    result = db.Column(db.Boolean) #求职结果
