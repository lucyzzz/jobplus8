from flask import Blueprint
import sys

company = Blueprint('company',__name__,url_prefix='/company')


@company.route('/list')
def comlist():
    return sys._getframe().f_code.co_name


@company.route('/detail')
def comdetail():
    return sys._getframe().f_code.co_name


@company.route('/info') #信息配置页面
def cominfo():
    return sys._getframe().f_code.co_name


@company.route('/positionmanage') #职位管理
def positionmanage():
    return sys._getframe().f_code.co_name

@company.route('/resumemanage') #简历管理
def resumemanage():
    return sys._getframe().f_code.co_name