from flask import Blueprint
import sys

job = Blueprint('job',__name__,url_prefix='/job')


@job.route('/list')
def joblist():
    return sys._getframe().f_code.co_name

@job.route('/detail')
def jobdetail():
    return sys._getframe().f_code.co_name