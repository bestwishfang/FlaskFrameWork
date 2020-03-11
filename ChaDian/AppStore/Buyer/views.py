import time

from flask import request
from flask import render_template
from flask_restful import Resource

from . import buyer, apibuyer


@buyer.route('/buyer/base/')
def base():
    return render_template('buyer/base.html')


@buyer.route('/buyer/index/')
def index():
    return render_template('buyer/index.html')


@buyer.route('/buyer/about/')
def about():
    return render_template('buyer/about.html')