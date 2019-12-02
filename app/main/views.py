from flask import render_template
from . import main

@main.route('/')
def index():

    title="Welcome to thy blogpost"
    return render_template('index.html', title=title)
