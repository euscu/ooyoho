# -*- coding: utf-8 -*-
# @Time    : 2017/3/30 23:49
# @Author  : euscu
# @remark  : 
__author__ = 'euscu'

from flask_script import Manager
from flask import Flask,render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.debug=True
manager = Manager(app)
bootstrap=Bootstrap(app)
@app.route('/')
def index():
    return render_template('myindex.html')

if __name__=="__main__":
    manager.run()