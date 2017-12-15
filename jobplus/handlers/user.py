from flask import Blueprint
import sys
user = Blueprint('user',__name__,url_prefix='/user')




@user.route('/')
def user_index():
    pass


@user.route('/info',methods=['GET', 'POST'])
def user_info():
    return sys._getframe().f_code.co_name


@user.route('/infoedit',methods=['GET', 'POST']) #GET展示,POST编辑
def userinfo_edit():
    return sys._getframe().f_code.co_name

@user.route('/resumemanage') #简历管理
def resumemanage():
    return sys._getframe().f_code.co_name


@user.route('/postmanage') #投递管理
def postmanage():
    return sys._getframe().f_code.co_name