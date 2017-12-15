from flask import Blueprint
import sys

admin = Blueprint('admin',__name__,url_prefix='/admin')

@admin.route('/')
def admin_index():
    return sys._getframe().f_code.co_name


@admin.route('/usermanage')
def usermanage():
    return sys._getframe().f_code.co_name


@admin.route('/postionmanage')
def postionmanage():
    return sys._getframe().f_code.co_name


