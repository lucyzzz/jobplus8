from flask import Blueprint, render_template, url_for, flash, redirect
import sys



front = Blueprint('front', __name__)


@front.route('/')
def index():
    return sys._getframe().f_code.co_name


@front.route('/login', methods=['GET', 'POST'])
def login():
    return sys._getframe().f_code.co_name

@front.route('/logout')
def logout():
    return sys._getframe().f_code.co_name

@front.route('/jobregister', methods=['GET', 'POST'])
def register_jobseeker():
    return sys._getframe().f_code.co_name


@front.route('/comregister', methods=['GET', 'POST'])
def register_company():
    return sys._getframe().f_code.co_name