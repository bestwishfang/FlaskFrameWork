from flask import render_template

from apps.movie import movie, apimovie


@movie.route('/')
def index():
    return "Hello World!"


@movie.route('/base/')
def base():
    return render_template('movie/base.html')


@movie.route('/detail/')
def detail():
    return render_template('movie/detail.html')